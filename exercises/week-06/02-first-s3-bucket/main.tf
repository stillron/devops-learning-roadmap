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

    tags = {
        Name        = "My first Terraform bucket"
        Environment = "Learning"
    }
}

resource "aws_s3_bucket_public_access_block" "my_first_bucket" {
    bucket = aws_s3_bucket.my_first_bucket.id

    block_public_acls   = true
    block_public_policy = true
    ignore_public_acls = true
    restrict_public_buckets = true
}

resource "aws_s3_object" "test_file" {
    bucket = aws_s3_bucket.my_first_bucket.id
    key = "hello.txt"
    content = "Hello from Terraform S3!"
}
