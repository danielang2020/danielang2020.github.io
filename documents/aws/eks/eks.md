# Amazon EKS
## Setting up
### Installing kubectl
> When first installing kubectl, it isn't yet configured to communicate with any server. We will cover this configuration as needed in other procedures. If you ever need to update the configuration to communicate with a particular cluster, you can run the following command. 
```bash
aws eks update-kubeconfig --region region-code --name my-cluster
```

## Clusters
### Configuring endpoint access
> You can enable private access to the Kubernetes API server so that all communication between your nodes and the API server stays within your VPC. You can limit the IP addresses that can access your API server from the internet, or completely disable internet access to the API server. 

## Nodes
### Managed Node Groups
> Amazon EKS Managed node groups automate the provisioning and lifecycle management of nodes(Amazon EC2 instances) for Amazon EKS Kubernetes clusters.

> With Amazon EKS Managed Node Groups,you don't need to separately provision or register the Amazon EC2 instances that provide compute capacity to run your Kubernetes applications. You can create, automatically update, or terminate nodes for your cluster with a single operation. Node updates and terminations automatically drain nodes to ensure that your applications stay available.

> Every managed node is provisioned as part of an Amazon EC2 Auto Scaling group that's managed for you by Amazon EKS. Every resource including the instances and Auto Scaling groups runs within your AWS account. Each node group runs across multiple Availability Zones that you define.

> Cluster -> Node Group -> Node -> Pod -> Container

### Instance types
>- **Number of instances in a node group**
> In general, fewer, larger instances are better, especially if you have a lot of Daemonsets. Each instance requires API calls to the API server, so the more instance you have, the more load on the API server.
>- **Maximum number of Pods**
> Since each Pod is assigned its own IP address, the number of IP addresses supported by an instance type is a factor in determining the number of Pods that can run on the instance.

## Storage
### Amazon EBS CSI driver
> THe Amazon EBS CSI driver isn't installed when you first create a cluster. To use the driver, you must add it as an Amazon EKS add-on or as a self-managed add-on.

## Networking
### VPC and subnet requirements
> Load balancers can load balance to Pods in private or public subnets. We recommend deploying your nodes to private subnets, if possible.