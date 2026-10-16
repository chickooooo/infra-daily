## AWS CLI

<br>
<br>
<br>

### Command structure:

```
aws <service> <operation> [options]
```

<br>

Example commands:

```bash
aws ec2 describe-instances
aws s3 ls
aws iam list-users
aws lambda list-functions
aws rds describe-db-instances
```

<br>

Common service codes:

| Service code | Service name |
| --- | --- |
| `ec2` | Elastic Compute Cloud |
| `s3` | Simple Storage Service |
| `iam` | Identity and Access Management |
| `lambda` | AWS Lambda |
| `rds` | Relational Database Service |
| `dynamodb` | Amazon DynamoDB |
| `ecs` | Elastic Container Service |
| `eks` | Elastic Kubernetes Service |
| `ecr` | Elastic Container Registry |
| `vpc` | Virtual Private Cloud |
| `elb` | Elastic Load Balancing (classic) |
| `elbv2` | Elastic Load Balancing (v2) |
| `sns` | Simple Notification Service |
| `sqs` | Simple Queue Service |
| `route53` | Amazon Route 53 |
| `cloudfront` | Amazon CloudFront |
| `cloudwatch` | Amazon CloudWatch |
| `cloudformation` | AWS CloudFormation |
| `kms` | Key Management Service |
| `secretsmanager` | AWS Secrets Manager |
| `sts` | Security Token Service |
| `apigateway` | Amazon API Gateway |
| `backup` | AWS Backup |
| `bedrock` | Amazon Bedrock |

<br>
<br>
<br>

### Core

<br>
<br>

Check the installed AWS CLI version
```
aws --version
```
```
aws-cli/2.37.6 Python/3.14.6 Linux/6.1.188-233.385.amzn2023.x86_64 exec-env/CloudShell exe/x86_64.amzn.2023
```

<br>
<br>

Log in to AWS using the given profile
```
aws login --profile infra-daily
```
```
Successfully logged in.
```

<br>
<br>

List all configured AWS CLI profiles
```
aws configure list-profiles
```
```
default
infra-daily
```

<br>
<br>

Get the caller identity
```
aws sts get-caller-identity
```
```
{
  "UserId": "AIDAEXAMPLE123456",
  "Account": "123456789012",
  "Arn": "arn:aws:iam::123456789012:user/example"
}
```

<br>
<br>

Run AWS command in the given region
```
<command> --region ap-south-1
```
```
...
```

<br>
<br>
<br>

### S3

<br>
<br>

List S3 buckets
```
aws s3 ls
```
```
2026-09-10 10:15:22 my-app-bucket
2026-09-12 14:30:05 my-backup-bucket
```

<br>
<br>

List files inside a bucket
```
aws s3 ls s3://my-app-bucket/
```
```
2026-10-01 09:30:10       1024 file1.txt
2026-10-02 11:45:00       2048 file2.csv
```

<br>
<br>

Upload a file to S3 bucket
```
aws s3 cp file.txt s3://my-app-bucket/file.txt
```
```
upload: ./file.txt to s3://my-app-bucket/file.txt
```

<br>
<br>

Download a file from S3 bucket
```
aws s3 cp s3://my-app-bucket/file.txt ./file.txt
```
```
download: s3://my-app-bucket/file.txt to ./file.txt
```

<br>
<br>

Create a new S3 bucket
```
aws s3 mb s3://my-new-bucket-12345 --region ap-south-1
```
```
make_bucket: my-new-bucket-12345
```

<br>
<br>

Delete an object from S3
```
aws s3 rm s3://my-app-bucket/file.txt
```
```
delete: s3://my-app-bucket/file.txt
```

<br>
<br>

Delete an empty bucket
```
aws s3 rb s3://my-app-bucket
```
```
remove_bucket: my-app-bucket
```
