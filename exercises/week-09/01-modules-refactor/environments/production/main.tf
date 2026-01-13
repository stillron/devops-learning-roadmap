terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>6.0"
    }
  }

  backend "s3" {
    bucket         = "ron-terraform-state-learning"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-locks"
    encrypt        = true

  }
}

provider "aws" {
  region = "us-east-1"

}

# Security groups module
module "security_groups" {
  source = "../../modules/security-groups"

  environment = "production"
  admin_ip    = var.my_ip

}

# Database module
module "database" {
  source = "../../modules/database"

  environment          = "production"
  db_name              = "flaskdb"
  db_username          = var.my_username
  db_password          = var.my_password
  db_security_group_id = module.security_groups.db_sg_id

}

# Compute module
module "compute" {
  source = "../../modules/compute"

  environment  = "production"
  ssh_key_name = var.my_ssh_key
  security_group_ids = [
    module.security_groups.base_sg_id,
    module.security_groups.admin_sg_id,
    module.security_groups.web_sg_id,
  ]

  db_address  = module.database.db_address
  db_name     = module.database.db_name
  db_username = var.my_username
  db_password = var.my_password


}

output "ec2_public_ip" {
  description = "EC2 public IP address"
  value       = module.compute.public_ip
}