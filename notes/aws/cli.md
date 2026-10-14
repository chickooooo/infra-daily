## AWS CLI

<br>
<br>
<br>

### Command structure:

```
aws <service> <operation> [options]
```

Example:
```
aws s3 ls
```

<br>
<br>
<br>

### AWS CLI version

```
aws --version
```

Output:
```
aws-cli/2.37.6 Python/3.14.6 Linux/6.1.188-233.385.amzn2023.x86_64 exec-env/CloudShell exe/x86_64.amzn.2023
```

<br>
<br>
<br>

### Caller Identity

- It shows which AWS Identity the commands are running as.
- Returns user ID, account ID and ARN.

```
aws sts get-caller-identity
```

Output:
```
{
    "UserId": "XXX:XXX",
    "Account": "XXX",
    "Arn": "arn:aws:sts::XXX:assumed-role/AccountFullAccessRole/XXX"
}
```
