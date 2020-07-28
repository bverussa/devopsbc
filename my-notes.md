# My Notes

- [ComIT](https://www.comit.org/)
- [Code Cast](https://www.codecast.io/)
- [Google Meet](https://meet.google.com/xon-irfy-egq)
- [Course Material](https://github.com/emersonmellado/devops)

## May 20, 2020
### Course Overview / Expectation:
- Tech+
- Soft Skills+
  - Commitment
  - Responsibility
  - Teamwork
    - Everyone understands the goal
      - The discussion is orderly
      - Decisions are reached by consensus
      - There are no personal attacks
      - Leadership is rotational
  - Tolerance to frustration
    - “Being a software developer means, learning how to get frustrated every day and keep going"
- Final Project

## May 22, 2020
- What is DevOps
- Common Tools and Resouces
  - Cloud Providers
    - AWS *
    - Azure
    - Google Cloud
  - Automation Test Tools
    - [Selenium](https://www.selenium.dev)
  - CI (Continuous Integration) Tools
    - [Jenkins *](https://www.jenkins.io)
  - CD (Continuous Delivery) Tools
    - [Chef *](https://www.chef.io)
    - [Puppet *](https://puppet.com)
    - [Ansible *](https://www.ansible.com)
  - Containerization Tools
    - [Docker *](https://www.docker.com)
    - [Kubernetes - Container Orchestration *](https://kubernetes.io)
  - Logging / Monitoring Tools
    - [Splunk *](https://www.splunk.com)
    - [Nagios](https://www.nagios.com)
- DevOps Skills
  - Linux Fundamentals and Scripting (security admin, shell scripting, vurtualization, user admin)
  - Programming Languages (eg. Python: OOPS Concepts, script debugging, CRUD Operations, Python IDE)
  - Infrastructure as Coode
  - Cloud Experience and Devps Key Concepts
  - Communication and Collaboration with others
  - Continuous Integration and Delivery
  - Knowledge on various DevOps tools and technologies
- Key Concepts
  - Continuous Integration
    - Commit Code (eg. Git) => Unit and Integration Test / Build (eg. Selenium / Jenkins)
  - Continuous Delivery
    - Deploy to Test / QA Environment => Acceptance Testing
  - Continuous Deployments
    - Deploy to Production
  - [Continuous Integration vs Delivery vs Deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)
  - [Example of a DevOps Program Syllabus](https://www.edureka.co/masters-program/devops-engineer-training)

## May 25, 2020
- Git & GitHub

## May 27, 2020
- Git & GitHub (cont.)
- [Git commands](git-commands.md)
- [Git Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4)

## May 29, 2020
- Operating Systems

## June 1, 2020
- Setup
  - [Docker instalation on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
  - [My Jenkins](http://localhost:8080)
    - User: admin
    - Pwd: devops

## June 3, 2020
- Logic
- Logic Statement Exercises:

```
"Today is raining and the grass is wet"
let p = "Today is raining"
let q = "Grass is wet"

Conjunction: `p ^ q` : "Today is raining AND the grass is wet"
Disjunction: `p v q` : "Today is raining OR the grass is wet"
Negation: `~p v ~q` : "Today is not raining OR the grass is not wet"

"I won't buy toilet paper and carry it with me"
let p = "I will buy toilet paper"
let q = "Carry it with me"

Conjunction: `~p ^ q` : "I won't buy toilet paper AND carry it with me"
Disjunction: `~p v q` : "I won't buy toilet paper OR carry it with me"
Negation: `p v ~q` : "I will buy toilet paper OR carry it with me"

"Neither Jane or I drink"
let j = "Jane drink"
let i = "I drink"

Conjunction: `~j v ~i` : "Neither Jane OR I drink"
Disjunction: `~j ^ ~i` : "Neither Jane AND I drink"
Negation: `j ^ i` : "Jane AND I drink"

"The Cannucks did not win or the game is going longer"
let p = "The Canucks won"
let q = "The game is going longer"

Conjunction: `~p v q` : "The Canucks did not win OR the game is going longer"
Disjunction: `~p ^ q` : "The Canucks did not win AND the game is going longer"
Negation: `p ^ ~q` : "The Canucks won AND the game is not going longer"
```

## June 5, 2020
- Logic (cont.)
  - Truth Tables
- Operating Systems (cont.)
  - Linux
    - Permissions
      - Read, Write, Execute
      - > rwx = 7
      - > r = 4
      - > w = 2
      - > x = 1
    - Folder Structure
      - [Linux Directory Structure](https://linuxhandbook.com/linux-directory-structure/)

## June 8, 2020
- Operating Systems (cont.)
  - Kernel versions
    - [kernel.org](kernel.org)
  - Key Groups / Users
    - root: administrator
    - daemon: automated user OR automated system user
  - Shell

## June 10, 2020
- Python

## June 12, 2020
- Python (cont.)

## June 15, 2020
- Python (cont.)

## June 17, 2020
- Python (cont.)

## June 19, 2020
- Python (cont.)

## June 22, 2020
- Python (cont.)

## June 24, 2020
- Recruiter Presentation

## June 26, 2020
- Python (cont.)

## June 29, 2020
- Python (cont.)

## June 29, 2020
- OOP - Object Oriented Programming
  - Classes (objects)
    - Polymorphism
    - Inheritance
  - Members
    - Attributes (Properties)
    - Methods
    - Constructor
    - Messages
    - Local Variables
    - Access Operators
    - Accessibility
    - Encacpsulation
    - 
    
# July 3, 2020
- OOP (cont.)

# July 6, 2020
- OOP (cont.)

# July 8, 2020
- OOP (cont.)

# July 10, 2020
- Networking
- AWS
  - EBS (Elastic Beanstalk)

# July 13, 2020
- Networking (cont.)

# July 15, 2020
- Networking (cont.)
- Application Plan
  1. Register a domain in godaddy
  2. Use Route 53 to configure the DNS
    * NS entries: ns-183.awsdns-22.com. ns-1088.awsdns-08.org. ns-1970.awsdns-54.co.uk. ns-744.awsdns-29.net.
    * Run DNS checker
    * Created an apex entry
    * Created an www entry
  3. Use Elastic Beanstalk as the Pipeline management
    * Open the tutorial
    * Created the local app
    * Tested it locally
    * eb init
      * eb init -p python-3.6 mydevopsbc --region cac-central-1
    * Installed EB CLI
      * pip install awsebcli --upgrade
    * Deploy
  4. Use git as version control 
- Pipelines examples
  - Environment
    - Domains
      - DNS management
    - Load balancer
    - Security (firewall, SSL, keys, ssh, etc.)
    - Version the environment
    - Host versions pre deploy
  - Application
    - Python
    - Flask
    - pip
  - Development
    - Local environment (dev computer)
      - Language (Python)
      - IDE (vscode, pycharm, etc.)
    - Application requirements
    - Build
    - Test
    - Version control (git)
  - Jenkins
    - Checkout (get code from git)
    - Build
    - Test
    - Deploy

# July 17, 2020
- Networking (cont.)

# July 20, 2020
- CI/CD

# July 22, 2020
- CI/CD (cont.)
  - Jenkins
    - Automation tool
    - Development
    - Build
    - Deployment
    - Pipelines
  - Ansible
    - Configuration tool
    - Operating system management
    - Software instalation
    - Creates user
  - Vagrant
    - Virtualization management tool
    - Make it easier to create and share virtual machines
  - Docker
    - Container management tool
  - Kubernetes / Docker Swarm
    - Container orchestration system for automating computer application deployment, scaling, and management
- Virtualization

# July 24, 2020
- CI/CD (cont.)
  - Jenkins: setup
  - Jenkins: creating pipelines
  - Docker: docker exec -it docker_id /bin/bash

# July 27, 2020
- CI/CD (cont.)
  - Jenkins (cont.)
    1. Creating more pipelines
      - With parameters
      - With external shell scripts
      - Multiple stages
    2. Jenkins agents
      - Setup one or more agents
      - Multiple agents (nodes)
    3. Linking Jenkins and GitHub

[<- Go Back](README.md)