resource "aws_db_instance" "this" {
  allocated_storage      = 20
  engine                 = "postgres"
  engine_version         = "17.2"
  instance_class         = "db.t3.micro"
  db_name                = var.db_name
  username               = var.db_username
  password               = var.db_password
  skip_final_snapshot    = true
  vpc_security_group_ids = [var.db_security_group_id]

  tags = {
    Name        = "${var.environment}-postgres"
    Environment = var.environment
  }

}