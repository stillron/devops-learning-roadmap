variable "environment" {
  description = "Environment name"
  type        = string

}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"

}

variable "ssh_key_name" {
  description = "SSH key pair name"
  type        = string

}

variable "security_group_ids" {
  description = "List of security group ids"
  type        = list(string)

}

variable "db_address" {
  description = "Database endpoint address"
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