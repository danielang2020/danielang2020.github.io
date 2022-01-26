# [Kubernetes](https://kubernetes.io/docs/home/)

## Concepts
### Overview
#### Kubernetes Components
> A Kubernetes cluster consist of a set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.

> The worker nodes host the Pods that are the components of the application workload. The control plane manages the worker nodes and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault-tolerance and high availability.
> ![](img/kcc.png)

##### Control Plane Components
> The control plane's components make global decisions about the cluster, as well as detecting and responding to cluster events.

###### kube-apiserver
> The API server is a components of the Kubernetes control plane that expose the Kubernetes API. The API server is the front end for the Kubernetes control plane.

###### etcd
> Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.

###### kube-scheduler
> Control plane component that watches for newly created Pods with no assigned node, and selects a node for them to run on.

> Factors taken into account for scheduling decisions include: individual and collective resource requirements, hardware/software/policy constraints, affinity and anti-affinity specifications, data locality, inter-workload interference, and deadlines.

###### kube-controller-manager
> Control plane component that runs controller processes.
>- Node controller: Responsible for noticing and responding when nodes go down.
>- Job controller: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion.
>- Endpoint controller: Populates the Endpoints object(that is, joins Services & Pods).
>- Service Account & Token controllers: Create default accounts and API access tokens for new namespaces.

###### cloud-controller-manager
> A Kubernetes contorl plane component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your provider's API, and seperates out the componenets that interact with that cloud platform from components that only interact with your cluster.
>- Node controller: For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding.
>- Route controller: For setting up routes in the underlying cloud infrastructure.
>- Service controller: For creating, updating and deleting cloud provider load balancers.

##### Node Components
> Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment.

###### kubelet
> An agent that runs on each node in the cluster. It makes sure that containers are running in a Pod.

> The Kubelet doesn't manage containers which were not created by Kubernetes.

###### kube-proxy
> kube-proxy is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept.

> kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster.

###### Container runtime
> The container runtime is the software that is responsible for running containers.

##### Addons
> Addons use Kubernetes resources to implement cluster features. Because these are providing cluster-level features, namespaced resources for addons belong within the kube-system namespace.

###### DNS
> While the other addons are not strictly required, all Kubernetes clusters should have cluster DNS.

> Containers started by Kubernetes automatically include this DNS server in their DNS searches.

#### The Kubernetes API
> The core of Kubernetes' control plane is the API server. The API server exposes an HTTP API that lets end users, different parts of your cluster, and external components communicate with one another.

> The Kubernetes API lets you query and manipulate the state of API objects in Kubernetes.

> Most operations can be performed through the kubectl command-line interface or other command-line tools, such as kubeadm, which in turn use the API. However, you can also access the API directly using REST calls.

#### Working with Kubernetes Objects
##### Understanding Kubernetes Objects
> A Kubernetes object is a "record of intent" -- once you create the object, the Kubernetes system will constantly work to ensure that object exists. By creating an object, you're efficiently telling the Kubernetes system what your cluster's workload to look like; this is your cluster's desire state.

> Almost every Kubernetes object includes two nested object fields that govern the object's configuration: the object spec and the object status. For objects that have a spec, you have to set this when you create the object, providing a description of the characteristics you want the resource to have: its desire state.

> The status describes the current state of the object, supplied and updated by the Kubernetes system and its components. The Kubernetes control plane continually and actively manages every object's actual state to match the desired state you supplied.

> When you create an object in Kubernetes, you must provide the object spec that describes its desired state, as well as some basic information about the object. When you use the Kubernetes API to create the object, that API request must include that information as JSON in the request body. Most often, you provide the information to kubectl in a .yaml file. kubectl converts the information to JSON when making the API request.

> In the .yaml file for the Kubernetes object you want to create, you'll need to set values for the following fields:
>- apiVersion - Which version of the Kubernetes API you're using to create this object
>- kind - What kind of object you want to create
>- metadata - Data that helps uniquely identify the object, including a name string, UID, and optional namespace
>- spec -  What state you desire for the object

##### Kubernetes Object Management
> ![](img/mt.png)

###### Imperative commands
>- When using imperative commands, a user operates directly on live objects in a cluster. The user provides operations to the kubectl command as arguments or flags.
>```
> kubectl create deployment nginx --image nginx
>```

###### Imperative object configuration
> In imperative object configuration, the kubectl command speicifies the operation(create, replace, etc.), optional flags and at least one file name. The file speicified must contain a full definition of the object in YAML or JSON format.
>```
> kubectl create -f nginx.yaml
>```

###### Declarative object configuration
> When using declarative object configuration, a user operates on object configuration files stored locally, however the user does not define the operations to be taken on the files. Create, update, and delete operations are automatically detected per-object by kubectl. This enables working on directories, where different operations might be needed for different objects.
>```
> kubectl diff -f configs/
> kubectl diff -R -f configs/
>```

##### Object Names and IDs
> Each object in your cluster has a Name that is unique for that type of resource. Every Kubernetes object also has a UID that is unique across your whole cluster.

###### Names
> A client-provided string that refers to an object in a resource URL, such as /api/v1/pods/some-name .

##### Namespace
> In Kubernetes, namespaces provides a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects(e.g. Deployments, Services, etc) and not for cluster-wide objects(e.g. StorageClass, Nodes, PersistentVolumes, etc).

> Namespaces are intended for use in environments with many users spread across multiple teams, or projects. For clusters with a few to ten of users, you should not need to create or think about namespaces at all. Start using namespaces when you need the features they provide.

> Namespaces provide a scope for names. Names of resources need to be unique within a namespace, but not across namespaces. Namespaces cannot be nested inside one another and each Kubernetes resource can only be in one namespace.

> Namespaces are a way to divide cluster resources between  multiple users.

> It's not necessary to use multiple namespaces to seperate slightly different resources, such as different versions of the same software: use labels to distinguish resources within the same namespace.

> Kubernetes starts with four initial namespaces:
>- default The default namespace for objects with no other namespace    
>- kube-system The namespace for objects created by the Kubernetes system
>- kube-public This namespace is created automatically and is readable by all users. This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a requirement.
>- kube-node-lease This namespace holds Lease objects associated with each node. Node leases allow the kubelet to send heartbeats so that the control plane can detect node failure.

> When you create a Service, it creates a corresponding DNS entry. This entry is of the form <service-name>.<namespace-name>.svc.cluster.local, which means that if a container only uses <service-name>, it will resolve to the service which is local to a namespace. This is useful for using the same configuration across multiple namespaces such as Development, Staging and Production.

> Most Kubernetes resources are in some namespaces. However namespace resources are not themselves in a namespace. And low-level resources, such as nodes and persistentVolumes, are not in any namespace.

##### Labels and Selectors
> Labels are key/value pairs that are attached to objects, such as pods. Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, but do not directly imply sematics to the core system. Labels can be used to organize and to select subsets of objects. Labels can be attached to objects at creation time and subsequently added and modified at any time. Each object can have a set of key/value labels defined. Each key must be unique for a given object.

> Valid label keys have two segments: an optional prefix and name, seperated by a slash(/). The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels seperated by dots(.). If the prefix is omitted, the label key is presumed to be private to the user. Automated system components which add labels to end-user objects must specify a prefix.

> Via a label selector, the client/user can  identify a set of objects. The label selector is the core grouping primitive in Kubernetes. The Api currently supports two types of selectors: equality-based and set-based.
>- Equality- or inequality-based requirements allow filtering by label keys and values. Matching objects must satisfy all of the specified label contraints, though they may have additional labels as well. Three kinds of operators are admitted =,==,!=.
>- Set-based label requirements allow filtering keys according to a set of values. Three kinds of operators are supported: in,notin and exists(only the key identifier). 

> Set-based requirements can be mixed with equality-based requirements.

##### Annotations
> You can use either labels or annotations to attach metadata to Kubernetes objects. Labels can be used to select objects and to find collections of objects that satisfy certain conditions. In contrast, annotations are not used to identify and select objects.

> Valid annotation keys have two segments: an optional prefix and name, seperated by a slash(/). The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels seperated by dots(.). If the prefix is omitted, the annotation key is presumed to be private to the user. Automated system components which add annotations to end-user objects must specify a prefix.

##### Field Selectors
> Field selectors let you select Kubernetes resources based on the value of one or more resource fields.

> You can use the =, ==, and != operators with field selectors.

##### Finalizers
> Finalizers are namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion.

> You can use finalizers to control garbage collection of resources by alerting controllers to perform specific cleanup tasks before deleting the target resource.

### Cluster Architecture
#### Nodes
> Kubernetes runs your workload by placing containers into Pods to run on Nodes. A node may be a virtual or physical machine, depending on the cluster. Each node is managed by the control plane and contains the services necessary to run Pods.

> The componenets on a node include the kubelet, a container runtime, and the kube-proxy.

> There are two main ways to have Nodes added to the API server:
>1. The kubelet on a node self-registers to the control plane
>2. You(or another human user) manually add a Node object

> A Node's status contains the following information:
>- Address
>- Conditions
>- Capacity and Allocatable
>>- The fields in the capacity block indicate the total amount of resources that a Node has. 
>>- The allocatable block indicates the amount of resources on a Node that is available to be consumed by normal Pods.
>- Info

> Heartbeats, sent by Kubernetes nodes, help your cluster determine the availability of each node, and to take action when failure are detected.

> The node controller is a Kubernetes control plane component that manages various aspects of nodes.

> The node controller has multiple roles in a node's life. The first is assigning a CIDR block to the node when it is registered. The second is keeping the node controller's internal list of nodes up to date with the cloud provider's list of available machines. The third is monitoring the node's health.

> Nodes that self register report their capacity during registration. If you manually add a Node, then you need to set the node's capacity information when you add it.

> The Kubernetes scheduler ensures that there are enough resources for all the Pods on a Node. The scheduler checks that the sum of the requests of containers on the node is no greater than the node's capacity. That sum of requests includes managed by kubelet, but excludes any containers started directly by the container runtime. and also excludes any processes running outside of the kubelet's control.

#### Control Plane-Node Communication
> Kubernetes has a "hub-and-spoke" API pattern. All API usage from nodes(or the pods they run) terminates at the apiserver. None of the other control plane components are designed to expose remote services.

> There are two primary communication paths from the control plane(apiserver) to the nodes. The first is from the apiserver to the kubelet which runs on each node in the cluster. The second is from the apiserver to any node, pod, or service through the apiserver's proxy functionality.

#### Controllers
> In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state.

> A controller tracks at least one Kubernetes resource type. These objects have a spec field that represents the desired state. The controller(s) for that resource are responsible for making the current state come closer to that desired state.

> Kubernetes takes a cloud-native view of systems, and is able to handle constant change. Your cluster could be changing at any point as work happens and control loops automatically fix failures. This means that, potentially, your cluster never reaches a stable state. As long as the controllers for your cluster are running and able to make useful changes, it doesn't matter if the overall state is stable or not.

> As a tenet of its design, Kubernetes uses lots of controllers that each manage a particular aspect of cluster state. Most commonly, a particular control loop(controller) uses one kind of resource as its desired state, and has a different kind of resource that it manages to make that desired state happen.

> Kubernetes comes with a set of built-in controllers that run inside the kube-controller-manager. These built-in controllers provide important core behaviors.

#### Container Runtime Interface(CRI)
> The CRI is a plugin interface which enables the kubelet to use a wide variety of container runtimes, without having a need to recompile the cluster components.

> The Container Runtime Interface(CRI) is the main protocol for the communication between the kubelet and Container Runtime.

> The Kubernetes Container Runtime Interface defines the main gRPC protocol for the communication between the cluster components kubelete and container runtime.

#### Garbage Collection
> Many objects in Kubernetes link to each other through owner references. Owner references tell the control plane which objects are dependent on others. Kubernetes uses owner references to give the control plane, and other API clients, the opportunity to clean up related resources before deleting an object. In most cases, Kubernetes manages owner references automatically.

> Kubernetes checks for and deletes objects that no longer have owner references. When you delete an object, you can control whether Kubernetes deletes the object's dependents automatically, in a process called cascading deletion. There are two types of cascading deletion, as follows:
>- Foreground cascading deletion
>> The object itself cann't be deleted before all the objects that it owns are deleted.
>- Background cascading deletion
>> The object itself is delted, after which the GC deletes the objects that it owned.

> When Kubernetes deletes an owner object, the dependents left behind are called orphan objects. By default, Kubernetes deletes dependent objects.



