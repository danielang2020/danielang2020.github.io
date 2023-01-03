# Amazon Elastic Container Service
## What is Amazon ECS?
### Amazon ECS components
> A task definition is a text file that describes one or more containers that form your application. It's in JSON format. You can use it to describe up to a maximum of ten containers.   
> Your entire application stack doesn't need to be on a single task definition. In fact, we recommend spanning your application across multiple task definitions. You can do this by combining related containers into their own task definitions, each representing a single component.
## AWS Fargate
> For Amazon ECS tasks hosted on Fargate, the following storage types are supported:
>1. Amazon EFS volumes for persistent storage.
>2. Bind mounts for ephemeral storage.

## Task definitions
>- A task is the instantiation of a task definition within a cluster. After you create a task definition for your application within Amazon ECS, you can specify the number of tasks to run on your cluster.  
>- An Amazon ECS service runs and maintains your desired number of tasks simultaneously in an Amazon ECS cluster. How it works is that, if any of tasks fail or stop for any reason, the Amazon ECS service scheduler launches another instance based on your task definition. It does this to replace it and thereby maintain your desired of tasks in the service.  

### Application architecture
#### Using the Fargate launch type
> The Fargate launch type is suitable for the following workloads:
>- Large workloads that require low operational overhead.  
>- Small workloads that have occasional burst.  
>- Tiny worloads.  
>- Batch workloads.  

> If the following conditions are required, we recommend deploying multiple containers into the same task definition:
>- Your containers share a common lifecycle(that is, they're launched and terminated together).  
>- Your containers must run on the same underlying host(that is, one container references the other on a localhost port).  
>- You require that your containers share resources.  
>- Your containers share data volumnes.     

> If these conditions aren't required, we recommend deploying containers separately in multiple task definions. This is because, by doing so, you can scale, provision, and deprovision them separately.  

#### Using the EC2 launch type
> The EC2 launch type is suitable for large workloads that must be price optimized.  

### Task definition parameters
> When running tasks that use the host network mode, do not run containers using the root user(UID 0) for better security. As a security best practice, always use a non-root user, instead of the root user.  

> Currently, only the Amazon ECS-optimized AMI, other Amazon Linux variants with the ecs-init package, or AWS Fargate infrastructure support the awsvpc network mode.  

> The host and awsvpc network modes offer the highest networking performance for containers beacuse they use the Amazon EC2 network stack. With the host and awsvpc network modes, exposed container ports are mapped directly to the corresponding host port(for the host network mode) or the attached elastic network interface port(for the awsvpc network mode). Because of this, you can't use dynamic host port mappings.  

> If using the Fargate launch type, the awsvpc network mode is required.  

> If you're linking mulitple containers in a task definition, the name of one container can be entered in the links of another container. This is to connect the container.  

> The Docker 20.10.0 or later daemon reserves a minimum of 6 MiB of memory for a container. So, don't specify less than 6 MiB of memory for your containers.  

> memory: The amount(in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. The total amount of memory reserved for all containers within a task must be lower than the task memory value, if one specified.  

> memoryReservation: The soft limit(in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when needed, up to either the hard limit that's specified with the memory paramenter(if applicable), or all of the available memory on the container instance, whichever comes first.  

