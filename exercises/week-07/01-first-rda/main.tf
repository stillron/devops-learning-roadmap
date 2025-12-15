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
  description = "Username for rds"
  type        = string
}

variable "my_password" {
  description = "Password for rds"
  type        = string

}

variable "my_ip" {
  description = "my work ip address"
  type        = string

}

resource "aws_security_group" "db_sg" {
  name        = "db_sg"
  description = "Security group for db"
}

resource "aws_vpc_security_group_ingress_rule" "allow_postgres_from_work" {
  security_group_id = aws_security_group.db_sg.id
  cidr_ipv4         = var.my_ip
  from_port         = 5432
  to_port           = 5432
  ip_protocol       = "tcp"
}

resource "aws_db_instance" "learning_db" {
  identifier             = "my-first-rds"
  allocated_storage      = 20
  engine                 = "postgres"
  instance_class         = "db.t3.micro"
  username               = var.my_username
  password               = var.my_password
  skip_final_snapshot    = true
  publicly_accessible = true
  vpc_security_group_ids = [aws_security_group.db_sg.id]

}