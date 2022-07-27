# Amazon Virtual Private Cloud

> ![](img/subnet_mask.png)

## Virtual private clouds
> When you create a VPC, you must specify an IPv4 CIDR block for the VPC. The allowed block size is between a /16 network(65535 IP addresses) and /28 netmask(16 IP addresses).

### DNS attributes
> The Amazon DNS server does not reside within a specific subnet or Availablility Zone in a VPC. It's located at the address 169.254.169.253.

## Subnets
> The first four IP addresses and the last IP address in each subnet CIDR block are not available for your use, and they cann't be assigned to a resource, such as an EC2 instance. For example, in a subnet with CIDR block 10.0.0.0/24, the following five IP addresses are reserved:
>- 10.0.0.0: Network address.
>- 10.0.0.1: Reserved by AWS for the VPC router.
>- 10.0.0.2: Reserved by AWS. The IP address of the DNS server is the base of the VPC network range plus two. For VPCs with multiple CIDR blocks, the IP address of the DNS server is located in the primary CIDR. We also reserve the base of each subnet range plus two for all CIDR blocks in the VPC. 
>- 10.0.0.3: Reserved by AWS for future use.
>- 10.0.0.255: Network broadcast address. We do not support broadcast in a VPC, therefore we reserve this address.

### Route tables
> Main route table, the route table that automatically comes with your VPC. It controls the routing for all subnets that are not explictly associated with any other route table.

### Network ACLs
> The client that initiates the request chooses the ephemeral port range. The range varies depending on the client's operating system.
>>- Many linux kernels(including the Amazon Linux Kernel) use ports 32768 - 61000.
>>- Requests originating from Elastic Load Balancing use ports 1024 - 65535.
>>- Windows operating systems through Windows Server 2003 use ports 1025 - 5000.
>>- Windows Server 2008 and later versions use ports 49152 - 65535.
>>- A NAT gateway uses ports 1024 - 65535.
>>- AWS Lambda functions use ports 1024 - 65535.

> In practice, to cover the different types of clients that might initiate traffic to public-facing instances in your VPC, you can open ephemeral ports 1024 - 65535. However, you can also add rules to the ACL to deny traffic on any malicious ports within that range. Ensure that you place deny rules eariler in the table than the allow rules that open the wide range of ephemeral ports.  

## Connect your VPC
### Internet gateways
> If a subnet is associated with a route table that has a route to an internet gateway, it's known as a public subnet. If a subnet is associated with a route table that does not have a route to an internet gateway, it's knowed as a private subnet.

### VPC peering connections
> A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them privately. Instances in either VPC can communicate with each other as if they are within the same network.

## Security 
### Security groups
> You can specify allow rules, but not deny rules.