# Certified Kubernetes Administrator
## Cluster Architecture, Installation & Configuration
### Manage role based access control(RBAC)
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
### Use kuberadm to install a basic cluster
### Manage a highly-available Kubernetes cluster
### Provision underlying infrastructure to deploy a Kubernetes cluster
### Perform a version upgrade on a Kubernetes cluster using Kubeadm
### Implement etcd backup and restore
