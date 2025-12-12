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

variable "my_ip" {
  description = "My work IP address for SSH access"
  type        = string
}

data "aws_ami" "debian13" {
  most_recent = true
  owners      = ["136693071363"]

  filter {
    name   = "name"
    values = ["debian-13-amd64*"]
  }
}

resource "aws_security_group" "base_sg" {
  name        = "base_sg"
  description = "Allow all outbound traffic"

  tags = {
    Name = "base_sg-practice"
  }
}

resource "aws_security_group" "admin_sg" {
  name        = "admin_sg"
  description = "Allow SSH from my ip"

  tags = {
    Name = "admin_sg-practice"
  }
}

resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Allow ports 80, 443"

  tags = {
    Name = "web_sg=practice"
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh_from_work" {
  security_group_id = aws_security_group.admin_sg.id
  cidr_ipv4         = var.my_ip
  from_port         = 22
  to_port           = 22
  ip_protocol       = "tcp"
}

resource "aws_vpc_security_group_ingress_rule" "allow_web_80" {
  security_group_id = aws_security_group.web_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 80
  to_port           = 80
  ip_protocol       = "tcp"

}

resource "aws_vpc_security_group_ingress_rule" "allow_web_443" {
  security_group_id = aws_security_group.web_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 443
  to_port           = 443
  ip_protocol       = "tcp"
}

resource "aws_vpc_security_group_egress_rule" "all_all_outbound" {
  security_group_id = aws_security_group.base_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

resource "aws_instance" "my_ec2" {
  ami           = data.aws_ami.debian13.id
  instance_type = "t2.micro"
  key_name      = "terraform-learning-key"
  vpc_security_group_ids = [
    aws_security_group.base_sg.id,
    aws_security_group.admin_sg.id,
    aws_security_group.web_sg.id
  ]

  user_data = <<-EOF
    #!/bin/bash
    apt update && apt upgrade -y
    apt install -y nginx
    systemctl enable --now nginx
  EOF

  tags = {
    Name = "practice-ec2-round-3"
  }
}

