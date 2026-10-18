
<br>

List all VPCs
```bash
aws ec2 describe-vpcs \
    --profile infra-daily
```
```json
{
  "Vpcs": [
    {
      "OwnerId": "XXX",
      "InstanceTenancy": "default",
      "CidrBlockAssociationSet": [
        {
          "AssociationId": "vpc-cidr-assoc-xxx",
          "CidrBlock": "X.X.X.X/16",
          "CidrBlockState": {
            "State": "associated"
          }
        }
      ],
      "IsDefault": true,
      "BlockPublicAccessStates": {
        "InternetGatewayBlockMode": "off"
      },
      "VpcId": "vpc-xxx",
      "State": "available",
      "CidrBlock": "X.X.X.X/16",
      "DhcpOptionsId": "dopt-xxx"
    }
  ]
}

```

<br>
<br>

List all subnets belonging to VPC
```bash
aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=vpc-xxx" \
    --profile infra-daily
```
```json
{
  "Subnets": [
    {
      "AvailabilityZoneId": "apse2-az3",
      "MapCustomerOwnedIpOnLaunch": false,
      "OwnerId": "XXX",
      "AssignIpv6AddressOnCreation": false,
      "Ipv6CidrBlockAssociationSet": [],
      "SubnetArn": "arn:aws:ec2:ap-southeast-2:XXX:subnet/subnet-xxx",
      "EnableDns64": false,
      "Ipv6Native": false,
      "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
      },
      "BlockPublicAccessStates": {
        "InternetGatewayBlockMode": "off"
      },
      "SubnetId": "subnet-xxx",
      "State": "available",
      "VpcId": "vpc-xxx",
      "CidrBlock": "X.X.X.X/20",
      "AvailableIpAddressCount": 4091,
      "AvailabilityZone": "ap-southeast-2b",
      "DefaultForAz": true,
      "MapPublicIpOnLaunch": true
    },
    {
      "AvailabilityZoneId": "apse2-az1",
      "MapCustomerOwnedIpOnLaunch": false,
      "OwnerId": "XXX",
      "AssignIpv6AddressOnCreation": false,
      "Ipv6CidrBlockAssociationSet": [],
      "SubnetArn": "arn:aws:ec2:ap-southeast-2:XXX:subnet/subnet-xxx",
      "EnableDns64": false,
      "Ipv6Native": false,
      "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
      },
      "BlockPublicAccessStates": {
        "InternetGatewayBlockMode": "off"
      },
      "SubnetId": "subnet-xxx",
      "State": "available",
      "VpcId": "vpc-xxx",
      "CidrBlock": "X.X.X.X/20",
      "AvailableIpAddressCount": 4091,
      "AvailabilityZone": "ap-southeast-2a",
      "DefaultForAz": true,
      "MapPublicIpOnLaunch": true
    },
    {
      "AvailabilityZoneId": "apse2-az2",
      "MapCustomerOwnedIpOnLaunch": false,
      "OwnerId": "XXX",
      "AssignIpv6AddressOnCreation": false,
      "Ipv6CidrBlockAssociationSet": [],
      "SubnetArn": "arn:aws:ec2:ap-southeast-2:XXX:subnet/subnet-xxx",
      "EnableDns64": false,
      "Ipv6Native": false,
      "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
      },
      "BlockPublicAccessStates": {
        "InternetGatewayBlockMode": "off"
      },
      "SubnetId": "subnet-xxx",
      "State": "available",
      "VpcId": "vpc-xxx",
      "CidrBlock": "X.X.X.X/20",
      "AvailableIpAddressCount": 4091,
      "AvailabilityZone": "ap-southeast-2c",
      "DefaultForAz": true,
      "MapPublicIpOnLaunch": true
    }
  ]
}
```

<br>
<br>

List all route tables belonging to VPC
```bash
aws ec2 describe-route-tables \
    --filters "Name=vpc-id,Values=vpc-xxx" \
    --profile infra-daily
```
```json
{
  "RouteTables": [
    {
      "Associations": [
        {
          "Main": true,
          "RouteTableAssociationId": "rtbassoc-xxx",
          "RouteTableId": "rtb-xxx",
          "AssociationState": {
            "State": "associated"
          }
        }
      ],
      "PropagatingVgws": [],
      "RouteTableId": "rtb-xxx",
      "Routes": [
        {
          "DestinationCidrBlock": "X.X.X.X/X",
          "GatewayId": "local",
          "Origin": "CreateRouteTable",
          "State": "active"
        },
        {
          "DestinationCidrBlock": "0.0.0.0/0",
          "GatewayId": "igw-xxx",
          "Origin": "CreateRoute",
          "State": "active"
        }
      ],
      "Tags": [],
      "VpcId": "vpc-xxx",
      "OwnerId": "XXX"
    }
  ]
}
```

<br>
<br>

List all internet gateways belonging to VPC
```bash
aws ec2 describe-internet-gateways \
    --filters "Name=attachment.vpc-id,Values=vpc-xxx" \
    --profile infra-daily
```
```json
{
    "InternetGateways": [
        {
            "Attachments": [
                {
                    "State": "available",
                    "VpcId": "vpc-xxx"
                }
            ],
            "InternetGatewayId": "igw-xxx",
            "OwnerId": "XXX",
            "Tags": []
        }
    ]
}
```
