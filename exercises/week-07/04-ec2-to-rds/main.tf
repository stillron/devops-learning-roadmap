terraform {
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 6.0"
      }
    }
}

provider "aws" {
    region = "us-east-1"
}

variable "my_username" {
    description = "rds username"
    type = string
  
}

variable "my_password" {
  description = "rds password"
  type = string
}

variable "my_ip" {
    description = "my work ip address"
    type = string
}

data "aws_ami" "debian13" {
    most_recent = true
    owners = ["136693071363"]

    filter {
      name = "name"
      values = ["debian-13-amd64-*"]
    }
  
}

resource "aws_security_group" "ec2_sg" {
    description = "for ec2 administration"
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh" {
    security_group_id = aws_security_group.ec2_sg.id
    ip_protocol = "tcp"
    from_port = 22
    to_port = 22
    cidr_ipv4 = var.my_ip
}

resource "aws_vpc_security_group_egress_rule" "allow_all_out" {
    security_group_id = aws_security_group.ec2_sg.id
    ip_protocol = "-1"
    cidr_ipv4 = "0.0.0.0/0"
  
}

resource "aws_security_group" "db_sg" {
    description = "for connection to rds"
  
}

resource "aws_vpc_security_group_ingress_rule" "allow_from_pc" {
    security_group_id = aws_security_group.db_sg.id
    ip_protocol = "tcp"
    cidr_ipv4 = var.my_ip
    from_port = 5432
    to_port = 5432
  
}

resource "aws_vpc_security_group_ingress_rule" "allow_from_ec2" {
    security_group_id = aws_security_group.db_sg.id
    ip_protocol = "tcp"
    from_port = 5432
    to_port = 5432
    referenced_security_group_id = aws_security_group.ec2_sg.id
  
}

resource "aws_instance" "my_ec2_to_rds" {
    ami = data.aws_ami.debian13.id
    instance_type = "t3.micro"
    key_name = "terraform-learning-key"
    vpc_security_group_ids = [aws_security_group.ec2_sg.id]

    tags = {
        Name = "ec2-to-rds-test"
    }
  
}

resource "aws_db_instance" "my_rds" {
    identifier = "ec2-to-rds-db"
    instance_class = "db.t3.micro"
    engine = "postgres"
    allocated_storage = 20
    username = var.my_username
    password = var.my_password
    skip_final_snapshot = true
    publicly_accessible = true
    vpc_security_group_ids = [aws_security_group.db_sg.id]
  
}