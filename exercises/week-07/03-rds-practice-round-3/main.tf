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
  description = "username for rds"
  type        = string

}

variable "my_password" {
  description = "password for rds"
  type        = string
}

variable "my_ip" {
  description = "my work ip address"
  type        = string

}

resource "aws_security_group" "postgres_sg" {
  name        = "postgres_sg"
  description = "security group for postgres db"

}

resource "aws_vpc_security_group_ingress_rule" "allow_postgres" {
  security_group_id = aws_security_group.postgres_sg.id
  ip_protocol       = "tcp"
  from_port         = 5432
  to_port           = 5432
  cidr_ipv4         = var.my_ip
}

resource "aws_db_instance" "learning_db" {
  identifier             = "my-third-rds"
  instance_class         = "db.t3.micro"
  allocated_storage      = 20
  engine                 = "postgres"
  username               = var.my_username
  password               = var.my_password
  publicly_accessible    = true
  skip_final_snapshot    = true
  vpc_security_group_ids = [aws_security_group.postgres_sg.id]

}
