# DevOps Learning Roadmap

## Overview

This repository documents my journey learning modern DevOps and cloud-native technologies. With 15 years of Linux systems administration experience managing production infrastructure, I'm expanding my skillset into container orchestration, infrastructure as code, and CI/CD automation through structured hands-on projects.

## Background

I currently manage production Linux infrastructure including:
- Proxmox virtualization clusters
- OPNsense firewalls and Ubiquiti networking
- AWS cloud services
- Docker containerized services (Gitea, oauth2-proxy, n8n, and others)
- Ansible automation and custom tooling

This repository represents my structured approach to learning enterprise-grade DevOps practices through hands-on projects and real-world implementations.

## Core Technologies

**Containerization & Orchestration**
- Docker and Docker Compose for multi-container applications
- Kubernetes for container orchestration (local development to AWS EKS)
- Helm for package management and deployments

**Infrastructure as Code**
- Terraform for AWS infrastructure provisioning
- Configuration management and state management
- Multi-environment deployments

**Databases**
- PostgreSQL (local, RDS, Kubernetes StatefulSets)
- Redis/Valkey for caching and performance optimization
- Database migrations and backup automation
- Connection pooling and high availability

**Development**
- Python for APIs, automation, and infrastructure tooling
- Advanced testing and code quality practices
- REST API development and async programming

**CI/CD**
- GitHub Actions for automated testing and deployment
- Container image building and registry management
- Infrastructure deployment automation

## Repository Structure

```
.
├── projects/          # Hands-on projects for each technology phase
├── infra/             # Terraform modules and Helm charts
├── docs/              # Architecture diagrams, notes, and documentation
├── exercises/         # Weekly exercises
├── .github/workflows/ # CI/CD pipeline definitions
├── learning-plan.md   # Detailed 6-month learning roadmap
```

## Current Progress

**Completed:**
- Docker fundamentals and multi-stage builds
- Container optimization and production best practices
- Docker Compose for local development environments

**In Progress:**
- Python Flask API development
- Multi-container applications with PostgreSQL
- Production-ready Docker configurations

**Upcoming:**
- Terraform for AWS infrastructure
- Kubernetes deployment patterns
- CI/CD pipeline implementation

## Projects

As projects are completed, they will be linked here with architecture diagrams and deployment documentation.

### Month 1: Multi-Container Applications (5 weeks)
- Flask REST API with PostgreSQL backend
- Docker Compose production patterns
- Database persistence and health checks
- **Lambda to Docker Migration**: Real-world serverless-to-container migration demonstrating reduced operational complexity and infrastructure portability

### Month 2: Cloud Infrastructure
- Terraform-managed AWS infrastructure
- RDS PostgreSQL deployment
- EC2 application hosting

### Month 3-4: Kubernetes
- Application deployment on Kubernetes
- StatefulSets for database workloads
- Helm chart development
- AWS EKS cluster management

### Month 5: Advanced Python & Testing
- Advanced Flask patterns with HTMX for dynamic interfaces
- Redis/Valkey caching for performance optimization
- Comprehensive testing with pytest
- Database migrations with Alembic
- CLI tools and infrastructure automation

### Month 6: CI/CD & Automation
- GitHub Actions pipelines
- Automated infrastructure deployment
- Database backup automation
- Monitoring and alerting

## Learning Approach

This roadmap emphasizes practical, production-ready implementations over theoretical knowledge. Each project includes:
- Working code with comprehensive documentation
- Architecture diagrams and design decisions
- Troubleshooting guides and lessons learned
- Screenshots and deployment evidence

## Goals

The skills and practices demonstrated in this repository focus on:
- Cloud-native application deployment
- Infrastructure automation and consistency
- Production reliability and monitoring
- Security best practices
- Documentation and knowledge sharing

## Connect

This is an active learning repository. Check the commit history and project folders to see current progress and implementations.

---

*Last Updated: November 2025*
