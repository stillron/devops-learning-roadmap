terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

data "aws_security_group" "web_sg" {
  name = "web_sg"
}

output "security_group_id" {
  value = data.aws_security_group.web_sg.id
}