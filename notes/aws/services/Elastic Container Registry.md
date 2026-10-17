## Elastic Container Registry - ECR

<br>
<br>
<br>

### Overview

- It is AWS's storage for Docker images.
- It is a private "Docker Hub" inside our account.
- Why it exists:
    - Anything in AWS that runs containers (ECS, Lambda, EKS) needs to pull the image from somewhere.
    - ECR is that place: Private, in our region, and controlled by IAM.

<br>
<br>
<br>

### Structure

- **Registry**:
    - One registry per account per region.
    - Its address looks like `<account-id>.dkr.ecr.<region>.amazonaws.com`.

- **Repository**:
    - One repository per app. Example `infra-daily-app`.
    - It holds every version of that image.

- **Tag**:
    - Label for version of the image, like `v1` or `latest`.
    - The full name of an image is: `<registry>/<repository>:<tag>`.

<br>
<br>
<br>

### Key Points

- Docker needs to log in to ECR, and the AWS CLI gives it a token for that.
- The login is still IAM underneath: anyone who can't access ECR can't push or pull.

<br>

- Tags can move. If we push `latest` again, it points to the new image.
- Every image also has a digest (`sha256:...`) that never changes. Use that when we need exactly one version.

<br>

- **Cost & Storage:**
    - Storage is about `$0.10` per GB per month.
    - Images are stored in compressed form.
