## Docker

<br>
<br>
<br>

### Overview

- Docker packages our application with everything it needs to run.
- Such as Python, libraries and code.
- It helps our application run consistently across different machines.

<br>
<br>
<br>

### Three Main Pieces

- Dockerfile:
    - A text file containing instructions for building a Docker image.
    - It defines the environment, files to copy, dependencies to install and command to run.

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

<br>

- Image:
    - A packaged, read-only template built from a Dockerfile.
    - It contains the application code, dependencies and filesystem needed to run the app.

<br>

- Container:
    - A running instance of a Docker image.
    - It runs the application in an isolated environment.
    - Multiple containers can run from the same image.
    - - - - 
    - A container can be stopped, deleted and recreated.
    - Hence, data written to its filesystem lost is when the container is removed.
    - Use volumes to persist data beyond a container's lifetime.

<br>
<br>
<br>

### Must-Know Concepts

- Port Mapping:
    - An application listens on a port inside its container.
    - To access it from another machine, you need to publish that port.
    - Example: `docker run -p 9000:8000 my-app`
    - Format: `-p <HOST_PORT>:<CONTAINER_PORT>`
    - Here, port 9000 on your Mac forwards traffic to port 8000 inside the container.

<br>

- `0.0.0.0` vs `127.0.0.1`
    - `127.0.0.1` means localhost. It accept connections only within the container.
    - `0.0.0.0` means listen on all available network inside the container.
    - Our app to be reachable through Docker's published port, it needs to listen on `0.0.0.0`.
