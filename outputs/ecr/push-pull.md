
<br>

Create a new repository
```bash
aws ecr create-repository \
    --repository-name infra-daily-app \
    --region XXX \
    --profile infra-daily
```
```
{
  "repository": {
    "repositoryArn": "arn:aws:ecr:XXX:XXX:repository/infra-daily-app",
    "registryId": "XXX",
    "repositoryName": "infra-daily-app",
    "repositoryUri": "XXX.dkr.ecr.XXX.amazonaws.com/infra-daily-app",
    "createdAt": "2026-10-17T10:28:42.220000+05:30",
    "imageTagMutability": "MUTABLE",
    "imageScanningConfiguration": {
      "scanOnPush": false
    },
    "encryptionConfiguration": {
      "encryptionType": "AES256"
    }
  }
}
```

<br>
<br>


Login to ECR
```bash
aws ecr get-login-password \
    --profile infra-daily \
    --region XXX \
    | docker login \
        --username AWS \
        --password-stdin <registry_uri>
```
```
Login Succeeded
```

<br>
<br>

Tag local image with full ECR name
```bash
docker tag infra-daily-app:latest <repository_uri>:v1
```
```
```

<br>
<br>

Check tag
```bash
docker images
```
```
IMAGE                                                                  ID             DISK USAGE   CONTENT SIZE   EXTRA
XXX.dkr.ecr.XXX.amazonaws.com/infra-daily-app:v1   XXX                 285MB         68.1MB
```

<br>
<br>

Push image to ECR
```bash
docker push <repository_uri>:v1
```
```
The push refers to repository [<repository_uri>]
XXX: Pushed
XXX: Pushed
XXX: Pushed
v1: digest: sha256:XXX size: 856
```

<br>
<br>

Check ECR repository
```bash
aws ecr describe-images \
    --repository-name infra-daily-app \
    --profile infra-daily
```
```
{
  "imageDetails": [
    {
      "registryId": "XXX",
      "repositoryName": "infra-daily-app",
      "imageDigest": "sha256:XXX",
      "imageSizeInBytes": 1687,
      "imagePushedAt": "2026-10-17T11:17:18.287000+05:30",
      "imageManifestMediaType": "application/vnd.oci.image.manifest.v1+json",
      "artifactMediaType": "application/vnd.docker.attestation.manifest.v1+json",
      "subjectManifestDigest": "sha256:XXX",
      "imageStatus": "ACTIVE"
    },
    {
      "registryId": "XXX",
      "repositoryName": "infra-daily-app",
      "imageDigest": "sha256:XXX",
      "imageSizeInBytes": 68112222,
      "imagePushedAt": "2026-10-17T11:17:18.277000+05:30",
      "imageManifestMediaType": "application/vnd.oci.image.manifest.v1+json",
      "artifactMediaType": "application/vnd.oci.image.config.v1+json",
      "imageStatus": "ACTIVE"
    },
    {
      "registryId": "XXX",
      "repositoryName": "infra-daily-app",
      "imageDigest": "sha256:XXX",
      "imageTags": ["v1"],
      "imageSizeInBytes": 68112222,
      "imagePushedAt": "2026-10-17T11:17:19.145000+05:30",
      "imageManifestMediaType": "application/vnd.oci.image.index.v1+json",
      "imageStatus": "ACTIVE"
    }
  ]
}
```

<br>
<br>

Pull Image from ECR
```bash
docker pull <repository_uri>:v1
```
```
v1: Pulling from infra-daily-app
XXX: Pull complete
XXX: Already exists
XXX: Download complete
Digest: sha256:XXX
Status: Downloaded newer image for <repository_uri>:v1
```

<br>
<br>

Run new image
```bash
docker run -d --name id-app -p 9000:9000 -e PORT=9000 <repository_uri>:v1
```
```
XXX
```

<br>
<br>

Hit `/health` endpoint
```bash
curl -i localhost:9000/health
```
```
HTTP/1.1 200 OK
date: Sat, 17 Oct 2026 05:54:58 GMT
server: uvicorn
content-length: 15
content-type: application/json

{"status":"ok"}
```

<br>
<br>

Check running containers
```bash
docker ps
```
```
CONTAINER ID   IMAGE                  COMMAND            CREATED         STATUS         PORTS                                         NAMES
4c278c8a1d3c   <repository_uri>:v1    "uv run main.py"   8 seconds ago   Up 8 seconds   0.0.0.0:9000->9000/tcp, [::]:9000->9000/tcp   id-app
```
