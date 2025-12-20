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

variable "my_username" {
  description = "RDS username"
  type        = string

}

variable "my_password" {
  description = "RDS password"
  type        = string
  sensitive   = true
}

variable "my_ip" {
  description = "work IP address"
  type        = string

}

data "aws_secretsmanager_secret_version" "rds_credentials" {
  secret_id = "learning-rds-credentials"

}

locals {
  db_creds = jsondecode(data.aws_secretsmanager_secret_version.rds_credentials.secret_string)
}

resource "aws_secretsmanager_secret" "rds_credentials" {
  name        = "learning-rds-credentials"
  description = "RDS credentials for learning project"

}

resource "aws_secretsmanager_secret_version" "rds_credentials" {
  secret_id = aws_secretsmanager_secret.rds_credentials.id
  secret_string = jsonencode({
    username = var.my_username
    password = var.my_password
    ip       = var.my_ip
  })

}

resource "aws_security_group" "db_sg" {
  name        = "db_sg"
  description = "RDS security group"

}

resource "aws_vpc_security_group_ingress_rule" "allow_postgres" {
  security_group_id = aws_security_group.db_sg.id
  ip_protocol       = "tcp"
  from_port         = 5432
  to_port           = 5432
  cidr_ipv4         = local.db_creds.ip

}

resource "aws_db_instance" "my-rds" {
  identifier             = "my-rds-05"
  instance_class         = "db.t3.micro"
  engine                 = "postgres"
  allocated_storage      = 20
  skip_final_snapshot    = true
  publicly_accessible    = true
  username               = local.db_creds.username
  password               = local.db_creds.password
  vpc_security_group_ids = [aws_security_group.db_sg.id]

}