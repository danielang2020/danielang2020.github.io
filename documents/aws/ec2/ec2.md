# EC2
## Instances
### Instance lifecycle
> Notice that you can't stop and start an instance store-backed instance.
> ![](img/il.png)

> When you hibernate an instance, we signal the operating system to perform hibernation(suspend-to-disk), which saves the contents from the instance memory(RAM) to your Amazon EBS root volume.
> When you hibernate your instance, it enters the stopping state, and then the stopped state. We don't charge usage for a hibernated instance when its is in the stopped state, but we do charge while it is in the stopping state, unlike when you stop an instance without hibernating it. We don't charge usage for data transfer fees, but we do charge for the storage for any Amazon EBS volumes, including storage for the RAM data.

## Fleets
### EC2 Fleet
#### Work with EC2 Fleets
> The fleet request must include a launch template that defines the information that the fleet needs to launch an instance, such as an AMI, instance type, subnet or Availability Zone, and one or more security groups.

> EC2 Fleets can only be created using the AWS CLI.

### Spot Fleet
> A Spot Fleet is a set of Spot Instances and optionally On-Demand Instances that is launched based on criteria that you specify.

