# Amazon Virtual Private Cloud
## Subnets
### Network ACLs
> The client that initiates the request chooses the ephemeral port range. The range varies depending on the client's operating system.
>>- Many linux kernels(including the Amazon Linux Kernel) use ports 32768 - 61000.
>>- Requests originating from Elastic Load Balancing use ports 1024 - 65535.
>>- Windows operating systems through Windows Server 2003 use ports 1025 - 5000.
>>- Windows Server 2008 and later versions use ports 49152 - 65535.
>>- A NAT gateway uses ports 1024 - 65535.
>>- AWS Lambda functions use ports 1024 - 65535.

> In practice, to cover the different types of clients that might initiate traffic to public-facing instances in your VPC, you can open ephemeral ports 1024 - 65535. However, you can also add rules to the ACL to deny traffic on any malicious ports within that range. Ensure that you place deny rules eariler in the table than the allow rules that open the wide range of ephemeral ports.  

