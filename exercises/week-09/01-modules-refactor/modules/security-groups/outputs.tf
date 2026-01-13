output "base_sg_id" {
  description = "ID of base security group"
  value       = aws_security_group.base_sg.id

}

output "admin_sg_id" {
  description = "ID of admin security group"
  value       = aws_security_group.admin_sg.id

}

output "web_sg_id" {
  description = "ID of web security group"
  value       = aws_security_group.web_sg.id

}

output "db_sg_id" {
  description = "ID of database security group"
  value       = aws_security_group.db_sg.id
}