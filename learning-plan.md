# 🧭 DevOps Career Transition Plan (6 Months)
**Goal:** Move into a Senior DevOps/Infrastructure Engineer role mastering Docker, Kubernetes, Terraform, Python, Go, and PostgreSQL  
**Pace:** Standard (10–12 hrs/week)  
**Cloud:** AWS Free Tier  
**Languages:** Python-first, Go later  
**Starting Point:** Docker fundamentals complete, now building multi-container applications

---

## 📅 Month 1 – Python + Multi-Container Applications
**Theme:** Python refresher + Docker Compose production patterns + PostgreSQL

---

### Week 1 – Python Environment + Simple API ✅/🕐/❌
Planned hours: 10 | Actual: 7

#### Tasks
- [x] Set up Python 3.12 + Poetry/venv
- [x] Review Python fundamentals: dicts, loops, list comprehensions, JSON
- [x] Write a simple Flask REST API with 3-4 endpoints (GET, POST)
- [x] Practice `requests` library for API calls
- [ ] Containerize the Flask app (single-stage Dockerfile)

#### Resources
- [Python Official Tutorial](https://docs.python.org/3/tutorial/) (review chapters 3-5, 9)
- [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- [Python requests Library](https://requests.readthedocs.io/en/latest/)

#### Proof of Completion
- Git commit: Flask API with requirements.txt
- Screenshot: API responses (via curl or Postman)
- Dockerfile that builds and runs the app

#### Reflection
**What I learned:**  
**What broke:**  
**What I'll improve next week:**  

---

### Week 2 – Docker Compose + PostgreSQL Integration ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Install PostgreSQL locally and practice basic queries
- [ ] Create `docker-compose.yml` for Flask + Postgres
- [ ] Add persistent volume for Postgres data
- [ ] Store credentials in `.env` file (use python-dotenv)
- [ ] Connect Flask to Postgres using psycopg2 or SQLAlchemy
- [ ] Implement basic CRUD endpoints (Create, Read, Update, Delete)

#### Resources
- [PostgreSQL psql Basics](https://www.postgresql.org/docs/current/app-psql.html)
- [Docker Compose](https://docs.docker.com/compose/)
- [psycopg2 Docs](https://www.psycopg.org/docs/) or [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)

#### Proof of Completion
- `docker-compose.yml` with Flask + Postgres + volume
- JSON API responses showing data from database
- Data persists after `docker compose down/up`

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 3 – Production-Ready Multi-Container Stack ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Add pgAdmin or Adminer to docker-compose.yml for database management
- [ ] Implement healthchecks for both Flask and Postgres
- [ ] Add resource limits (memory, CPU)
- [ ] Configure proper logging (JSON format for Flask)
- [ ] Add restart policies
- [ ] Test failure scenarios (kill Postgres, watch Flask handle it)

#### Resources
- [Compose Healthcheck](https://docs.docker.com/compose/compose-file/05-services/#healthcheck)
- [Docker Resource Constraints](https://docs.docker.com/config/containers/resource_constraints/)
- [pgAdmin Docker](https://hub.docker.com/r/dpage/pgadmin4)

#### Proof of Completion
- Screenshot of pgAdmin connected to database
- Healthcheck status in `docker compose ps`
- Logs showing graceful handling of database connection issues

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 4 – Documentation + Architecture Diagrams ✅/🕐/❌
Planned hours: 8 | Actual: ___  

#### Tasks
- [ ] Write comprehensive README.md with setup instructions
- [ ] Create architecture diagram (Mermaid or draw.io)
- [ ] Document API endpoints (consider using Swagger/OpenAPI)
- [ ] Add troubleshooting section to README
- [ ] Push to GitHub with proper .gitignore
- [ ] Write a brief blog post or LinkedIn post about what you built

#### Resources
- [Mermaid Diagrams for Markdown](https://mermaid.js.org/)
- [Flask-RESTX for API docs](https://flask-restx.readthedocs.io/)
- [README Best Practices](https://github.com/matiassingers/awesome-readme)

#### Proof of Completion
- GitHub repo link with polished README
- Architecture diagram showing Flask → Postgres network
- Screenshot of running containers

#### Reflection
**Wins:**  
**Challenges:**  
**Next Month Focus:**  

---

## 📅 Month 2 – Terraform + AWS Cloud Infrastructure
**Theme:** Infrastructure as Code + Cloud Postgres (RDS)

---

### Week 5 – Terraform Fundamentals ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Install Terraform + AWS CLI
- [ ] Create IAM user with appropriate permissions
- [ ] Learn Terraform basics: providers, resources, variables, outputs
- [ ] Write `main.tf` to provision a simple EC2 instance
- [ ] Practice `terraform init`, `plan`, `apply`, `destroy`
- [ ] Output the instance public IP

#### Resources
- [Terraform AWS Tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)
- [AWS CLI Setup](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

#### Proof
- `terraform apply` output showing created resources
- SSH connection to the EC2 instance
- Screenshot of EC2 console showing your instance

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 6 – RDS PostgreSQL + Security Groups ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Create RDS PostgreSQL instance using Terraform
- [ ] Configure security groups for database access
- [ ] Store RDS credentials in AWS Secrets Manager
- [ ] Connect to RDS from local machine using psql
- [ ] Test connection from EC2 instance

#### Resources
- [AWS RDS Terraform Resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/db_instance)
- [Terraform Variables](https://developer.hashicorp.com/terraform/language/values/variables)
- [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

#### Proof
- Screenshot of AWS RDS dashboard showing running instance
- Successful psql connection output
- Terraform state showing security group rules

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 7 – Deploy Flask App to EC2 + Connect to RDS ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Use Terraform to provision EC2 with Docker installed (user_data script)
- [ ] Deploy your Flask app container to EC2
- [ ] Update Flask app to connect to RDS instead of local Postgres
- [ ] Configure environment variables for RDS endpoint
- [ ] Test the full stack: EC2 Flask → RDS

#### Resources
- [Terraform EC2 User Data](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#user_data)
- [Docker on Amazon Linux](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)

#### Proof
- Flask API responding from public EC2 IP
- Database queries hitting RDS
- Architecture diagram: Internet → EC2 (Flask) → RDS

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 8 – Terraform Best Practices + Remote State ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Organize Terraform code: modules, variables.tf, outputs.tf
- [ ] Set up remote state in S3 + DynamoDB for locking
- [ ] Add tags to all resources
- [ ] Implement terraform workspace for dev/staging
- [ ] Document your Terraform structure

#### Resources
- [Terraform Modules](https://developer.hashicorp.com/terraform/language/modules)
- [S3 Backend Configuration](https://developer.hashicorp.com/terraform/language/settings/backends/s3)
- [Terraform Workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces)

#### Proof
- Well-organized Terraform directory structure
- S3 bucket containing terraform.tfstate
- Screenshot showing terraform workspace list

#### Reflection
**Wins:**  
**Challenges:**  
**Next Month Focus:**  

---

## 📅 Month 3 – Kubernetes Fundamentals
**Theme:** Deploy applications on Kubernetes (minikube → cloud concepts)

**Note:** This month focuses on understanding Kubernetes core concepts. CKA certification prep will come later in your timeline (April 2026).

---

### Week 9 – Kubernetes Core Concepts ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Install kubectl and minikube (or kind)
- [ ] Learn Pods, ReplicaSets, Deployments
- [ ] Practice imperative commands: `kubectl run`, `kubectl create`
- [ ] Write your first YAML manifests
- [ ] Deploy nginx and expose it with a Service
- [ ] Practice `kubectl get`, `describe`, `logs`, `exec`

#### Resources
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

#### Proof
- Screenshot: `kubectl get pods,deployments,svc`
- YAML manifest files in Git
- Screenshot showing Service endpoint responding

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 10 – Deploy Flask App to Kubernetes ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Create Deployment for your Flask app
- [ ] Create Service (ClusterIP or LoadBalancer)
- [ ] Add ConfigMap for environment variables
- [ ] Add Secret for database credentials
- [ ] Test pod restart/rollout scenarios
- [ ] Practice rolling updates

#### Resources
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

#### Proof
- Flask app running in Kubernetes
- Screenshot of successful API calls
- ConfigMap and Secret manifests

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 11 – StatefulSets + Persistent Storage ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Learn about PersistentVolumes and PersistentVolumeClaims
- [ ] Deploy PostgreSQL as a StatefulSet
- [ ] Configure PVC for database persistence
- [ ] Connect Flask app to PostgreSQL in K8s
- [ ] Test data persistence after pod deletion

#### Resources
- [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)

#### Proof
- StatefulSet running with PVC
- Data survives pod deletion/recreation
- Screenshot: `kubectl get pods,pvc,pv`

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 12 – Introduction to Helm ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Install Helm 3
- [ ] Learn Helm concepts: Charts, Values, Releases
- [ ] Deploy PostgreSQL using Bitnami Helm chart
- [ ] Create a simple Helm chart for your Flask app
- [ ] Practice `helm install`, `upgrade`, `rollback`

#### Resources
- [Helm Quickstart](https://helm.sh/docs/intro/quickstart/)
- [Bitnami PostgreSQL Chart](https://artifacthub.io/packages/helm/bitnami/postgresql)
- [Creating Helm Charts](https://helm.sh/docs/topics/charts/)

#### Proof
- Helm releases list
- PostgreSQL deployed via Helm
- Custom Helm chart in Git

#### Reflection
**Wins:**  
**Challenges:**  
**Next Month Focus:**  

---

## 📅 Month 4 – Cloud Kubernetes + Advanced Terraform
**Theme:** EKS deployment + Infrastructure as Code for K8s

---

### Week 13-14 – EKS Cluster with Terraform ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Use Terraform to provision an EKS cluster
- [ ] Configure kubectl to access EKS
- [ ] Deploy a simple app to verify cluster works
- [ ] Understand node groups and autoscaling
- [ ] Set up IAM roles for service accounts (IRSA)

#### Resources
- [Terraform EKS Module](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest)
- [AWS EKS Getting Started](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
- [EKS Best Practices](https://aws.github.io/aws-eks-best-practices/)

#### Proof
- EKS cluster visible in AWS Console
- kubectl connected to EKS
- Sample deployment running

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 15 – Deploy Full Stack to EKS ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Deploy Flask app to EKS using your Helm chart
- [ ] Connect to RDS PostgreSQL from EKS
- [ ] Configure security groups for EKS → RDS access
- [ ] Set up Application Load Balancer (ALB) Ingress
- [ ] Test the full production-like setup

#### Resources
- [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)
- [EKS Security Groups](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

#### Proof
- Application accessible via ALB URL
- Database connection working from EKS
- Architecture diagram: Internet → ALB → EKS → RDS

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 16 – Monitoring + Cost Management ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Set up CloudWatch Container Insights
- [ ] Configure kubectl logs and metrics-server
- [ ] Review AWS billing and tag resources
- [ ] Practice terraform destroy and cleanup
- [ ] Document your infrastructure costs

#### Resources
- [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)
- [Kubernetes Metrics Server](https://github.com/kubernetes-sigs/metrics-server)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

#### Proof
- CloudWatch dashboard screenshot
- Cost breakdown report
- Clean terraform destroy output

#### Reflection
**Wins:**  
**Challenges:**  
**Next Month Focus:**  

---

## 📅 Month 5 – Go Language + Database Migrations
**Theme:** Learn Go, build tooling, automate database schema changes

---

### Week 17 – Go Fundamentals ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Complete Tour of Go
- [ ] Write basic Go programs: file I/O, HTTP client, JSON parsing
- [ ] Build a simple CLI tool using cobra or flags
- [ ] Practice Go testing with the testing package
- [ ] Containerize a Go application (multi-stage build)

#### Resources
- [Tour of Go](https://go.dev/tour/)
- [Effective Go](https://go.dev/doc/effective_go)
- [Cobra CLI Framework](https://github.com/spf13/cobra)

#### Proof
- Completed Go exercises
- CLI tool that performs a useful task
- Multi-stage Dockerfile for Go app

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 18 – Go + PostgreSQL Integration ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Use pgx driver to connect to PostgreSQL from Go
- [ ] Build a Go API with http or Gin framework
- [ ] Implement CRUD operations in Go
- [ ] Add proper error handling and logging
- [ ] Write tests for your database functions

#### Resources
- [pgx PostgreSQL Driver](https://github.com/jackc/pgx)
- [Gin Web Framework](https://gin-gonic.com/)
- [Go Database/SQL Tutorial](https://go.dev/doc/database/querying)

#### Proof
- Go API responding to HTTP requests
- Database queries working from Go
- Test coverage report

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 19 – Database Migrations ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Learn database migration concepts
- [ ] Use golang-migrate or atlas for schema management
- [ ] Create migration files (up/down)
- [ ] Test migrations against local and RDS databases
- [ ] Integrate migrations into application startup

#### Resources
- [golang-migrate](https://github.com/golang-migrate/migrate)
- [Atlas Migrations](https://atlasgo.io/)
- [Database Migration Best Practices](https://www.prisma.io/dataguide/types/relational/what-are-database-migrations)

#### Proof
- Migration files in Git
- Successful up/down migration runs
- Database schema version tracking

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 20 – Deploy Go App to Kubernetes ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Create Helm chart for your Go application
- [ ] Deploy to minikube or EKS
- [ ] Run migrations as a Kubernetes Job
- [ ] Configure health checks for the Go app
- [ ] Test the full stack: Go API → PostgreSQL

#### Resources
- [Kubernetes Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

#### Proof
- Go app running in Kubernetes
- Migration job completed successfully
- Health check endpoints responding

#### Reflection
**Wins:**  
**Challenges:**  
**Next Month Focus:**  

---

## 📅 Month 6 – CI/CD + Automation + Portfolio Polish
**Theme:** Production pipelines, automation, and portfolio presentation

---

### Week 21 – GitHub Actions for Docker ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Create GitHub Actions workflow for Docker builds
- [ ] Push images to Docker Hub or ECR automatically
- [ ] Add automated testing (linting, unit tests)
- [ ] Implement branch protection and PR workflows
- [ ] Test the full CI pipeline

#### Resources
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Docker Build Push Action](https://github.com/docker/build-push-action)
- [GitHub Actions Best Practices](https://docs.github.com/en/actions/learn-github-actions/best-practices-for-using-github-actions)

#### Proof
- Successful GitHub Actions workflow runs
- Docker images in registry with version tags
- Screenshot of passing CI checks

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 22 – Terraform + Helm CD Pipeline ✅/🕐/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Automate Terraform apply/destroy in GitHub Actions
- [ ] Deploy Helm charts automatically on merge to main
- [ ] Add manual approval steps for production
- [ ] Store secrets in GitHub Secrets or AWS Secrets Manager
- [ ] Test the full deployment pipeline

#### Resources
- [Terraform CLI in Actions](https://developer.hashicorp.com/terraform/tutorials/automation/github-actions)
- [Helm GitHub Action](https://github.com/marketplace/actions/helm-deploy)

#### Proof
- Automated infrastructure deployment
- Helm release updated automatically
- Pipeline logs showing successful deployment

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 23 – Database Automation + Backups ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Automate database migrations in CI/CD
- [ ] Set up automated PostgreSQL backups to S3
- [ ] Create restore procedure and test it
- [ ] Add monitoring/alerting for backup failures
- [ ] Document the backup and recovery process

#### Resources
- [pg_dump Backups](https://www.postgresql.org/docs/current/app-pgdump.html)
- [AWS RDS Automated Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
- [S3 Lifecycle Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

#### Proof
- Backup files visible in S3
- Successful restore test
- Automated backup schedule configured

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 24 – Portfolio Polish + Documentation ✅/🕐/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Polish all README files across projects
- [ ] Create comprehensive architecture diagrams
- [ ] Add badges (build status, coverage, etc.)
- [ ] Write a project overview/case study document
- [ ] Prepare LinkedIn post about your learning journey
- [ ] Optional: Write blog posts or record demo videos

#### Resources
- [Shields.io for Badges](https://shields.io/)
- [Mermaid for Diagrams](https://mermaid.js.org/)
- [Technical Writing Best Practices](https://developers.google.com/tech-writing)

#### Proof
- GitHub profile with polished projects
- LinkedIn post published
- Professional README files with diagrams

#### Reflection
**Wins:**  
**Challenges:**  
**What's Next:**

---

## 🎯 After Month 6 – Continue Learning

Your learning doesn't stop here. Consider these next steps:
- **CKA Certification Prep** (April 2026 target) - Structured study for Certified Kubernetes Administrator
- **AWS Solutions Architect Certification** - After Terraform mastery
- **Advanced Topics:** Prometheus/Grafana monitoring, ArgoCD/Flux GitOps, Service Mesh (Istio/Linkerd)
- **HashiCorp Vault** for secrets management
- **Advanced Kubernetes:** Operators, Custom Resources, Multi-cluster management

---

## 🏆 Capstone Project
**Cloud-Native Application Platform**  

A production-ready system demonstrating:
- Python and Go microservices
- PostgreSQL with automated migrations
- Containerized with Docker, deployed to AWS EKS
- Infrastructure provisioned with Terraform
- CI/CD pipeline with GitHub Actions
- Automated backups and monitoring
- Complete documentation and architecture diagrams

This portfolio demonstrates the skills required for senior infrastructure/DevOps roles.

---

**Progress Tracking:** Mark each week ✅ complete, 🕐 in progress, or ❌ blocked.  
**Portfolio Focus:** Every project should have screenshots, diagrams, and thorough documentation.  
**Interview Ready:** By month 6, you'll have 4-5 production-quality projects to discuss in technical interviews.
