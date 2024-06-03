# Karpenter
1. [install karpenter](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/)
1.a. in 3. Create a Cluster section, should add (spot: true) attribute.
``` yaml
managedNodeGroups:
- instanceType: m5.large
  amiFamily: AmazonLinux2
  name: ${CLUSTER_NAME}-ng
  desiredCapacity: 2
  minSize: 1
  maxSize: 10
  spot: true
```    
1.b. in 5. Create NodePool section, should add label below.
```yaml
spec:
  template:
    metadata:
      labels:
        type: karpenter
```
1.c. create everything that document mention until 6. Scale up deployment.

2. [deploy application](https://www.eksworkshop.com/docs/introduction/getting-started/first)
2.a [before deploying, should modify every pod spec config with adding nodeSelection](https://github.com/aws-samples/eks-workshop-v2/tree/main/manifests/base-application)
```yaml
spec:
  template:    
    spec:
      nodeSelector:
          type: karpenter
```

3. [install load balancer controller](https://docs.aws.amazon.com/eks/latest/userguide/lbc-helm.html)