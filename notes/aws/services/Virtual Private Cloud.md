## Virtual Private Cloud - VPC

<br>
<br>
<br>

### Overview

- It provides a private network inside AWS to run our services & resources.
- In our AWS account, each region is pre-configured with a default VPC.

<br>

### VPC location

- One VPC sits inside one AWS region.
- Inside that region, it stretches across all availability zones.
- One region can have multiple VPCs. Example: Prod, Testing, etc.
- One VPC cannot be present in multiple regions.

<br>

### IP address

- Each VPC has a range of private IP addresses available.
- Example: `172.31.0.0/16`. This is the default VPC address range.
- These addresses inside a VPC are free.

<br>
<br>
<br>

## Subnet

<br>

### Overview

- A subnet is a smaller range of IP addresses within a VPC.
- It is used to isolate and organise resources.
- Example: VPC CIDR: `172.31.0.0/16`.
    - Subnet 1: `172.31.1.0/24`,
    - Subnet 2: `172.31.2.0/24`,

<br>

### Types of subnets:

- Public subnet: Resources can access the internet through an Internet Gateway.
- Private subnet: No direct route to an Internet Gateway.

<br>

### Features:

- One subnet belongs to only one AZ inside a VPC.
- One AZ can hold multiple subnets.
- Most setups generally have 2 subnets per AZ. One public & one private.
- 5 addresses in every subnet is reversed by AWS.

<br>
<br>
<br>

## Internet Gateway

<br>

### Overview

- Internet gateway is also written as **IGW**.
- It allows resources in a VPC to communicate with the internet.

<br>

### How it works

- Create an Internet Gateway and attach it to the VPC.
- Add a route to the internet gateway in the route table (`0.0.0.0/0`).
- Configure the EC2 instance with a public IP and appropriate security rules.
- This EC2 instance can now communicate with the internet.
- **Note:**
    - An Internet Gateway alone does not make the EC2 instance publicly accessible.
    - We also need the correct routing, public IP, and security settings.

<br>

### Features:

- One VPC can have only 1 IGW. And vice-versa.
- It's free of cost and managed by AWS.

<br>
<br>
<br>

## Route Table

<br>

### Overview

- It is a table containing a set of rules that tells network traffic where to go inside our VPC.
- These rules are known as **Routes**.
- Each route has a destination and a target.

<br>

| Destination | Target | Meaning |
| --- | --- | --- |
| `172.31.0.0/16` | `local` | Traffic stays inside the VPC |
| `0.0.0.0/0` | `igw-12345` | Traffic goes toward the Internet Gateway |

<br>

### Features

- Every VPC automatically gets a main route table.
- A VPC can have multiple route tables.
- Each subnet is associated with one route table at a time.
- A route table can be associated with multiple subnets.

<br>

### More

- A subnet is public if it's route table has this entry:  `0.0.0.0/0` -> `igw-12345`.
- When selecting a route from the route table, most specific one is selected.
- Example: If the destination is `172.31.10.12`, then `172.31.0.0/16` is selected instead of `0.0.0.0/0`.

<br>
<br>
<br>

## Elastic IP

<br>

### Overview

- Elastic IP is also written as **EIP**.
- It is a static public IPv4 address that we can allocate to our AWS resources.

<br>

### Why it is needed?

- Normally, a resource's public IP can change when we stop and start it.
- An Elastic IP gives it a fixed public IP address.

<br>

### Features

- **Static:** The IP address stays the same.
- **Reassignable:** We can move it from one resource to another.
- **Cost:** We pay an hourly charge for each Elastic IP, whether it is attached or not.

<br>
<br>
<br>

## NAT Gateway

<br>

### Overview

- It allows resources in a private subnet to access the internet.
- But it does not allow the internet to initiate connections directly to those resources.

<br>

### When it is needed?

- A service needs to download packages or call an external API.
- A NAT Gateway lets it make those outbound connections without exposing the instance directly to the internet.

<br>

### Features

- It lives in a public subnet so it can access the internet.
- A new route is added in the private subnet's route table for NAT gateway: `0.0.0.0/0` -> `nat-123`.
- We pay for the NAT Gateway's running time and the data it processes, plus applicable data transfer charges.
- A NAT gateway lives in one AZ.

<br>

### Important

- NAT gateway also charges for data transfer. So pulling large docker images is expensive.
- Services like S3, ECR, Secrets Manager, CloudWatch logs, etc. don't live inside the VPC.
- So, data transfer between the app and those services is charged.
- There's a solution for this: VPC endpoint.

<br>
<br>
<br>

## VPC Endpoint

### Overview

- It allows resources inside a VPC to privately connect to supported AWS services.
- Without going through the public internet.
- This reduces NAT Gateway data processing costs when accessing services like S3 or DynamoDB.

### Types:

- **Gateway Endpoint:**
    - Used for S3 and DynamoDB. No additional endpoint charge.
    - A route is added to the route table for Gateway Endpoints.

- **Interface Endpoint:**
    - Commonly used for services like ECR, Secrets Manager and CloudWatch Logs.
    - Uses AWS PrivateLink and creates private network interfaces (ENIs) in the subnets.
    - It uses private IP addresses and DNS, no route in RT needed.
    - It generally charges for endpoint uptime and data processed.
