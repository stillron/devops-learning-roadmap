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
    owners    = ["amazon"]

    filter {
        name = "name"
        values = ["al2023-ami-*-x86_64"]
    }
}

resource "aws_security_group" "allow_ssh" {
    name        = "allow-ssh-practice"
    description = "Allow SSH from my IP"

    tags = {
        Name = "allow-ssh-practice"
    }
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh_from_work" {
    security_group_id   = aws_security_group.allow_ssh.id
    cidr_ipv4           = var.my_ip
    from_port           = 22
    to_port             = 22
    ip_protocol = "tcp"
}

resource "aws_instance" "my_ec2" {
    ami             = data.aws_ami.amazon_linux_2023.id
    instance_type   = "t2.micro"
    key_name        = "terraform-learning-key"
    vpc_security_group_ids = [aws_security_group.allow_ssh.id]

    tags = {
        Name = "practice-ec2-round-2"
    }
}