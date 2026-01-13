data "aws_ami" "debian13" {
  most_recent = true
  owners      = ["136693071363"]

  filter {
    name   = "name"
    values = ["debian-13-amd64*"]
  }

}

resource "aws_instance" "this" {
  ami                    = data.aws_ami.debian13.id
  instance_type          = var.instance_type
  key_name               = var.ssh_key_name
  vpc_security_group_ids = var.security_group_ids

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
      -e POSTGRES_USER="${var.db_username}" \
      -e POSTGRES_PASSWORD="${var.db_password}" \
      -e POSTGRES_DBHOST="${var.db_address}" \
      -e POSTGRES_DB="${var.db_name}" \
      stillron/flask-app:latest
  EOF

  tags = {
    Name        = "${var.environment}-flask-server"
    Environment = var.environment
  }

}