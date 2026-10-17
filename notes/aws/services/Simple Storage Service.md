## Simple Storage Service - S3

<br>
<br>
<br>

### Overview

- It is AWS's file storage service.
- We put files, which S3 calls **objects**, into containers called **buckets**, and read them back over the API from anywhere.
- Used to store anything file-shaped, such as user uploads, backups, logs, static websites, or raw requests.

<br>
<br>
<br>

### Key points

- **No real folders**:
    - An object's name is called a **key**. It can contain slashes like `reports/2026/oct.pdf`.
    - The console shows those as folders, but a bucket is really a flat list of keys.
- **Private by default**:
    - Nothing in a bucket is public unless we deliberately open it up.
- **Pricing**:
    - We pay for the amount of data stored (GB/month).
    - Charges also apply for API requests (PUT, GET, etc.) and retrieving data.

<br>
<br>
<br>

### 
