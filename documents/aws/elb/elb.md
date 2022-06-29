# Elastic Load Balancing

## Load balancers
> If you need flexible application management, we recommend that you use an Application Load Balancer. If extreme performance and static IP is needed for your application, we recommend that you use a Network Load Balancer. If you have an existing application that was built within the EC2-Classic network, then you should use a Classic Load Balancers.  
[Product comparisons](https://aws.amazon.com/elasticloadbalancing/features/)
## Listeners
> The X-Forwarded-For request header is automatically added and helps you identify the IP address of a client when you use an HTTP or HTTPS load balancer.  
> The X-Forwarded-For request header may contain multiple IP addresses that are comma separated. The left-most address is the client IP address where the request was first made.  

> The X-Forwarded-Proto request header helps you identify the protocol(HTTP or HTTPS) that a client used to connect to your load balancer.  

> The X-forwarded-Port request header helps you identify the destination port that the client used to connect to the load balancer.  

