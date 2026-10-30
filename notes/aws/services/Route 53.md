## Route 53

<br>
<br>
<br>

### Overview

- It is a DNS (Domain Name System) service.
- It is highly available and scalable.
- It translates domain names into IP addresses so users can access our application.
- Example: `www.example.com` -> `43.2.0.2`.
- We create a DNS record in Route 53 that maps the domain to our resource's public IP.

<br>
<br>

### Features

- Allows registration and management of domain names.
- Routes user traffic based on different routing strategies.
- Monitors the health of application endpoints.

<br>
<br>

### Types of Routing Policies

| Routing Policy | Purpose |
| --- | --- |
| Simple Routing | Routes traffic to a single resource. |
| Weighted Routing | Distributes traffic based on assigned weights. |
| Latency-Based Routing | Routes users to the region with the lowest latency. |
| Geolocation Routing | Routes traffic based on the user's geographic location. |
