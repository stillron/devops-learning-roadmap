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
  description = "rds username"
  type        = string

}

variable "my_password" {
  description = "rds password"
  type        = string
  sensitive   = true
}

variable "my_ssh_key" {
  description = "ec2 ssh key name"
  type        = string
}

variable "my_ip" {
  description = "work ip"
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
  description = "Base security group"
}

resource "aws_vpc_security_group_egress_rule" "allow_traffic_out" {
  security_group_id = aws_security_group.base_sg.id
  ip_protocol       = "-1"
  cidr_ipv4         = "0.0.0.0/0"
}

resource "aws_security_group" "admin_sg" {
  description = "Admin security group"

}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh_from_work" {
  security_group_id = aws_security_group.admin_sg.id
  ip_protocol       = "tcp"
  cidr_ipv4         = var.my_ip
  from_port         = "22"
  to_port           = "22"
}

resource "aws_security_group" "web_sg" {
  description = "Web security group"

}

resource "aws_vpc_security_group_ingress_rule" "allow_http_traffic" {
  security_group_id = aws_security_group.web_sg.id
  ip_protocol       = "tcp"
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = "80"
  to_port           = "80"
}

resource "aws_security_group" "db_sg" {
  description = "Database security group"
}

resource "aws_vpc_security_group_ingress_rule" "allow_pg_from_ec2" {
  security_group_id            = aws_security_group.db_sg.id
  referenced_security_group_id = aws_security_group.base_sg.id
  from_port                    = 5432
  to_port                      = 5432
  ip_protocol                  = "tcp"

}

resource "aws_db_instance" "flask_db" {
  allocated_storage      = 20
  engine                 = "postgres"
  engine_version         = "17.2"
  instance_class         = "db.t3.micro"
  db_name                = "flaskdb"
  username               = var.my_username
  password               = var.my_password
  skip_final_snapshot    = true
  vpc_security_group_ids = [aws_security_group.db_sg.id]
}

resource "aws_instance" "flask_server" {
  ami                    = data.aws_ami.debian13.id
  instance_type          = "t3.micro"
  key_name               = var.my_ssh_key
  vpc_security_group_ids = [aws_security_group.admin_sg.id, aws_security_group.base_sg.id, aws_security_group.web_sg.id]

  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y docker.io
    systemctl start docker
    systemctl enable docker
    docker pull stillron/flask-app:latest
    docker run -d \
      --name flask-app \
      --restart unless-stopped \
      -p 80:5000 \
      -e POSTGRES_USER="${var.my_username}" \
      -e POSTGRES_PASSWORD="${var.my_password}" \
      -e POSTGRES_DBHOST="${aws_db_instance.flask_db.address}" \
      -e POSTGRES_DB="flaskdb" \
      stillron/flask-app:latest
  EOF

  tags = {
    Name = "flask-app-server"
  }

}

output "ec2_public_ip" {
  description = "EC2 public ip"
  value       = aws_instance.flask_server.public_ip

}