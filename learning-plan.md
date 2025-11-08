# 🧭 DevOps Career Transition Plan (6 Months)
**Goal:** Move into a $140K+ DevOps role mastering Docker, Kubernetes, Terraform, Python, Go, and PostgreSQL  
**Pace:** Standard (10–12 hrs/week)  
**Cloud:** AWS Free Tier  
**Languages:** Python-first, Go later  

---

## 📅 Month 1 — Docker, Python, and Postgres Foundations
**Theme:** Containers + Python API + real database

---

### Week 1 — Docker Basics + Python Refresh ✅/🕒/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Install Docker + Docker Compose  
- [ ] Learn `docker run`, `docker ps`, `docker exec`, `docker logs`  
- [ ] Install Python 3.12 + Poetry or venv  
- [ ] Review Python dicts, loops, JSON parsing  
- [ ] Install PostgreSQL locally (`psql`) and run simple queries  

#### Resources
- [Docker Get Started](https://docs.docker.com/get-started/overview/)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [PostgreSQL psql Basics](https://www.postgresql.org/docs/current/app-psql.html)

#### Proof of Completion
- Screenshot: `docker run hello-world`
- Output of `psql -c "SELECT version();"`
- Git commit: setup folder for first Python script

#### Reflection
**What I learned:**  
**What broke:**  
**What I’ll improve next week:**  

---

### Week 2 — Writing & Containerizing a Python App ✅/🕒/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Write a Python script that outputs system info (CPU, RAM, uptime)  
- [ ] Create Dockerfile (`FROM python:3.12-slim`)  
- [ ] Run container, verify script output  
- [ ] Push image to Docker Hub  
- [ ] Practice using `requests` to call an API  

#### Resources
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Hub Docs](https://docs.docker.com/docker-hub/)
- [Python requests Library](https://requests.readthedocs.io/en/latest/)

#### Proof of Completion
- `docker images` screenshot  
- Docker Hub link  
- Commit showing Dockerfile + requirements.txt  

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 3 — Docker Compose + PostgreSQL ✅/🕒/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Create `docker-compose.yml` for Python API + Postgres + pgAdmin  
- [ ] Add persistent volume for Postgres data  
- [ ] Store credentials in `.env` file  
- [ ] Connect Python app via psycopg2  
- [ ] Test insert/select query from API endpoint  

#### Resources
- [Docker Compose](https://docs.docker.com/compose/)
- [pgAdmin Docker](https://hub.docker.com/r/dpage/pgadmin4)
- [psycopg2 Docs](https://www.psycopg.org/docs/)

#### Proof of Completion
- Screenshot of pgAdmin connected  
- JSON API response from Python app  
- Data persists after `docker compose down/up`  

#### Reflection
**What I learned:**  
**What broke:**  
**Next actions:**  

---

### Week 4 — Cleanup + Docs ✅/🕒/❌
Planned hours: 8 | Actual: ___  

#### Tasks
- [ ] Add Docker labels, resource limits, healthcheck  
- [ ] Test logs with `docker compose logs`  
- [ ] Write README.md with architecture diagram  
- [ ] Push final repo to GitHub  

#### Resources
- [Compose Healthcheck](https://docs.docker.com/compose/compose-file/05-services/#healthcheck)
- [Mermaid Diagrams for Markdown](https://mermaid.js.org/)

#### Proof of Completion
- GitHub repo link  
- Screenshot of running containers  
- Diagram showing API ↔ Postgres network  

#### Reflection
**Wins:**  
**Challenges:**  
**Next Month Focus:**  

---

## 📅 Month 2 — Terraform + Cloud Postgres
**Theme:** Infrastructure as Code + AWS RDS  

---

### Week 5 — Terraform Setup ✅/🕒/❌
Planned hours: 10 | Actual: ___  

#### Tasks
- [ ] Install Terraform + AWS CLI  
- [ ] Create IAM user + keys  
- [ ] Terraform EC2 provisioning (main.tf)  
- [ ] Output instance IP  

#### Resources
- [Terraform AWS Tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)
- [AWS CLI Setup](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

#### Proof
- `terraform apply` output  
- SSH connection to instance  
- Screenshot of EC2 console  

#### Reflection
...

---

### Week 6–8 (Condensed) — EC2 + RDS Integration ✅/🕒/❌
Planned hours: 12 | Actual: ___  

#### Tasks
- [ ] Deploy Postgres on RDS using Terraform  
- [ ] Move Python API to use RDS endpoint  
- [ ] Create security group rules  
- [ ] Add Terraform remote state (S3)  
- [ ] Document infra diagram  

#### Resources
- [AWS RDS Terraform Resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/db_instance)
- [Terraform Variables](https://developer.hashicorp.com/terraform/language/values/variables)

#### Proof
- Screenshot of AWS RDS dashboard  
- Connection test from app  
- GitHub commit links  

#### Reflection
...

---

## 📅 Month 3 — Kubernetes + Stateful Postgres
**Theme:** Deploy your app on K8s  

---

### Week 9–12 — From Minikube to Helm ✅/🕒/❌
Planned hours: 10–12 | Actual: ___  

#### Tasks
- [ ] Install `kubectl`, `minikube`, and `helm`  
- [ ] Deploy Postgres StatefulSet + PVC  
- [ ] Deploy Python app using Deployment + Service + Ingress  
- [ ] Replace manual YAML with Bitnami Postgres Helm chart  
- [ ] Add ConfigMaps + Secrets  
- [ ] Validate persistence after pod restart  

#### Resources
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [Bitnami PostgreSQL Chart](https://artifacthub.io/packages/helm/bitnami/postgresql)
- [Helm Quickstart](https://helm.sh/docs/intro/quickstart/)

#### Proof
- Screenshot: `kubectl get pods,pvc,svc`
- Helm release output  
- Diagram of K8s namespace

#### Reflection
...

---

## 📅 Month 4 — Terraform + EKS + RDS Integration
**Theme:** End-to-end IaC and deployment pipeline  

---

### Week 13–16 — Cloud-Native Infrastructure ✅/🕒/❌
Planned hours: 10–12 | Actual: ___  

#### Tasks
- [ ] Provision EKS cluster via Terraform  
- [ ] Add RDS Postgres instance  
- [ ] Deploy Helm chart automatically  
- [ ] Validate connection + security groups  
- [ ] Automate teardown (`terraform destroy`)  

#### Resources
- [Terraform EKS Module](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest)
- [AWS EKS Setup Docs](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)

#### Proof
- EKS + RDS running in AWS Console  
- Helm deploy logs  
- Screenshot of web app online  

#### Reflection
...

---

## 📅 Month 5 — Go Fundamentals + DB Migrations
**Theme:** Add a compiled language + schema automation  

---

### Week 17–20 — Go + Postgres ✅/🕒/❌
Planned hours: 10–12 | Actual: ___  

#### Tasks
- [ ] Complete Tour of Go  
- [ ] Build CLI to query Postgres with `pgx`  
- [ ] Implement migrations with `golang-migrate` or `dbmate`  
- [ ] Build Go REST API  
- [ ] Containerize and deploy via Helm  

#### Resources
- [Tour of Go](https://go.dev/tour/)
- [pgx Postgres Driver](https://github.com/jackc/pgx)
- [golang-migrate](https://github.com/golang-migrate/migrate)

#### Proof
- CLI demo screenshot  
- API response  
- Helm release output  

#### Reflection
...

---

## 📅 Month 6 — CI/CD + Database Automation
**Theme:** Automation, backups, monitoring  

---

### Week 21–24 — Pipelines & Portfolio ✅/🕒/❌
Planned hours: 10–12 | Actual: ___  

#### Tasks
- [ ] Create GitHub Actions workflow  
- [ ] Automate Docker builds + Terraform + Helm deploy  
- [ ] Add DB migrations + S3 backups  
- [ ] Add health check job (Go or Python)  
- [ ] Polish READMEs and diagrams  
- [ ] Write LinkedIn update / portfolio blog post  

#### Resources
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Terraform CLI Integration](https://developer.hashicorp.com/terraform/cli)
- [pg_dump Backups](https://www.postgresql.org/docs/current/app-pgdump.html)

#### Proof
- Successful GitHub Actions run  
- S3 backup visible  
- Repo badges + screenshots  

#### Reflection
**Wins:**  
**Challenges:**  
**Next Goals (After Month 6):**
- Prometheus/Grafana monitoring  
- HashiCorp Vault for secrets  
- ArgoCD or Flux GitOps pipeline  

---

# 🏁 Capstone Project
> **Cloud-Native Shift Board**  
> Python + Go apps with PostgreSQL backend, containerized via Docker, deployed to AWS EKS via Terraform, managed by CI/CD pipeline with automated migrations and S3 backups.

---

**Tip:** Each “Proof of Completion” item = one GitHub screenshot or commit link.  
By the end of 6 months, you’ll have 4–5 polished projects and a DevOps-ready portfolio.
