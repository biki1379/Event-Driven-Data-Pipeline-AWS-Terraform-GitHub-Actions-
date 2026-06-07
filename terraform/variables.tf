variable "bucket_name" {
  type        = string
  description = "Name of the S3 bucket for data storage"
}

variable "aws_region" {
  type        = string
  description = "AWS region to deploy resources into"
  default     = "ap-south-1"
}

variable "lambda_function_name" {
  type        = string
  description = "Name of the Lambda function"
  default     = "dataProcessorFunction"
}

variable "lambda_runtime" {
  type        = string
  description = "Runtime for the Lambda function"
  default     = "python3.13"
}
