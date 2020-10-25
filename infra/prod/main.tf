terraform {
  backend "s3" {
    bucket = "sentimentalists-terraform"
    key    = "backend-prod"
    region = "eu-west-2"
  }
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}

data "terraform_remote_state" "apig" {
  backend = "s3"
  config = {
    bucket = "sentimentalists-terraform"
    key    = "shared-prod"
    region = "eu-west-2"
  }
}

module "backend-lambda" {
  source         = "github.com/TheSentimentalists/SentimentalistsApp-Infrastructure/terraform/modules/lambda"
  lambda_stage   = "prod"
  lambda_name    = "sentimentalists-backend"
  lambda_payload = var.payload
}

module "backend-apig-lambdaresource" {
  source               = "github.com/TheSentimentalists/SentimentalistsApp-Infrastructure/terraform/modules/apigateway_resource"
  apig_id              = data.terraform_remote_state.apig.outputs.apig_id
  apig_root_id         = data.terraform_remote_state.apig.outputs.apig_root_id
  apig_execution_arn   = data.terraform_remote_state.apig.outputs.apig_execution_arn
  lambda_arn           = module.backend-lambda.apig_invoke_arn
  lambda_function_name = module.backend-lambda.apig_function_name
}

module "backend-apig-deployment" {
  source     = "github.com/TheSentimentalists/SentimentalistsApp-Infrastructure/terraform/modules/apigateway_deploy"
  apig_id    = data.terraform_remote_state.apig.outputs.apig_id
  apig_stage = "prod"
  depends_on = [module.backend-apig-lambdaresource]
}