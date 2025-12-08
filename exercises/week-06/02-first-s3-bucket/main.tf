# Tell Terraform we're using AWS
terraform {
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 5.0"
      }
    }
}

# Configure the AWS provider
provider "aws" {
    region = "us-east-1"
}

# Create an S3 bucket
resource "aws_s3_bucket" "my_first_bucket" {
    bucket = "ron-terraform-test-bucket-04040"
}
