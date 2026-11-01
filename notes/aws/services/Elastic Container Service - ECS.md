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
