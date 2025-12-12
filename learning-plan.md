# 🧭 DevOps Career Transition Plan (6 Months)
**Goal:** Move into a Senior DevOps/Infrastructure Engineer role mastering Docker, Kubernetes, Terraform, Python, Go, and PostgreSQL  
**Pace:** Standard (10–12 hrs/week)  
**Cloud:** AWS Free Tier  
**Languages:** Python-first, Go later  
**Starting Point:** Docker fundamentals complete, now building multi-container applications

---

## 📅 Month 1 – Python + Multi-Container Applications
**Theme:** Python refresher + Docker Compose production patterns + PostgreSQL  
**Note:** Month 1 extended to 5 weeks to include real-world migration project

---

### Week 1 – Python Environment + Simple API ✅
Planned hours: 10 | Actual: 10

#### Tasks
- [x] Set up Python 3.12 + Poetry/venv
- [x] Review Python fundamentals: dicts, loops, list comprehensions, JSON
- [x] Write a simple Flask REST API with 3-4 endpoints (GET, POST)
- [x] Practice `requests` library for API calls
- [x] Containerize the Flask app (single-stage Dockerfile)

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
    - How to build a docker image (single and multi-stage)
    - That in term of isolation, it makes sense to use venv even in a docker image
    - Basic Flask routing
    - How to process POST/PUT data in flask
    - How to issue simple http requests using the Python requests module

**What broke:**
    - In the flask app, I was initially trying to pass post data as URL variables.
    - When building a docker image for a dev flask app, I need to designate `--host=0.0.0.0` in order for the app to be accessible from outside the container
    - Copied app.py to the wrong path in the Dockerfile a copy of times (COPY app.py /app)

**What I'll improve next week:**
    - Slow down with documentation - accept that I need time to read and experiment
    - When docs feel overwhelming, focus on quickstart/examples first, then dive deeper only for what I specifically need
    - Run small experiments to test understanding rather than trying to absorb everything at once
    - Continue rebuilding Python fluency through practice

**Key commands/patterns to remember:**
    - Multi-stage: COPY --from=builder /app/.venv app/.venv
    - Flask in docker needs: --host=0.0.0.0
    - Python isolated mode: python -I

---

### Week 2 – Docker Compose + PostgreSQL Integration ✅
Planned hours: 12 | Actual: 13

#### Tasks
- [x] Install PostgreSQL locally and practice basic queries
- [x] Create `docker-compose.yml` for Flask + Postgres
- [x] Add persistent volume for Postgres data
- [X] Store credentials in `.env` file (use python-dotenv)
- [X] Connect Flask to Postgres using psycopg2 or SQLAlchemy
- [x] Implement basic CRUD endpoints (Create, Read, Update, Delete)

#### Resources
- [PostgreSQL psql Basics](https://www.postgresql.org/docs/current/app-psql.html)
- [Docker Compose](https://docs.docker.com/compose/)
- [psycopg Docs](https://www.psycopg.org/psycopg3/docs/) or [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)

#### Proof of Completion
- `docker-compose.yml` with Flask + Postgres + volume
- JSON API responses showing data from database
- Data persists after `docker compose down/up`

#### Reflection
**What I learned:**  
- Connected Flask to PostgreSQL using psycopg3 with connection pooling for production-ready database access. 
- Learned PostgreSQL permission model (database vs schema privileges - even with GRANT ALL on database, still need CREATE on schema). 
- Discovered RETURNING keyword for getting feedback from INSERT/UPDATE/DELETE operations. 
- Implemented proper REST API status codes (200, 201, 400, 404). Practiced CRUD operations via curl. 
- Automated database initialization with init.sql in Docker's entrypoint directory. 
- Worked with PostgreSQL arrays (INTEGER[]) and custom ENUM types. 
- Deployed with Granian WSGI server instead of Flask's development server.

**What broke:**  
- Missing psycopg[binary] in requirements.txt caused "no pq wrapper available" errors in Docker. 
- Hit permission denied creating types/tables until I granted CREATE ON SCHEMA public. 
- Docker Compose initially failed because I forgot env_file configuration. 
- Granian defaulted to RSGI mode instead of WSGI (needed --interface wsgi flag). 
- Volume mount path confusion between /var/lib/postgres and /var/lib/postgresql.

**What I'll improve next week:**  
- Start with brief review of prior week's concepts before adding new complexity. 
- Continue using small test exercises to isolate learning (worked extremely well this week). 
- When tools feel abstract, do things manually first to understand what's actually happening underneath. 
- Break down complex integrations into smaller steps when feeling muddled.

**Key commands/patterns to remember:**  
- Connection pooling: `with pool.connection() as conn:`
- PostgreSQL arrays: `'{80, 443}'` in SQL, `[80, 443]` in Python/JSON
- RETURNING clause: `INSERT ... RETURNING id, name`
- Volume mount: `app-db:/var/lib/postgresql` (changed in PG 18+)
- Granian production server: `granian --interface wsgi --host 0.0.0.0 app:app`
- Docker Compose: `docker compose up -d` / `docker compose down`

**Additional Learning: Dynamic SQL with PATCH endpoints**

Implemented a PATCH endpoint requiring dynamic query construction with `psycopg.sql` module:
```python
# Build SET clauses for each field to update
set_clauses = []
values = []
for key, value in update_data.items():
    set_clauses.append(sql.SQL("{} = %s").format(sql.Identifier(key)))
    values.append(value)

# Join into single SQL composable object
fields = sql.SQL(', ').join(set_clauses)

# Insert into query template
query = sql.SQL("UPDATE containers SET {} WHERE id = %s").format(fields)

# Execute with unpacked values
cur.execute(query, (*values, id))
```

**Key insight:** `sql.SQL(', ').join()` is a method of the SQL object, not Python's string join. This creates a single composable SQL object from a list of SQL fragments.

**Why this matters:** Dynamic SQL construction is essential when you don't know which fields will be updated ahead of time - common pattern for PATCH operations and dynamic WHERE clauses.

---

### Week 3 – Production-Ready Multi-Container Stack ✅
Planned hours: 12 | Actual: 12

**Theme:** Production patterns + reinforcing dynamic SQL from Week 2 PATCH work

---

#### Phase 1: Health Checks & Monitoring
**Focus:** Build a production health endpoint, then add Docker healthchecks

**Tasks:**
- [x] Create `/health` endpoint in Flask with multiple check types:
  - App liveness check
  - Database connection check
  - Database response time check
- [x] Add dynamic query parameter support: `GET /health?checks=db,app`
  - Reinforces PATCH patterns: build response dict dynamically based on params
  - Practice the `for key, value in items()` pattern from Week 2
- [x] Test health endpoint with curl (different param combinations)
- [x] Add HEALTHCHECK directive to Flask Dockerfile
- [x] Add healthcheck to compose.yml for both Flask and Postgres
- [x] Observe health status with `docker compose ps`

**Resources:**
- [Compose Healthcheck](https://docs.docker.com/compose/compose-file/05-services/#healthcheck)
- [Dockerfile HEALTHCHECK](https://docs.docker.com/engine/reference/builder/#healthcheck)
- Your Week 2 PATCH endpoint code (similar dynamic pattern)

---

#### Phase 2: Resource Management & Restart Policies

**Tasks:**
- [x] Add resource limits to compose.yml (memory, CPU) for both services
- [x] Add restart policies (restart: unless-stopped)
- [x] Test resource constraints work as expected
- [x] Document resource allocation decisions

**Resources:**
- [Docker Resource Constraints](https://docs.docker.com/config/containers/resource_constraints/)
- [Compose Restart Policies](https://docs.docker.com/compose/compose-file/05-services/#restart)

---

#### Phase 3: Production Patterns & Failure Testing

**Tasks:**
- [x] Add pgAdmin as third service in compose.yml
- [x] Configure proper logging (JSON format for Flask)
- [x] Test failure scenarios:
  - Kill Postgres container, watch Flask health endpoint respond
  - Watch Docker restart failed containers
  - Verify pgAdmin reconnects after failures
- [x] Document failure recovery behavior

**Resources:**
- [pgAdmin Docker](https://hub.docker.com/r/dpage/pgadmin4)
- [Python JSON Logging](https://docs.python.org/3/library/logging.html#logging.Formatter)

---

#### Proof of Completion
- Working `/health` endpoint with dynamic check selection
- Screenshot of pgAdmin connected to database
- `docker compose ps` showing health status for all services
- Logs showing graceful handling of database failures and recovery
- Documentation of failure scenarios and recovery behavior

#### Reflection
**What I learned:**
- **Python logging architecture** - Learned how logging actually works: Logger (creates messages) + Handler (where they go) + Formatter (what they look like). Implemented JSON logging with defensive programming to handle missing data gracefully.

- **Production Docker patterns** - Added Docker HEALTHCHECK directives, restart policies (unless-stopped for production services that survive reboots), and resource limits based on actual container usage.

- **Health endpoint design** - Built `/health` endpoint with dynamic query parameters using sets to filter checks. Used dictionary mapping (`check_functions`) to call different check functions dynamically.

- **Defensive programming** - Learned to test edge cases and handle missing data (like when `?checks=app` is requested but code assumes `db` exists). Used try/except for graceful error handling in database checks.

- **Python skills refreshed** - Worked with sets for intersection logic, gathered timing information with `time.time()`, learned about pip-tools for dependency management.

- **Learning approach validated** - When overwhelmed by logging complexity, stepped back to create isolated exercise (`/03-learn-logging/`), learned concepts piece by piece, then applied to real project. This pattern works well for me. 

**What broke:**

- My healthchecks weren't working originally because I wasn't making sure that I was getting a 0 or 1 for exit codes
- I'd forgotten to send server responses so the healthchecks were not reliable
- I assumed there would always be db output for the logs and that caused the program to crash when I tried to log non-existent data
- I mistakenly thought that a restart policy of on-failure would still restart on a reboot
- Created a logger without a handler in the isolated logging exercise and got no output - learned that Logger creates messages but needs a Handler to actually send them somewhere
- Initially tried to use `asctime` in JSON logs but it was missing timestamp and log level because I didn't specify the format string for JsonFormatter  

**How PATCH patterns applied to health checks:**

Week 2's PATCH endpoint taught me to build things dynamically based on what data is present - iterating through `update_data.items()` to construct SQL queries. Applied the same pattern in Week 3's health checks: iterate through requested checks and build the response dictionary dynamically. The core pattern is the same: `for key, value in items()` to process whatever data exists rather than assuming a fixed structure.

**Next actions:**

- Complete Week 3 reflection and push to GitHub
- Start Week 4: Lambda → Docker migration project  
- Apply pip-tools for dependency management from the start
- Continue using defensive programming patterns (check if data exists before accessing)
- Use isolated exercises when encountering new complex concepts

---

### Week 4 – Events Display Docker Migration ✅
Planned hours: 12 | Actual: 12 

**Project Goal:** Migrate existing AWS Lambda application to containerized architecture, demonstrating cost optimization and reduced operational complexity.

#### Tasks
- [x] Set up project structure with pip-tools (requirements.in)
- [x] Create Dockerfile for events generator
- [x] Create docker-compose.yml with two services:
  - Generator container (Python app)
  - Uploader container (amazon/aws-cli)
- [x] Configure shared volume between containers
- [x] Set up .env file for AWS credentials and API tokens
- [x] Implement service dependencies (uploader waits for generator)
- [x] Apply production patterns from Week 3:
  - Resource limits
  - Proper logging
  - Restart policies
- [x] Test locally: generate → upload to S3
- [x] Deploy to Proxmox with scheduled execution (cron or systemd timer)

#### Resources
- [Docker Compose depends_on](https://docs.docker.com/compose/compose-file/05-services/#depends_on)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Amazon AWS CLI Docker Image](https://hub.docker.com/r/amazon/aws-cli)
- [pip-tools Documentation](https://pip-tools.readthedocs.io/)

#### Proof of Completion
- docker-compose.yml with generator and uploader services
- requirements.in showing only direct dependencies
- HTML file successfully generated and uploaded to S3
- Chromestick displaying updated content
- Screenshot of docker compose ps showing both containers

#### Portfolio Narrative
**"Lambda to Docker Migration"**: Demonstrates:
- Reduced operational complexity (no layer management, easier debugging)
- Improved developer experience (local testing, clearer workflows)
- Infrastructure portability (runs anywhere Docker runs)
- Understanding of when to use (and not use) serverless
- *Note: While not a cost factor at this scale (free tier), the migration pattern is valuable for larger workloads*
- *Future enhancement: Can be deployed as Kubernetes CronJob in Month 3-4*

#### Reflection

**What I learned:**  
- Multi-container orchestration with `depends_on: service_completed_successfully` to create sequential pipelines. 
- Migrated from python-dotenv to os.environ for containerized environments, discovering that quotes in .env files are literal when Docker reads them (not stripped like in shell exports). 
- Implemented non-root containers with dynamic UID/GID mapping using `user: ${HOST_UID:-1000}:${HOST_GID:-1000}` for portable bind mount permissions. 
- Set up IAM users with restricted least-privilege policies for S3 and CloudFront access. 
- Created systemd service (oneshot) and timer files for scheduled execution with proper dependencies (After=network-online.target docker.service). 
- Learned Mermaid syntax for architecture diagrams and the .env.example convention for portfolio projects. 
- Understood operational trade-offs between bind mounts (direct access for debugging) vs named volumes (Docker-managed abstraction) for batch jobs.

**What broke:**  
- Environment variable quote handling - .env file had quotes around values which Docker passed literally to the OAuth API, causing 400 errors. Fixed by removing quotes from .env values. 
- UID permission mismatches on bind mounts between laptop (UID 1001) and hardcoded Dockerfile (UID 1000), resolved with runtime user mapping in compose. 
- AWS CLI syntax confusion - used `--dry-run` instead of `--dryrun` for s3 sync command. 
- Typo in exception handler: `RequestExeception` instead of `RequestException` - discovered by testing with bad credentials. 
- Initially structured Mermaid diagram with too many action nodes instead of focusing on components and data flow.

**How this reinforced Week 3 patterns:**  
- Applied logging patterns from Week 3 but simplified for batch jobs (structured logging without JSON, since no need for centralized aggregation). 
- Used multi-stage Dockerfile pattern with .venv isolation. Applied pip-tools from Week 3 for dependency management (requirements.in → requirements.txt).
- Continued defensive programming with try/except blocks and proper error handling. 
- Made operational decisions about resource limits (chose not to add them for 5-second batch jobs, unlike Week 3's long-running services). 
- Reinforced the pattern of breaking down complex problems - when Mermaid felt overwhelming, stepped back to understand components vs actions. 
- Applied the "do things manually first" pattern by testing with --dryrun before real S3 uploads.

---

### Week 5 – Documentation + Architecture Diagrams ✅
Planned hours: 10 | Actual: 8  

**Focus:** Document BOTH the Flask+PostgreSQL stack AND the Events Display project

#### Tasks
- [x] **Flask+PostgreSQL Project:**
  - Write comprehensive README.md with setup instructions
  - Create architecture diagram (Mermaid or draw.io)
  - Document API endpoints (consider using Swagger/OpenAPI)
  - Add troubleshooting section
- [x] **Events Display Project:**
  - Write README.md explaining Lambda → Docker migration
  - Document the multi-container architecture
  - Explain scheduling approach (cron/systemd timer)
  - Include cost comparison (Lambda vs containerized)
- [x] Push both projects to GitHub with proper .gitignore
- [x] Write LinkedIn post about both projects and learning journey


#### Resources
- [Mermaid Diagrams for Markdown](https://mermaid.js.org/)
- [Flask-RESTX for API docs](https://flask-restx.readthedocs.io/)
- [README Best Practices](https://github.com/matiassingers/awesome-readme)
- [Technical Writing Best Practices](https://developers.google.com/tech-writing)

#### Proof of Completion
- Two GitHub repos with polished READMEs
- Architecture diagrams for both projects

#### Reflection
**Wins:**  
- Created comprehensive documentation for both Flask+PostgreSQL and Events Display projects with professional README files
- Learned Mermaid diagram syntax and successfully created architecture diagrams showing component relationships and data flows
- Wrote honest migration story for Events Display explaining operational complexity reduction (not cost) as primary motivation
- Established .env.example pattern for portfolio projects to document required environment variables
- Organized completed work into proper project structure under `projects/month-01-containers/`

**Challenges:**  
- Initial Mermaid diagrams had too many action nodes instead of focusing on components and data flow
- Needed to reframe Lambda migration narrative from "cost savings" to accurate "operational complexity reduction" 
- Finding the right level of detail for documentation (enough to be useful, not so much it becomes overwhelming)

**Key differences between the two projects:**  
- **Flask+PostgreSQL**: Long-running services requiring health checks, restart policies, resource limits, and connection pooling
- **Events Display**: Batch job pipeline with sequential container execution using `depends_on: service_completed_successfully`
- Flask project emphasized production patterns for always-on services; Events Display focused on orchestration and scheduling
- Different logging strategies: JSON structured logging for long-running services vs. simpler logging for short-lived batch jobs

**Next Month Focus:**  
Moving into Terraform and AWS infrastructure.

---

## 📅 Month 2 – Terraform + AWS Cloud Infrastructure
**Theme:** Infrastructure as Code + Cloud Postgres (RDS)

---

### Week 6 – Terraform Fundamentals ✅
Planned hours: 10 | Actual: 10 

#### Tasks
- [x] Install Terraform + AWS CLI
- [x] Create IAM user with appropriate permissions
- [x] Learn Terraform basics: providers, resources, variables, outputs
- [x] Write `main.tf` to provision a simple EC2 instance
- [x] Practice `terraform init`, `plan`, `apply`, `destroy`
- [x] Output the instance public IP

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
- Terraform configuration structure: terraform block (required providers), provider block (global settings like region), variable block (import variables/sensitive data), data block (lookup existing resources), resource block (create infrastructure), output block (return information)
- State management: terraform.tfstate tracks what Terraform has created and compares desired state (main.tf) to actual state to determine what changes to make
- Reference syntax: Resources reference each other using `resource_type.local_name.attribute` pattern (e.g., `aws_security_group.web_sg.id`)
- Security group architecture: Separate security groups for different concerns (base for egress, admin for SSH, web for HTTP/HTTPS) can be combined on instances for modular, reusable infrastructure
- Infrastructure layering: Shared infrastructure (security groups, VPCs) should be managed in separate Terraform projects from application resources to avoid dependencies

**What broke:**
- Couldn't SSH initially because I hadn't created ingress rules in the security group and attached it to the instance
- apt update hung because there was no egress rule allowing outbound traffic
- Used `security_groups` attribute initially which forces instance replacement; switching to `vpc_security_group_ids` allows in-place updates
- Looked in data source documentation when I needed resource documentation (wrong section of the Terraform provider docs)

**What I'll improve next week:**
- Continue using repetition to build muscle memory - typing configurations multiple times helped concepts click
- Once syntax becomes familiar, freed up mental space to explore infrastructure design patterns
- Get more comfortable navigating Terraform documentation (distinguishing between data sources and resources)
- Expect that Week 7 will also require building things multiple times before they stick

**Key commands/patterns to remember:**
- `terraform fmt` - format .tf files automatically
- `terraform validate` - check configuration syntax
- `terraform init` - download and set up providers
- `terraform plan` - preview what changes will be made
- `terraform show` - display current state
- `terraform apply` - create/update infrastructure
- `terraform destroy` - tear down infrastructure
- Reference syntax: `resource_type.local_name.attribute` (e.g., `data.aws_ami.debian13.id`)
- Heredoc for multi-line strings: `<<-EOF ... EOF` (used in user_data)
- Workflow pattern: init → plan → apply → destroy

---

### Week 7 – RDS PostgreSQL + Security Groups ✅/🕐/❌
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

### Week 8 – Deploy Flask App to EC2 + Connect to RDS ✅/🕐/❌
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

### Week 9 – Terraform Best Practices + Remote State ✅/🕐/❌
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

### Week 10 – Kubernetes Core Concepts ✅/🕐/❌
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

### Week 11 – Deploy Flask App to Kubernetes ✅/🕐/❌
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

### Week 12 – StatefulSets + Persistent Storage ✅/🕐/❌
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

### Week 13 – Introduction to Helm ✅/🕐/❌
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

### Week 14-15 – EKS Cluster with Terraform ✅/🕐/❌
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

### Week 16 – Deploy Full Stack to EKS ✅/🕐/❌
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

### Week 17 – Monitoring + Cost Management ✅/🕐/❌
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

### Week 18 – Go Fundamentals ✅/🕐/❌
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

### Week 19 – Go + PostgreSQL Integration ✅/🕐/❌
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

### Week 20 – Database Migrations ✅/🕐/❌
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

### Week 21 – Deploy Go App to Kubernetes ✅/🕐/❌
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

### Week 22 – GitHub Actions for Docker ✅/🕐/❌
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

### Week 23 – Terraform + Helm CD Pipeline ✅/🕐/❌
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

### Week 24 – Database Automation + Backups ✅/🕐/❌
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

### Week 25 – Portfolio Polish + Documentation ✅/🕐/❌
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
**Interview Ready:** By month 6, you'll have 5-6 production-quality projects to discuss in technical interviews, including a real-world Lambda to containerized architecture migration.
