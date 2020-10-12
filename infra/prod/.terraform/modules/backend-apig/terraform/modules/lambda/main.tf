resource "aws_lambda_function" "lambda" {
    function_name = "app-${var.lambda_name}-${var.lambda_stage}"
    handler = var.lambda_handler
    runtime = "python3.8"

    filename = var.lambda_payload
    source_code_hash = filebase64sha256(var.lambda_payload)

    role = aws_iam_role.lambda_exec.arn
}

resource "aws_iam_role" "lambda_exec" {
   name = "role-${var.lambda_name}-${var.lambda_stage}"

   assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

}