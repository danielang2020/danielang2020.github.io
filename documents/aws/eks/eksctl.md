# eksctl

## Fargate
```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: auto
  region: us-west-2
  version: "1.29"
iam:
  withOIDC: true
fargateProfiles:
  - name: fp-default
    selectors:
      - namespace: kube-system
  - name: app
    selectors:
      - namespace: default

cloudWatch:
  clusterLoggin:
    enableTypes: ["api","audit","authenticator","controllerManager","scheduler"]      
    logRetentionInDays: 7
```