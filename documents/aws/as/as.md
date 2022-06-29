# Amazon EC2 Auto Scaling

## Scale your group
### Set capacity limits
> The group's desired capacity is resizeable between the minimum and maximum size limits. The desired capacity must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.  

> An Auto Scaling group will start by launching as many instances as are specified for desired capacity. If there are no scaling policies or scheduled actions attached to the Auto Scaling group, Amazon EC2 Auto Scaling maintains the desired amount of instances, performing periodic health checks on the instances in the group.  

### Dynamic scaling
#### Set default warm-up or cooldown values
> After your Auto Scaling group launches or terminates instances, it waits for a cooldown period to end before any further scaling activities initiated by simple scaling policies can start. 

### Lifecycle hooks
> A popular use of lifecycle hooks is to control when instances are registered with Elastic Load Balancing. By adding a launch lifecycle hook to your Auto Scaling group, you can ensure that your bootstrap scripts have completed successfully and the applications on the instances are ready to accept traffic before they are registered to the load balancer at the end of the lifecycle hook.