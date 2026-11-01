## Elastic Container Service - ECS

<br>

### Overview

- AWS ECS is a fully managed AWS service.
- It used to deploy, run, and manage Docker containers at scale.
- It helps us run containers without manually managing the infrastructure.

<br>

### Key components

- **Cluster:** A logical grouping of resources where the containers run.
- **Task Definition:** A blueprint that defines the Docker image, CPU, memory, ports, and environment variables.
- **Task:** A running instance of a task definition (one or more containers).
- **Service:** Ensures the desired number of tasks are continuously running. It replaces failed tasks automatically.
- **Container Instance:** An EC2 instance that runs containers (when using EC2 launch type).

<br>

### Launch types

- **EC2:** We manage the underlying EC2 instances.
- **Fargate:** AWS manages the infrastructure; we just deploy containers.

<br>
<br>
<br>

## AWS Fargate

<br>

### Overview

- AWS Fargate is a serverless compute engine for containers.
- It allows us to run Docker containers without managing EC2 instances or servers.
- It works with AWS ECS and EKS.

<br>

- AWS Fargate billing is based on:
    - CPU and memory resources allocated to our containers.
    - Duration they run.

<br>

### How it works

- Create a Docker image.
- Define CPU and memory in the ECS Task Definition.
- Select Fargate as the launch type.
- AWS automatically provisions and manages the infrastructure.
- Our containers start running.

<br>

### Fargate vs EC2

| Fargate | EC2 |
| --- | --- |
| Serverless | Server management required |
| No EC2 management | We manage EC2 instances |
| Pay for allocated resources | Pay for EC2 instances |
| Less infrastructure control | More infrastructure control |
