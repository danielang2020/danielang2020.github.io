# service, pod and DNS

## debug pod
```shell
kubectl run tmp01 --rm -it --image=tutum/dnsutils -- /bin/bash
```

## Deployment with regular service and headless service
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
  labels:
    app: server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: regular-svc
spec:
  selector:
    app: web
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: headless-svc
spec:
  clusterIP: None 
  selector:
    app: web
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```
### regular service DNS result
```shell
root@tmp01:/# nslookup regular-svc
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	regular-svc.default.svc.cluster.local
Address: 10.101.16.246
```
### headless service DNS result
```shell
root@tmp01:/# nslookup headless-svc
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	headless-svc.default.svc.cluster.local
Address: 10.244.0.148
Name:	headless-svc.default.svc.cluster.local
Address: 10.244.2.13
Name:	headless-svc.default.svc.cluster.local
Address: 10.244.1.87
```

## StatefulSet with regular service and headless service
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: sfs-app
  labels:
    app: sfs-server
spec:
  serviceName: sfs-headless-svc # <= Don't forget!!
  replicas: 3
  selector:
    matchLabels:
      app: sfs-web
  template:
    metadata:
      labels:
        app: sfs-web
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: sfs-regular-svc
spec:
  selector:
    app: sfs-web
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: sfs-headless-svc
spec:
  clusterIP: None 
  selector:
    app: sfs-web
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```
### regular service DNS result
```shell
root@tmp01:/# nslookup sfs-regular-svc
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	sfs-regular-svc.default.svc.cluster.local
Address: 10.101.86.176
```

### headless service DNS result
```shell
root@tmp01:/# nslookup sfs-headless-svc
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	sfs-headless-svc.default.svc.cluster.local
Address: 10.244.1.34
Name:	sfs-headless-svc.default.svc.cluster.local
Address: 10.244.2.231
Name:	sfs-headless-svc.default.svc.cluster.local
Address: 10.244.0.241
```
## statefulset pod DNS result
```shell
root@tmp01:/# nslookup sfs-app-0.sfs-headless-svc
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	sfs-app-0.sfs-headless-svc.default.svc.cluster.local
Address: 10.244.2.231

root@tmp01:/# nslookup sfs-app-1.sfs-headless-svc
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	sfs-app-1.sfs-headless-svc.default.svc.cluster.local
Address: 10.244.0.241

root@tmp01:/# nslookup sfs-app-2.sfs-headless-svc
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	sfs-app-2.sfs-headless-svc.default.svc.cluster.local
Address: 10.244.1.34
```