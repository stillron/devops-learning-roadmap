variable "environment" {
  description = "Environment name (production, staging, etc)"
  type        = string
}

variable "admin_ip" {
  description = "IP address allowed SSH access"
  type        = string

}