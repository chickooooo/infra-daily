## Identity and Access Management - IAM

<br>
<br>
<br>

### Overview

- This service is AWS's security guard.
- Every request to AWS, from console, CLI or code, goes through IAM.
- It takes care of 2 things:
    - **Authentication**: Who are you?
    - **Authorization**: What are your allowed to do?
- It provides restricted access to a person, app or a service.

<br>
<br>

### Pieces of IAM

- Policy:
    - A JSON document of rules, such as "Allow reading S3 buckets".
    - On its own, it does nothing. It has to be atatched to an **Identity**.
- Identity:
    - It is what a policy is attached to.
    - **User**: A long lived identity with a password and/or access keys.
    - **Role**: A borrowed identity.

<br>
<br>

### Role

- A role is like a visitor badge. It has no password or keys of its own.
- Someone who is allowed to wear it, can assumes it.
- They get temporary credentials that expire in about an hour and can do only what the badge allows.
- Every role has two policies:
    - **Trust policy**: Who can wear this badge.
    - **Permissions policy**: What the badge lets you do. Anything not listed is denied by default.

<br>

- A role can be assigned to AWS services like EC2, Lambda, ECS task, etc.
- Example: An EC2 instance gets a role that can list buckets but not create them.
- Each role has a **Session Duration**. It defines the maximum duration an entity can assume the role for.
- AWS services automatically refresh the session before it expires.
