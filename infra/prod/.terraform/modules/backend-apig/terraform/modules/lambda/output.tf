output "apig_invoke_arn" {
  value = aws_lambda_function.lambda.invoke_arn
}

output "apig_function_name" {
  value = aws_lambda_function.lambda.function_name
}