# Amazon EKS
## Setting up
### Installing kubectl
> When first installing kubectl, it isn't yet configured to communicate with any server. We will cover this configuration as needed in other procedures. If you ever need to update the configuration to communicate with a particular cluster, you can run the following command. 
```bash
aws eks update-kubeconfig --region region-code --name my-cluster
```
## Nodes
### Managed Node Groups
> Amazon EKS Managed node groups automate the provisioning and lifecycle management of nodes(Amazon EC2 instances) for Amazon EKS Kubernetes clusters.

> With Amazon EKS Managed Node Groups,you don't need to separately provision or register the Amazon EC2 instances that provide compute capacity to run your Kubernetes applications. You can create, automatically update, or terminate nodes for your cluster with a single operation. Node updates and terminations automatically drain nodes to ensure that your applications stay available.

> Every managed node is provisioned as part of an Amazon EC2 Auto Scaling group that's managed for you by Amazon EKS. Every resource including the instances and Auto Scaling groups runs within your AWS account. Each node group runs across multiple Availability Zones that you define.

> Cluster -> Node Group -> Node -> Pod -> Container