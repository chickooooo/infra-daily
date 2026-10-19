## Core Concepts

<br>
<br>
<br>

### Amazon Resource Name - ARN

- It is the full address of one thing in AWS.
- Example: a role, a bucket, a file in a bucket or a queue.
- No two things in AWS share the same ARN.

<br>

Format:
```
arn : aws : service : region : account-id : resource
```

<br>

| Example | What it is |
|---|---|
| `arn:aws:iam::XXX:role/s3-readonly-test` | Our role (IAM is global, so the region is empty) |
| `arn:aws:s3:::my-bucket` | A bucket (bucket names are globally unique, so region and account are empty) |
| `arn:aws:s3:::my-bucket/*` | Every object inside that bucket |
| `arn:aws:sqs:ap-southeast-2:XXX:orders` | A queue in Sydney |

<br>

- Empty fields are normal. Region and account are left blank for things that don't need them.
- `*` is a wildcard, so one ARN can cover many things, like "all objects in this bucket".

<br>
<br>
<br>

### AWS Region

- It is a geographical area in the world where AWS has its data centers.
- Each region is assigned a code. Example:
    - Mumbai (`ap-south-1`)
    - Sydney (`ap-southeast-2`)
    - North Virginia (`us-east-1`), etc.
- Each region contains multiple **Availability Zones (AZs)**.

<br>

Why do we need separate regions?
- **Speed:** Data takes time to travel. A region closer to our users will serve them faster.
- **Law:** Some countries want certain data to stay inside their borders.
