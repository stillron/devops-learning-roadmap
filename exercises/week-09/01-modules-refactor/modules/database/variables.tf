variable "environment" {
  description = "Environment name"
  type        = string

}

variable "db_name" {
  description = "Database name"
  type        = string
}

variable "db_username" {
  description = "Database user name"
  type        = string

}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

variable "db_security_group_id" {
  description = "Database security group id"
  type        = string

}