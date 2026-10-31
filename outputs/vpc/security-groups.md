<br>

Get our public IP (IPv4)

```bash
curl https://checkip.amazonaws.com
```

```
X.X.X.X
```

<br>
<br>

Create security group for app

```bash
aws ec2 create-security-group \
    --group-name infra-daily-app-sg \
    --description "Security group for infra-daily app" \
    --vpc-id vpc-XXX \
    --profile infra-daily
```

```json
{
  "GroupId": "sg-XXX",
  "SecurityGroupArn": "arn:aws:ec2:XXX:XXX:security-group/sg-XXX"
}
```

<br>
<br>

Allow inbound traffic from our IP

```bash
aws ec2 authorize-security-group-ingress \
    --group-name infra-daily-app-sg \
    --protocol tcp \
    --port 8000 \
    --cidr X.X.X.X/32 \
    --profile infra-daily
```

```json
{
  "Return": true,
  "SecurityGroupRules": [
    {
      "SecurityGroupRuleId": "sgr-XXX",
      "GroupId": "sg-XXX",
      "GroupOwnerId": "XXX",
      "IsEgress": false,
      "IpProtocol": "tcp",
      "FromPort": 8000,
      "ToPort": 8000,
      "CidrIpv4": "X.X.X.X/32",
      "SecurityGroupRuleArn": "arn:aws:ec2:XXX:XXX:security-group-rule/sgr-XXX"
    }
  ]
}
```

<br>
<br>

Create security group for load balancer

```bash
aws ec2 create-security-group \
    --group-name infra-daily-lb-sg \
    --description "Security group for infra-daily load balancer" \
    --vpc-id vpc-XXX \
    --profile infra-daily
```

```json
{
  "GroupId": "sg-XXX",
  "SecurityGroupArn": "arn:aws:ec2:XXX:XXX:security-group/sg-XXX"
}
```

<br>
<br>

Allow inbound traffic from LB security group

```bash
aws ec2 authorize-security-group-ingress \
    --group-name infra-daily-app-sg \
    --protocol tcp \
    --port 8000 \
    --source-group infra-daily-lb-sg \
    --profile infra-daily
```

```json
{
  "Return": true,
  "SecurityGroupRules": [
    {
      "SecurityGroupRuleId": "sgr-XXX",
      "GroupId": "sg-XXX",
      "GroupOwnerId": "XXX",
      "IsEgress": false,
      "IpProtocol": "tcp",
      "FromPort": 8000,
      "ToPort": 8000,
      "ReferencedGroupInfo": {
        "GroupId": "sg-XXX",
        "UserId": "XXX"
      },
      "SecurityGroupRuleArn": "arn:aws:ec2:XXX:XXX:security-group-rule/sgr-XXX"
    }
  ]
}
```

<br>
<br>

List all security groups

```bash
aws ec2 describe-security-groups \
    --profile infra-daily
```

```json
{
    "SecurityGroups": [
        {
            "GroupId": "sg-XXX",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "UserIdGroupPairs": [],
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": []
                }
            ],
            "VpcId": "vpc-XXX",
            "SecurityGroupArn": "arn:aws:ec2:XXX:XXX:security-group/sg-XXX",
            "OwnerId": "XXX",
            "GroupName": "infra-daily-lb-sg",
            "Description": "Security group for infra-daily load balancer",
            "IpPermissions": []
        },
        {
            "GroupId": "sg-XXX",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "UserIdGroupPairs": [],
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": []
                }
            ],
            "VpcId": "vpc-XXX",
            "SecurityGroupArn": "arn:aws:ec2:XXX:XXX:security-group/sg-XXX",
            "OwnerId": "XXX",
            "GroupName": "infra-daily-app-sg",
            "Description": "Security group for infra-daily app",
            "IpPermissions": [
                {
                    "IpProtocol": "tcp",
                    "FromPort": 8000,
                    "ToPort": 8000,
                    "UserIdGroupPairs": [
                        {
                            "UserId": "XXX",
                            "GroupId": "sg-XXX"
                        }
                    ],
                    "IpRanges": [
                        {
                            "Description": "My laptop on home wifi",
                            "CidrIp": "X.X.X.X/32"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": []
                }
            ]
        },
        {
            "GroupId": "sg-XXX",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "UserIdGroupPairs": [],
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": []
                }
            ],
            "VpcId": "vpc-XXX",
            "SecurityGroupArn": "arn:aws:ec2:XXX:XXX:security-group/sg-XXX",
            "OwnerId": "XXX",
            "GroupName": "default",
            "Description": "default VPC security group",
            "IpPermissions": [
                {
                    "IpProtocol": "-1",
                    "UserIdGroupPairs": [
                        {
                            "UserId": "XXX",
                            "GroupId": "sg-XXX"
                        }
                    ],
                    "IpRanges": [],
                    "Ipv6Ranges": [],
                    "PrefixListIds": []
                }
            ]
        }
    ]
}
```

<br>
<br>
