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
