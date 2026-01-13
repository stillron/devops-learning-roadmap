resource "aws_security_group" "base_sg" {
  description = "Base security group"

  tags = {
    Name        = "${var.environment}-base-sg"
    Environment = var.environment
  }

}

resource "aws_vpc_security_group_egress_rule" "allow_traffic_out" {
  security_group_id = aws_security_group.base_sg.id
  ip_protocol       = "-1"
  cidr_ipv4         = "0.0.0.0/0"
}

resource "aws_security_group" "admin_sg" {
  description = "Admin security group"

  tags = {
    Name        = "${var.environment}-admin-sg"
    Environment = var.environment
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh_from_work" {
  security_group_id = aws_security_group.admin_sg.id
  ip_protocol       = "tcp"
  cidr_ipv4         = var.admin_ip
  from_port         = "22"
  to_port           = "22"

}

resource "aws_security_group" "web_sg" {
  description = "Web security group"

  tags = {
    Name        = "${var.environment}-web-sg"
    Environment = var.environment
  }
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

  tags = {
    Name        = "${var.environment}-db-sg"
    Environment = var.environment
  }

}

resource "aws_vpc_security_group_ingress_rule" "allow_pg_from_ec2" {
  security_group_id            = aws_security_group.db_sg.id
  referenced_security_group_id = aws_security_group.base_sg.id
  ip_protocol                  = "tcp"
  from_port                    = "5432"
  to_port                      = "5432"

}