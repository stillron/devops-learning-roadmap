output "db_address" {
  description = "Database endpoint address"
  value       = aws_db_instance.this.address

}

output "db_name" {
  description = "Database name"
  value       = aws_db_instance.this.db_name

}