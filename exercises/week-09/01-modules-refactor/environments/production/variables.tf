variable "my_username" {
  description = "RDS Username"
  type        = string
}

variable "my_password" {
  description = "RDS password"
  type        = string
  sensitive   = true

}

variable "my_ssh_key" {
  description = "EC2 SSH key name"
  type        = string

}

variable "my_ip" {
  description = "IP address for SSH access"
  type        = string

}