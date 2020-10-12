# Stage
variable "lambda_stage" {
  type = string
}

# Lambda Name
variable "lambda_name" {
  type = string
}

# Lambda Handler
variable "lambda_handler" {
    type = string
    default = "lambda_function.lambda_handler"
}

# Payload
variable "lambda_payload" {
    type = string
    default = "payload.zip"
}