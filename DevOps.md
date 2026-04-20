# 🐳 DevOps Foundations — Ship the MERN App
### A Hands-On DevOps Course for BCA Year 3 Students · 40 Hours

> **Instructor:** Satyavs · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)
> **The Thread:** Every session operates on the MERN app students built in Year 2.

---

## Why 40 Hours?

DevOps tools are unforgiving for beginners. A misconfigured Dockerfile, a wrong port
in Nginx, a missing environment variable in Compose — any of these silently breaks
the app with no obvious error. Extra time is not padding. It is:

- Practice sessions where students work independently without the instructor guiding every step
- Dedicated debug sessions where common mistakes are walked through deliberately
- Buffer for topics that trip beginners the most: Linux permissions, Docker networking, YAML syntax
- Consolidation sessions that connect what was just learned to the full pipeline picture

Every extra session has a specific purpose. Nothing is repeated for its own sake.

---

## The BCA Trilogy

```
Year 1 — Core Python          →  Learn to think like a programmer       (36 hrs)
Year 2 — Full-Stack MERN      →  Learn to build a working application    (40 hrs)
Year 3 — DevOps Foundations   →  Learn to operate and ship that app      (40 hrs)
```

> Each course hands off directly to the next. Students arrive in Year 3 with a
> working MERN app (MySQL + Express + React + Node). This course takes it
> from localhost to a containerised, automated, running deployment.

---

## Course at a Glance

| | |
|---|---|
| **Total Duration** | 40 hours · 20 sessions × 2 hours |
| **The Project** | MERN app from Year 2 — containerised, pipelined, shipped |
| **Target Audience** | BCA Year 3 — has built the MERN app, basic command line comfort |
| **Environment** | Linux (WSL2 on Windows / Ubuntu) · VS Code · Docker Desktop |
| **What NOT covered** | AWS · Kubernetes · Monitoring (Prometheus/Grafana) |
| **Those topics belong in** | Cloud Engineering / Platform Engineering — Year 4 or elective |

---

## How the Extra 10 Hours Are Used

| Phase | 30-hr plan | 40-hr plan | Extra sessions used for |
|---|---|---|---|
| Linux & Shell | 3 sessions · 6 hrs | 5 sessions · 10 hrs | +1 Permissions deep dive · +1 Practice lab |
| Git & GitHub | 2 sessions · 4 hrs | 3 sessions · 6 hrs | +1 Real team collaboration with live conflicts |
| Docker | 4 sessions · 8 hrs | 5 sessions · 10 hrs | +1 Docker networking & volumes deep dive |
| CI/CD | 3 sessions · 6 hrs | 4 sessions · 8 hrs | +1 Pipeline failure lab — read logs, fix pipelines |
| IaC | 2 sessions · 4 hrs | 2 sessions · 4 hrs | Same — already right depth for intro |
| Capstone | 1 session · 2 hrs | 1 session · 2 hrs | Same — now students arrive better prepared |
| **Total** | **15 sessions · 30 hrs** | **20 sessions · 40 hrs** | |

---

## The One Mental Model

```
Code  →  Git Push  →  GitHub Actions (CI/CD)
                             ↓
                      docker build + push
                             ↓
                   Ansible pulls + runs compose
                             ↓
              Docker Compose (Node + React + MySQL)
                             ↓
                    Nginx (port 80 · one URL)
                             ↑
                  Terraform defined the server
                  Ansible configured the server
```

> **Key teaching line:** DevOps is not a tool. It is the practice of making software
> delivery fast, repeatable, and reliable. Every tool in this course serves one
> of those three goals.

---

## Teaching Philosophy

1. **Problem before tool** — Every tool is introduced by the problem it solves. Students feel the pain first.
2. **The app is always running** — Every session ends with the MERN app in a better, more automated state.
3. **Break things intentionally** — Students deliberately break the pipeline to understand what each piece protects.
4. **Commands must be understood** — No copy-pasting without explanation. Every flag and config key is discussed.
5. **Localhost is the cloud** — We simulate production on local Linux VMs. The concepts transfer to any cloud provider.
6. **Struggle time is learning time** — The extra 10 hours exist so students hit walls, debug independently, and build real confidence.

### Session Structure (every 2 hours)
| Segment | Time | What happens |
|---|---|---|
| Problem statement | 10 min | What breaks without this tool? Students see the pain first. |
| Concept + diagram | 15 min | What the tool does and where it fits in the pipeline |
| Live demo | 45 min | Instructor runs commands, students watch and ask |
| Student hands-on | 30 min | Students replicate on their own machines |
| Recap + what's next | 10 min | Connect this session to the next one |

> **Practice / Lab sessions** run differently: 10 min recap → 90 min independent
> student work on a given challenge → 20 min group debug and review.

---

## Curriculum — Session by Session

---

### Phase 1 — Linux & Shell Scripting (Sessions 1–5 · 10 hrs)

> **Goal:** Students can navigate a Linux server, manage permissions, write shell scripts,
> and handle basic networking with genuine confidence — not just surface familiarity.
>
> **Why 5 sessions:** Linux permissions and process management trip up beginners more
> than any other topic. Rushing here means students spend the Docker and CI/CD phases
> debugging Linux problems they never properly understood. The practice lab (S5)
> is the most important session in this phase — it is where understanding becomes skill.

---

#### S1 — Linux Fundamentals for DevOps
**The problem:** "Our MERN app runs on your laptop. How do we run it on a server?"

| | |
|---|---|
| **Key concepts** | File system structure · `ls`, `cd`, `mkdir`, `rm`, `cp`, `mv` · Absolute vs relative paths · Hidden files · `cat`, `less`, `head`, `tail` · `man` pages · Where things live: `/etc`, `/var`, `/home`, `/usr` |
| **What gets done** | Set up WSL2 (Windows) or Ubuntu VM · Navigate the full file system · Find and read config files · Understand the Linux directory structure |
| **Key teaching line** | Linux is the operating system that runs the internet. If your app goes to production, it goes to Linux. |

---

#### S2 — Linux Permissions & User Management
**The problem:** "I ran a command and got 'Permission denied'. Why? Who decides what I can do?"

| | |
|---|---|
| **Key concepts** | File permissions: read/write/execute · `chmod` numeric and symbolic modes · `chown` · Users and groups · `sudo` and `su` · `whoami` · `adduser` · Package management: `apt install`, `apt update`, `apt upgrade` |
| **What gets done** | Change permissions on MERN project files · Create a new Linux user for the app · Install Node.js and MySQL on Linux manually using `apt` · Run the Node server as a non-root user |
| **Key teaching line** | Linux permissions are not obstacles — they are the security model that keeps servers safe. Understand them once, never be confused by them again. |

---

#### S3 — Shell Scripting & Process Management
**The problem:** "I have to type the same 10 commands every time I start the app. There has to be a better way."

| | |
|---|---|
| **Key concepts** | Bash scripting · Variables · `if` / `for` / `while` · `chmod +x` · `ps`, `kill`, `top` · `systemctl start/stop/enable` · `cron` basics · Environment variables · `.env` files · `export` |
| **What gets done** | Write a shell script that starts Node, checks if MySQL is running, and logs the result · Schedule it with `cron` to run on boot · Register Node as a `systemctl` service so it restarts automatically on crash |
| **Key teaching line** | A shell script is automation at its simplest. Every DevOps pipeline is ultimately a set of shell commands wired together. |

---

#### S4 — Networking Basics & SSH
**The problem:** "How does traffic actually reach my app? How do I access a remote server?"

| | |
|---|---|
| **Key concepts** | IP addresses and ports · `curl` · `netstat` / `ss` · `ping` · `ufw` firewall · SSH key generation (`ssh-keygen`) · `ssh` and `scp` · `~/.ssh/config` · `authorized_keys` |
| **What gets done** | Generate an SSH key pair · SSH into a second Linux VM or WSL instance · Copy the MERN project over `scp` · Run the app manually on the remote machine via SSH only — no desktop, no GUI |
| **Key teaching line** | A server is just a computer you access over SSH. Everything else is just tools running on top of that. |

---

#### S5 — Linux Practice Lab & Consolidation
**The problem:** "I followed every command in class but when I sit alone I do not know where to start."

| | |
|---|---|
| **Key concepts** | Consolidation of S1–S4 · Debugging common Linux errors · Reading error messages · `grep`, `find`, `wc`, pipe (`\|`) · `screen` or `tmux` basics · Writing a multi-function shell script from scratch |
| **What gets done** | Students independently complete a Linux challenge: set up a user, configure permissions, write a startup script, SSH into a peer's machine, verify the MERN app starts via the script. No instructor help for the first 60 minutes. Group debug in the last 30. |
| **Key teaching line** | Confidence on the command line does not come from watching — it comes from being stuck and finding your own way out. |

---

### Phase 2 — Git & GitHub for Teams (Sessions 6–8 · 6 hrs)

> **Goal:** Students use Git the way a development team does — branches, pull requests,
> protected branches, repository secrets, and real conflict resolution under pressure.
>
> **Why 3 sessions:** Merge conflicts and branch protection are the two things students
> consistently get wrong in internships. The extra session (S8) is a full team exercise
> with deliberate conflicts — the most valuable session in this phase.

---

#### S6 — Git Branching & Collaboration Workflow
**The problem:** "Two students edited the same file. Everything is broken. How do teams manage this?"

| | |
|---|---|
| **Key concepts** | `git branch` · `git switch` · `git merge` · Merge conflicts — reading and resolving · Pull Requests on GitHub · `.gitignore` for Node + React · `git log --oneline --graph` |
| **What gets done** | Fork the MERN repo · Create a feature branch · Make a change · Open a Pull Request · Review a peer's PR · Deliberately create and resolve a merge conflict |
| **Key teaching line** | Git is not a backup tool. It is a collaboration protocol. Branching is what makes teams work in parallel without destroying each other's work. |

---

#### S7 — GitHub Secrets, Branch Protection & Release Tags
**The problem:** "My `.env` file with the MySQL password is on GitHub. Anyone can see it."

| | |
|---|---|
| **Key concepts** | GitHub Secrets · Protected branches · Branch protection rules (require PR, require review) · Removing secrets from git history · `git tag` and releases · `README` badges |
| **What gets done** | Audit the MERN repo for leaked secrets · Remove `.env` from git history · Add GitHub Secrets for `DB_PASSWORD` and `JWT_SECRET` · Set branch protection on `main` — no direct pushes allowed · Tag `v1.0.0` |
| **Key teaching line** | Secrets in code is one of the most common and most costly security mistakes in industry. Fix it once, understand it forever. |

---

#### S8 — Team Git Workflow — Real Collaboration Exercise
**The problem:** "In class we push to our own repo. In a real team, three people push to the same repo simultaneously. What actually happens?"

| | |
|---|---|
| **Key concepts** | `git rebase` vs `git merge` — the difference and when to use each · `git stash` · `git cherry-pick` · Writing meaningful commit messages · Conventional commits (`feat:`, `fix:`, `chore:`) · Reviewing PRs properly |
| **What gets done** | Students split into pairs. Both make different changes to the MERN app on separate branches simultaneously. Both open PRs. They review each other's code, leave comments, request changes, and merge in sequence — resolving whatever conflicts arise naturally. |
| **Key teaching line** | The code review is where the team's knowledge lives. A PR without a proper review is a liability, not a delivery. |

---

### Phase 3 — Docker & Containerisation (Sessions 9–13 · 10 hrs)

> **Goal:** Students containerise all three MERN services and run them with Docker
> Compose. The extra session (S11) adds a dedicated Docker networking and volumes
> deep dive — the area where beginners break things most and understand least.
>
> **Why 5 sessions:** Docker networking is invisible until something breaks. When
> a container cannot reach another container, students with no mental model panic.
> One dedicated session on how Docker networks work prevents hours of confusion
> in the Compose and Nginx sessions that follow.

---

#### S9 — Docker Fundamentals
**The problem:** "It works on my machine but not on yours. How do we ship the environment, not just the code?"

| | |
|---|---|
| **Key concepts** | Container vs VM — what is actually different · Docker architecture: daemon, client, registry · `docker pull` · `docker run` · `docker ps` · `docker stop` · `docker rm` · `docker images` · Docker Hub · `docker exec -it` |
| **What gets done** | Pull and run official Node and MySQL images · Explore a running container filesystem with `docker exec` · Run the Node backend inside a container manually — no Dockerfile yet |
| **Key teaching line** | A container is a process with a boundary. It carries its own environment. "Works on my machine" stops being an excuse. |

---

#### S10 — Writing Dockerfiles
**The problem:** "The official Node image does not have our app in it. How do we create our own image?"

| | |
|---|---|
| **Key concepts** | `Dockerfile` syntax: `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD` · Layer caching and why order matters · `.dockerignore` · `docker build` and `docker tag` · Multi-stage builds: build stage → runtime stage |
| **What gets done** | Write `Dockerfile` for the Node/Express backend · Write `Dockerfile` for React (multi-stage: `npm run build` → Nginx serve) · Build both images · Run containers · Verify APIs respond |
| **Key teaching line** | A Dockerfile is a recipe. Docker follows it to bake an image. The image is the thing you ship — not the code. |

---

#### S11 — Docker Networking & Volumes Deep Dive
**The problem:** "My Node container starts. My MySQL container starts. But Node says it cannot connect to MySQL. Why?"

| | |
|---|---|
| **Key concepts** | Docker bridge networks · `docker network create` · Container DNS — containers find each other by name, not by IP · `docker network inspect` · Named volumes vs bind mounts · Volume persistence · `docker volume ls` and `docker volume inspect` |
| **What gets done** | Create a custom Docker network · Run Node and MySQL on that network · Node connects to MySQL using container name as hostname · Mount a named volume for MySQL data · Destroy and recreate MySQL container — verify data survived |
| **Key teaching line** | Containers talk to each other by name on a shared network. If they are on different networks, they are strangers. This is the most common Docker mistake beginners make. |

---

#### S12 — Docker Compose — Multi-Container Apps
**The problem:** "I have three containers to start separately, in the right order, with the right env vars. Every single time."

| | |
|---|---|
| **Key concepts** | `docker-compose.yml` structure · `services`, `networks`, `volumes` · `depends_on` · Environment variables in Compose · `docker compose up -d` / `down` / `logs` / `ps` · Rebuilding with `--build` · Health checks |
| **What gets done** | Write `docker-compose.yml` for all three MERN services · One command starts the entire app · MySQL data persists via named volumes · Students bring the stack down and up repeatedly until muscle memory sets in |
| **Key teaching line** | Docker Compose is the conductor. Each container is a musician. The compose file is the score they all follow. |

---

#### S13 — Nginx as Reverse Proxy
**The problem:** "React runs on port 3000, Node runs on port 5000. How does a user go to one URL and get the right thing?"

| | |
|---|---|
| **Key concepts** | What a reverse proxy does and why it exists · Nginx `server` block · `location` blocks · `proxy_pass` to Node · Serving React production build statically · Adding Nginx as a fourth Compose service · Testing with `curl` |
| **What gets done** | Build React for production with `npm run build` · Add Nginx container to `docker-compose.yml` · Configure: serve React on `/`, proxy `/api/*` to Node · Full MERN app on port 80 via one URL — no raw ports exposed |
| **Key teaching line** | Nginx is the front door. It decides which room each visitor goes to. One port, one URL, three services behind it. |

---

### Phase 4 — CI/CD Pipelines (Sessions 14–17 · 8 hrs)

> **Goal:** Students automate testing and building on every Git push using both
> Jenkins and GitHub Actions. The extra session (S17) is a pipeline failure lab —
> students read logs and fix deliberately broken pipelines independently.
>
> **Why 4 sessions:** Reading CI/CD logs is a skill that must be practised. Students
> who have never diagnosed a failed pipeline in a controlled setting are helpless
> when one fails in real life. The failure lab changes that permanently.

---

#### S14 — CI/CD Concepts + Jenkins Setup
**The problem:** "Every time someone pushes code, someone manually tests and builds it. How do teams automate this?"

| | |
|---|---|
| **Key concepts** | CI vs CD (Delivery vs Deployment) · Pipeline stages: clone → install → test → build → deploy · Jenkins architecture · Jenkins in Docker · `Jenkinsfile` basics · Declarative pipeline syntax |
| **What gets done** | Run Jenkins in a Docker container · Create a basic pipeline job · Write a `Jenkinsfile` that clones the MERN repo and runs `npm install` |
| **Key teaching line** | CI/CD is not a tool — it is a practice. The tool executes the practice automatically on every push. |

---

#### S15 — Jenkins Pipeline — Build & Test
**The problem:** "The pipeline clones the code. But it does not know if the code actually works."

| | |
|---|---|
| **Key concepts** | Pipeline stages in `Jenkinsfile` · `sh` steps · Running `npm test` · Environment variables in Jenkins · Build triggers · Build history and logs · Notification on failure |
| **What gets done** | Add `test` stage to Jenkinsfile · Add `build` stage running `docker build` · Trigger on push to `main` · Deliberately break a test — watch Jenkins report the failure · Fix the test — watch it go green |
| **Key teaching line** | A pipeline that never fails has never been tested. Break it on purpose. That is how you learn what each stage protects. |

---

#### S16 — GitHub Actions — Modern CI/CD
**The problem:** "Jenkins needs a separate server to maintain. Is there a way to run pipelines without that overhead?"

| | |
|---|---|
| **Key concepts** | GitHub Actions architecture · `.github/workflows/` · YAML workflow syntax · `on` triggers · `jobs` and `steps` · `actions/checkout` · GitHub Secrets in workflows · `docker build` and `docker push` to Docker Hub |
| **What gets done** | Write a GitHub Actions workflow triggered on push to `main` · Stages: checkout → install → test → docker build → push to Docker Hub · Compare with Jenkins — discuss when to use each |
| **Key teaching line** | GitHub Actions is CI/CD where the pipeline lives next to the code. No extra server. No extra login. The workflow file is the pipeline. |

---

#### S17 — Pipeline Failure Lab — Read Logs, Fix Pipelines
**The problem:** "The pipeline went red. There are 200 lines of logs. I have no idea what broke or where to look."

| | |
|---|---|
| **Key concepts** | Reading pipeline logs top to bottom · Exit codes and what they mean · Common failure patterns: missing env var, wrong port, failed `npm test`, Docker build error, Docker Hub auth failure · `docker logs` · `docker exec` for debugging inside containers |
| **What gets done** | Instructor pre-breaks five different things in the pipeline one at a time. Students diagnose and fix each using only the logs — no hints. Failures include: missing GitHub Secret, wrong Dockerfile path, failing test, wrong Docker Hub credentials, incorrect build command. |
| **Key teaching line** | Reading logs is a skill, not an instinct. Every senior engineer you admire got there by reading thousands of error messages. Start now. |

---

### Phase 5 — Infrastructure as Code (Sessions 18–19 · 4 hrs)

> **Goal:** Students understand IaC as a concept — writing config files instead of
> clicking dashboards. Terraform provisions. Ansible configures. Same depth as
> before — this phase was already correctly scoped for absolute beginners.

---

#### S18 — Terraform — Infrastructure as Code
**The problem:** "Setting up a server means clicking through 15 screens. If I need to do it again, I repeat every click. And I cannot track a screenshot in Git."

| | |
|---|---|
| **Key concepts** | What is IaC and why it exists · Terraform architecture · `provider`, `resource`, `variable`, `output` blocks · `terraform init` · `terraform plan` · `terraform apply` · `terraform destroy` · State files · Docker provider (no AWS account needed) |
| **What gets done** | Install Terraform · Write `main.tf` using the Terraform Docker provider · `terraform apply` creates a container · `terraform destroy` removes it · Students experience Infrastructure as Code without a cloud account |
| **Key teaching line** | Terraform is a blueprint for infrastructure. Write it once, apply it anywhere, track it in Git. Clicking dashboards is not repeatable. Code is. |

---

#### S19 — Ansible — Configuration Management
**The problem:** "The server exists. But it has nothing on it — no Docker, no app. How do I set it up automatically without logging in and typing commands manually?"

| | |
|---|---|
| **Key concepts** | Ansible vs Terraform — provision vs configure · Agentless (SSH only, no agent installed on server) · Inventory files · Playbooks · Tasks · Modules: `apt`, `copy`, `service`, `shell`, `git` · Idempotency — running twice must not break anything |
| **What gets done** | Write an Ansible playbook that installs Docker on the Linux VM · Copies `docker-compose.yml` to the server · Runs `docker compose up -d` · The MERN app starts on a fresh machine without the student logging in manually |
| **Key teaching line** | Ansible is a remote control for servers. You write what the server should look like. Ansible makes it so — every time, exactly the same. |

---

### Phase 6 — Capstone (Session 20 · 2 hrs)

> **Goal:** Students wire every tool from the course into one automated pipeline.
> Because the extra 10 hours have been distributed across earlier phases, students
> arrive at the capstone genuinely ready — not scrambling to finish the Docker
> session they did not complete.

---

#### S20 — Capstone — Full DevOps Pipeline for the MERN App

**The full picture — everything connected:**

```
Developer pushes to GitHub (main branch)
          ↓
GitHub Actions pipeline triggers automatically
          ↓
  Stage 1: npm install + npm test
  Stage 2: docker build (Node + React images)
  Stage 3: docker push to Docker Hub
          ↓
Ansible playbook runs on Linux server
          ↓
  Pulls latest images from Docker Hub
  Runs docker compose up -d
          ↓
Nginx serves the full MERN app on port 80
          ↓
One URL. Three containers. Fully automated.
```

| | |
|---|---|
| **What gets done** | Each student does a live demo — push one commit, watch it travel through every stage, show the running app on port 80 · Peer questions and feedback · 15-min discussion: what would change with AWS EC2? What does Kubernetes add? What is the Cloud Engineering course? |
| **Key teaching line** | You did not learn DevOps tools. You learned how to make software delivery fast, repeatable, and reliable. The tools will change. That goal never will. |

---

## Complete Session Summary

| Session | Phase | Topic | Hours |
|---|---|---|---|
| S1 | Linux | Linux Fundamentals for DevOps | 2 hrs |
| S2 | Linux | Linux Permissions & User Management | 2 hrs |
| S3 | Linux | Shell Scripting & Process Management | 2 hrs |
| S4 | Linux | Networking Basics & SSH | 2 hrs |
| S5 | Linux | Linux Practice Lab & Consolidation | 2 hrs |
| S6 | Git | Git Branching & Collaboration Workflow | 2 hrs |
| S7 | Git | GitHub Secrets, Branch Protection & Tags | 2 hrs |
| S8 | Git | Team Git Workflow — Real Collaboration Exercise | 2 hrs |
| S9 | Docker | Docker Fundamentals | 2 hrs |
| S10 | Docker | Writing Dockerfiles | 2 hrs |
| S11 | Docker | Docker Networking & Volumes Deep Dive | 2 hrs |
| S12 | Docker | Docker Compose — Multi-Container Apps | 2 hrs |
| S13 | Docker | Nginx as Reverse Proxy | 2 hrs |
| S14 | CI/CD | CI/CD Concepts + Jenkins Setup | 2 hrs |
| S15 | CI/CD | Jenkins Pipeline — Build & Test | 2 hrs |
| S16 | CI/CD | GitHub Actions — Modern CI/CD | 2 hrs |
| S17 | CI/CD | Pipeline Failure Lab — Read Logs, Fix Pipelines | 2 hrs |
| S18 | IaC | Terraform — Infrastructure as Code | 2 hrs |
| S19 | IaC | Ansible — Configuration Management | 2 hrs |
| S20 | Capstone | Full DevOps Pipeline — Demo Day | 2 hrs |
| | | **Total** | **40 hrs** |

---

## Complete Tool Stack

| Tool | Purpose | Sessions |
|---|---|---|
| Linux (Ubuntu / WSL2) | The OS everything runs on | S1–S5 |
| Bash | Automation at the shell level | S3 |
| SSH | Accessing remote servers securely | S4 |
| Git + GitHub | Version control and team collaboration | S6–S8 |
| Docker | Containerising each service | S9–S12 |
| Docker Compose | Orchestrating all three containers | S12 |
| Nginx | Reverse proxy — one URL for the app | S13 |
| Jenkins | Classic CI/CD pipeline | S14–S15 |
| GitHub Actions | Modern CI/CD — pipeline as code | S16 |
| Pipeline debugging | Reading logs, diagnosing failures | S17 |
| Terraform | Infrastructure as Code (intro) | S18 |
| Ansible | Configuration management (intro) | S19 |

---

## What NOT to Teach — Scope Guard

| Topic | Why excluded | Where it belongs |
|---|---|---|
| AWS / GCP / Azure | Cloud is a full discipline — needs its own course | Cloud Engineering — Year 4 / elective |
| Kubernetes | Requires solid Docker foundation; K8s is a career specialisation | Platform Engineering course |
| Prometheus + Grafana | Monitoring belongs after students can deploy reliably | SRE / Cloud Operations course |
| Docker Swarm | Superseded by Kubernetes in industry — not worth a session | Skip entirely |
| Advanced Terraform | Modules, remote state, workspaces | Cloud Engineering course |
| Vault / Secrets Management | Important but complex — beyond this course's scope | DevSecOps course |

---

## What Comes After This Course

| Path | Next Steps |
|---|---|
| **Cloud Engineering** | AWS / GCP fundamentals · EC2 · S3 · RDS · IAM · VPC |
| **Platform Engineering** | Kubernetes · Helm · GitOps (ArgoCD) · Service mesh |
| **DevSecOps** | SAST/DAST · Vault · Container image scanning |
| **SRE** | Prometheus · Grafana · Alerting · SLOs · Incident management |

---

**Satyavs** · [github.com/reachsatyavs](https://github.com/reachsatyavs)
