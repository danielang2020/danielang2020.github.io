# Certified Kubernetes Administrator(v1.29)
## Cluster Architecture, Installation & Configuration
### [Manage role based access control(RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
1. User (RoleBinding is User kind) [RBAC with Kubernetes in Minikube](https://medium.com/@HoussemDellai/rbac-with-kubernetes-in-minikube-4deed658ea7b)
    1.1 Generate a key using OpenSSL
    ```shell
    openssl genrsa -out daniel.key 2048
    ```
    1.2 Generate a Client Sign Request, CN must match user, O must match group.
    ```shell
    openssl req -new -key daniel.key -out daniel.csr -subj "/CN=daniel/O=dev"
    ``` 
    1.3 Generate the certificate. (/etc/kubernetes/pki in production env.)
    ```shell
    openssl x509 -req -in daniel.csr -CA ~/.minikube/ca.crt -CAkey ~/.minikube/ca.key -CAcreateserial -out daniel.crt -days 500
    ```
    1.4 Set a user entry in kubeconfig
    ```shell
    kubectl config set-credentials daniel --client-certificate=daniel.crt --client-key=daniel.key
    ```
    1.5 Set a context entry in kubeconfig
    ```shell
    kubectl config set-context daniel-context --cluster=minikube --user=daniel
    ```
    1.6 Test it
    ```shell
    kubectl config use-context daniel-context
    kubectl create ns ns-test
    will return error.
    ```

    apply this yaml file. (role-and-binding.yaml)
    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: default
      name: pod-reader
    rules:
    - apiGroups: [""]
      resources: ["pods"]
      verbs: ["get","watch","list"]

    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: read-pods
      namespace: default
    subjects:
    - kind: User # !!!!!!!
      name: daniel
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
    ```
    ```shell
    kubectl config use-context minikube
    kubectl apply -f role-and-binding.yaml
    kubectl config use-context daniel-context
    kubectl create ns ns-test
    will also return error.

    kubectl get pods
    will return success.
    ```
2. Group (RoleBinding is Group kind)
    2.1 Generate a key using OpenSSL
    ```shell
    openssl genrsa -out daniel.key 2048
    ```
    2.2 Generate a Client Sign Request, CN must match user, O must match group.
    ```shell
    openssl req -new -key daniel.key -out daniel.csr -subj "/CN=daniel/O=dev"
    ``` 
    2.3 Generate the certificate. (/etc/kubernetes/pki in production env.)
    ```shell
    openssl x509 -req -in daniel.csr -CA ~/.minikube/ca.crt -CAkey ~/.minikube/ca.key -CAcreateserial -out daniel.crt -days 500
    ```
    2.4 Set a user entry in kubeconfig
    ```shell
    kubectl config set-credentials daniel --client-certificate=daniel.crt --client-key=daniel.key
    ```
    2.5 Set a context entry in kubeconfig
    ```shell
    kubectl config set-context daniel-context --cluster=minikube --user=daniel
    ```
    2.6 Test it
    ```shell
    kubectl config use-context daniel-context
    kubectl create ns ns-test
    will return error.
    ```

    apply this yaml file. (role-and-binding.yaml)
    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: default
      name: pod-reader
    rules:
    - apiGroups: [""]
      resources: ["pods"]
      verbs: ["get","watch","list"]

    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: read-pods
      namespace: default
    subjects:
    - kind: Group # !!!!!!!
      name: dev
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
    ```
    ```shell
    kubectl config use-context minikube
    kubectl apply -f role-and-binding.yaml
    kubectl config use-context daniel-context
    kubectl create ns ns-test
    will also return error.

    kubectl get pods
    will return success.
    ```
3. ServiceAccount  (RoleBinding is ServiceAccount kind) [Kubernetes Role Based Access Control with Service Account](https://medium.com/rahasak/kubernetes-role-base-access-control-with-service-account-e4c65e3f25cc)
    3.1 Create namespace
    ```shell
    kubectl create namespace dev
    ```
    3.2 Create service account (service-account.yaml)
    ```yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: daniel
      namespace: dev
    ```
    
    ```shell
    kubectl apply -f service-account.yaml
    ```
    3.3 Create role and rolebinding (role-and-binding.yaml)
    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: dev
      name: pod-reader
    rules:
    - apiGroups: [""]
      resources: ["pods"]
      verbs: ["get","watch","list"]

    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: read-pods
      namespace: dev
    subjects:
    - kind: ServiceAccount # !!!!!!!
      name: daniel
      namespace: dev
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
    ```
    ```shell
    kubectl apply -f role-and-binding.yaml    
    ```
    3.4 Test it 
    create pod yaml (kubectl-pod.yaml)
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: kubectl-pod
      namespace: dev
    spec:
      containers:
      - name: kubectl
        image: bibinwilson/docker-kubectl:latest
      serviceAccountName: daniel
    ```
    ```shell
    kubectl apply -f kubectl-pod.yaml
    kubectl exec -it -ndev kubectl-pod -- /bin/bash

    root@kubectl-pod:/# kubectl get pods -n dev
    will return success

    root@kubectl-pod:/# kubectl get nodes
    will return error
    ```

- [How to issue a certificate for a user](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#normal-user)
- [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

### Use kuberadm to install a basic cluster

### Manage a highly-available Kubernetes cluster

### Provision underlying infrastructure to deploy a Kubernetes cluster

### Perform a version upgrade on a Kubernetes cluster using Kubeadm

### Implement etcd backup and restore
1. install etcdctl [Intsall etcdctl](https://k21academy.com/docker-kubernetes/etcd-backup-restore-in-k8s-step-by-step/)
2. find out kubelet config yaml and staticPodPath 
   /var/lib/kubelet/config.yaml
3. find out etcd ca, crt, key files path.
   /etc/kubernetes/manifests/etcd.yaml
4. backup
   ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/var/lib/minikube/certs/etcd/ca.crt --cert=/var/lib/minikube/certs/etcd/server.crt --key=/var/lib/minikube/certs/etcd/server.key snapshot save today.db
5. restart api-server
   move kube-apiserver.yaml out, then move back
6. delete etcd data dir in /etc/kubernetes/manifests/etcd.yaml   
7. restore 
   ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/var/lib/minikube/certs/etcd/ca.crt --cert=/var/lib/minikube/certs/etcd/server.crt --key=/var/lib/minikube/certs/etcd/server.key snapshot restore --data-dir=/var/lib/minikube/etcd today.db

- [Backing up an etcd cluster](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/#snapshot-using-etcdctl-options)
- [Restoring an etcd cluster](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/#restoring-an-etcd-cluster)


## Workload & Scheduling
### Understand deployments and how to perform rolling update and rollbacks
- [Creating a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment)
- [Updating a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment)
- [Rolling Back to Previous Revision](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-to-a-previous-revision)

### Use ConfigMaps and Secrets to configure applications
- [ConfigMaps and Pods](https://kubernetes.io/docs/concepts/configuration/configmap/#configmaps-and-pods)
- [Uses for Secret](https://kubernetes.io/docs/concepts/configuration/secret/#use-case-dotfiles-in-a-secret-volume)