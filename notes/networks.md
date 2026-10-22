## Networks

<br>
<br>
<br>

### IP Address

- IP Address stands for **Internet Protocol Address**.
- It is a unique numerical address used to identify a device on a network.
- Example: `192.168.1.10`.

<br>

- Just like a courier uses our home address to deliver packages, a network uses an IP address to deliver data to the correct device.
- IP addresses can be:
    - **Private:** Used inside a private network.
    - **Public:** Used to communicate over the internet
- Three ranges are set aside for private use:
    - `10.X.X.X` (`10.0.0.0/8`)
    - `172.16-31.X.X` (`172.16.0.0/12`)
    - `192.168.X.X` (`192.168.0.0/16`)

<br>

#### IPv4:

- IPv4 (Internet Protocol version 4) is the older and widely used version of IP addressing.
- Example: `192.168.1.10`.
- Uses 32 bits to represent an address.
- Written as four numbers separated by dots.
- Each number ranges from 0 to 255.
- Supports about 4.3 billion unique addresses.

<br>

#### IPv6:

- IPv6 (Internet Protocol version 6) is the newer version, designed mainly to provide a much larger pool of IP addresses.
- Example: `2001:db8:1234::1`.
- Uses 128 bits to represent an address.
- Written using hexadecimal numbers separated by colons.
- Supports an extremely large number of addresses. About `3.4 x 10^38`.

<br>

#### CIDR Notation

- CIDR stands for **Classless Inter-Domain Routing**.
- It is a way of representing an IP address range.
- Example: `192.168.1.0/24`.
- In the above example, `/24` means first 24 bits are fixed and last 8 bits are available.
- So the available IP addresses are `192.168.1.0` to `192.168.1.255`. Total 256.
