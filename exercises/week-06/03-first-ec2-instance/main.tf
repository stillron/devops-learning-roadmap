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

variable "my_ip" {
  description = "My work IP address for SSH access"
  type        = string
}

data "aws_ami" "amazon_linux_2023" {
    most_recent = true
    owners      = ["amazon"]

    filter {
        name = "name"
        values = ["al2023-ami-*-x86_64"]
    }
}

resource "aws_security_group" "allow_ssh_from_work" {
    name                = "allow_ssh_from_work"
    description         = "Allow inbound SSH traffic from work"

    tags    = {
        Name = "allow_ssh_from_work"
    }
}

resource "aws_vpc_security_group_ingress_rule" "allows_ssh_ipv4" {
    security_group_id = aws_security_group.allow_ssh_from_work.id
    cidr_ipv4 = var.my_ip
    from_port = 22
    ip_protocol = "tcp"
    to_port = 22
}

resource "aws_instance" "my_first_ec2" {
    ami             = data.aws_ami.amazon_linux_2023.id
    instance_type   = "t2.micro"
    key_name        = "terraform-learning-key"
    vpc_security_group_ids = [aws_security_group.allow_ssh_from_work.id]

    tags = {
        Name = "my-first-terraform-ec2"
    }
}