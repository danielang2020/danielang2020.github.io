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
>- Foreground cascading deletion: The object itself cann't be deleted before all the objects that it owns are deleted.
>- Background cascading deletion: The object itself is deleted, after which the GC deletes the objects that it owned.

> By default, Kubernetes uses background cascading deletion unless you manually use foreground deletion or choose to orphan the dependent objects.

> When Kubernetes deletes an owner object, the dependents left behind are called orphan objects. By default, Kubernetes deletes dependent objects.

> The kubelet performs garbage collection on unused images every five minutes and on unused containers every minutes. You should avoid using external garbage collection tools, as these can break the kubelet behavior and remove containers that should exist.

> Kubernetes manages the lifecycle of all images through its images manager, which is part of the kubelet, with the cooperation of cadvisor. 

> Disk usage above the configured HighThresholdPercent value triggers garbage collection, which deletes images in order based on the last time they were used, starting with the oldest first. The kubelet deletes images until disk usage reaches the LowThresholdPercent value.

### Containers
> Kubernetes supports container runtimes such as containerd, CRI-O, and any other implementation of the Kubernetes CRI.

#### Images
> A container image represents binary data that encapsulates an application and all its software dependencies. Container images are executable software bundles that can run standalone and that make very well defined assumptions about their runtime environment.

> You typically create a container image of your application and push it to a registry before referring to it in a Pod.

> If you don't specify a registry hostname, Kubernetes assumes that you mean the Docker public registry.

> If you don't specify a tag, Kubernetes assumes you mean the tag latest.

> You should avoid using the :latest tag when deploying containers in production as it is harder to track which version of the image is running and more difficult to roll back properly.

> To make sure the Pod always uses the same version of a container image, you can specify the image's digest; replace image-name:tag with image-name@digest.

> When using image tags, if the image registry were to change the code that the tag on that image represents, you might end up with a mix of Pods running the old and new code. An image digest uniquely identifies a specific version of the image, so Kubernetes runs the same code every time it starts a container with that image name and digest specified. Specifying an image fixes the code that you run so that a change at the registry cann't lead to that mix of versions.

> Pre-pulled images can be used to preload certain images for speed or as an alternative to authenticating to a private registry.

> Specifying imagePullSecrets on a Pod is the recommended approach to run containers based on images in private registers.

#### Container environment
> The Pod name and namespace are available as environment variables through the downward API.

> User defined environment variables from the Pod definition are also available to the Containers, as are any environment variables specified statically in the Docker image.

#### Container Lifecycle Hooks
> There are two hooks that are exposed to Containers:
>- PostStart: This hook is executed immediately after a container is created. However, there is no guarantee that the hook will execute before the container ENTRYPOINT.
>- PreStop: This hook is called immediately before a container is terminated due to an API request or management event such as a liveness/startup probe failure, preemption, resource contention and others. The Pod's termination grace period countdown begins before the PreStop hook is executed, so regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period.

> Hook handler calls are synchronous within the context of the Pod containing the Container. This means that for a PostStart hook, the Container ENTRYPOINT and hook fire asynchronously. However, if the hook takes too long to run or hangs, the Container cannot reaching a running state.
> PreStop hooks are not executed asynchronously from the signal to stop the Containers; the hook must complete its execution before the TERM signal can be sent. If a PreStop hook hangs during execution, the Pod's phase will be Terminating and remain there until the Pod is killed after its terminationGracePeriodSeconds expires.

> If either a PostStart or PreStop hook fails, it kills the Container.

> Users should make their hook handlers as lightweight as possible. There are cases, however, when long running commands make sense, such as when saving state prior to stopping a Container.

> Hook delivery is intended to be at least once, which means that a hook may be called multiple times for any given event. It's up to the hook implementation to handle this correctly.

### Workloads
> A workload is an application running on Kubernetes. Whether your workload is a single component or several that work together, on Kubernetes you run it inside a set of pods. In Kubernetes, a Pod represents a set of running containers on your cluster.

> To make life considerably easier, you don't need to manage each Pod directly. Instead, you can use workload resources that manage a set of pods on your behalf. These resources configure controllers that make sure the right number of the right kind of pod are running, to match the state you specified.

> Kubernetes provides several built-in workload resources:
>- Deployment and ReplicaSet: Deployement is a good fit for managing a stateless application workload on your cluster, where any Pod in the Deployment is interchangable and can be replaced if needed.
>- StatefulSet: Lets you run one or more related Pods that do track state somehow.
>- DaemonSet: Defines Pods that provide node-local facilities. These might be fundamental to the operation of your cluster, such as a networking helper tool, or be part of an add-on.
>- Job and CronJob: Defines tasks that run to completion and then stop. Jobs represent one-off task, whereas CronJob recur according to a schedule.

#### Pods
[Eight Ways to Create a Pod](https://www.cyberark.com/resources/threat-research-blog/eight-ways-to-create-a-pod)

> Pods are the smallest deployable units of computing that you can create and manage in Kubernetes.

> A Pod is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-localed and co-scheduled, and run in a shared context. A Pod models an application-specific "logical host": it contains one or more application containers which are relatively tightly coupled.

> Usually you don't need to create Pods directly, even singleton Pods. Instead, create them using workload resources such as Deployment or Job. If your Pods need to track state, consider the StatefulSet resource.

> Pods in a Kubernetes cluster are used in two main ways:
>- Pods that run a single container. The "one-container-Pod" model is the most common Kubernetes use cases; in this case, you can think of a Pod as a wrapper around a single container; Kubernetes manages Pods rather than managing the containers directly.
>- Pods that run multiple containers that need to work together. A Pod can encapsulate an appliation composed of mulitple co-located containers that are tightly coupled and need to share resources. Those co-located containers form a single cohesive unit of service. The Pod wraps these containers, storage resources, and an ephemeral network identify together as a single unit.

> Each Pod is meant to run a single instance of a given application. If you want to scale your application horizontally, you should use multiple Pods, one for each instance. In Kubernetes, this is typically referred to as replication. Replicated Pods are usually created and managed as a group by a workload resource and its controller.

> Pods are designed to support multiple cooperating processes(as containers) that form a cohesive unit of service. The containers in a Pod are automatically co-located and co-scheduled on the same physical or virtual machine in the cluster. The containers can share resources and dependencies, communicate with one another, and coordinate when and how they are terminated.

> Pods are designed as relatively ephemeral, disposable entities. When a Pod gets created(directly by you, or indirectly by a controller), the new Pod is scheduled to run on a Node in your cluster. The Pod remains on that Node until the Pod finished execution, the Pod object is deleted, the Pod is evicted for lack of resources, or the Node fails.

> Controllers for workload resources create Pods from a pod template and manage those Pods on your behalf.

> PodTemplates are specifications for creating Pods, and are included in workload resources such as Deployments, Jobs, and DaemonSets.

> Each controller for a workload resource uses the PodTemplate inside the workload object to make actual Pods. The PodTemplate is part of the desired state of whatever workload resource you used to run your app.

> Modifying the pod template or switching to a new pod template has no direct effect on the Pods that already exist. If you change the pod template for a workload resource, that resource needs to create replacement Pods that use the updated template. For example, the StatefulSet controller ensures that the running Pods match the current pod template for each StatefulSet object. If you edit the StatefulSet to change its pod template, the StatefulSet starts to create new Pods based on the updated template. Eventually, all of the old Pods are replaced with new Pods, and the update is complete.

> On Nodes, the kubelet does not directly observe or manage any of the details around pod templates and updates; those details are abstracted away. That abstraction and separation of concerns simplifies system semantics, and makes it feasible to extend the cluster's behavior without changing existing code.

> When the Pod template for a workload resource is changed, the controller creates new Pods based on the updated template instead of updating or patching the existing Pods.

> Pods enable data sharing and communication among their constituent containers.
>- Storage in Pods: A Pod can specify a set of shared storage volumes. All containers in the Pod can access the shared volumes, allowing those containers to share data. Volumes also allow persistent data in a Pod to survive in case one of the containers within needs to be restarted.
>- Pod networking: Each Pod is assigned a unique IP address for each address family. Every container in a Pod shares the network namespace, including the IP address and network ports. Inside a Pod, the containers that belong to the Pod can communicate with one another using localhost. When containers in a Pod communicate with entities outside the Pod, they must coordinate how they use the shared network resources(such as ports). The containers in a Pod can communicate with each other using standard inter-process communication like SystemV semaphores or POSIX shared memory. Containers in different Pods have distinct IP addresses and can not communicate by IPC without special configuration. Containers that want to interact with a container running in a different Pod can use IP networking to communicate.

> Static Pods are managed directly by the kubelet daemon on a specific node, without the API server observing them. Whereas most Pods are managed by the control plane, for static Pods, the kubelet directly supervises each static Pod(and restarts it if it fails).

> Static Pods are always bound to one Kubelet on a specify node. The main use for static Pods is to run a self-hosted control plane: in other words, using the kubelet to supervise the individual control plane components.

> The kubelet automatically tries to create a mirror Pod on the Kubernetes API server for each static Pod. This means that the Pods running on a node are visible on the API server, but cannot be controlled from there.

##### Pod Lifecycle
> Pods follow a defined lifecycle, starting in the Pending phase, moving through Running if at least one of its primary containers starts OK, and then through either the Succeeded or Failed phases depending on whether any container in the Pod terminated in failure.

> Whilst a Pod is running, the kubelet is able to restart containers to handle some kind of faults. Within a Pod, Kubernetes tracks different container states and determines what action to take to make the Pod healthy again.

> In the Kubernetes API, Pods have both a specification and an actual status. The status for a Pod object consists of a set of Pod conditions. You can also inject custom readiness information into the condition data for Pod, if that is useful to your application.

> Pods are only scheduled once in their lifetime. Once a Pod is scheduled(assigned) to a Node, the Pod runs on that Node until it stops or is terminated.

> If a Node dies, the Pods scheduled to that node are scheduled for deletion after a timeout period.

> Pods do not, by themselves, self-heal. If a Pod is scheduled to a node that then fails, the Pod is deleted; likewise, a Pod won't survive an eviction due to a lack of resources or Node maintenance. Kubernetes uses a higher-level abstraction, called a controller, that handles the work of managing the relatively disposable Pod instances.

> A given Pod(as defined by a UID) is never "rescheduled" to a different node; instead, that Pod can be replaced by a new, near-identical Pod, with even the same name if desired, but with a different UID.

> When something is said to have the same lifetime as a Pod, such as volume, that means that the thing exist as long as that specific Pod(with that exact UID) exist. If that Pod is deleted for any reason, and even if an identical replacement is created, the related thing is also destroyed and created a new.

> If a node dies or is disconnected from the rest of the cluster, Kubernetes applies a policy for setting the phase of all Pods on the lost node to Failed.

> Once the scheduler assigns a Pod to a Node, the kubelet starts creating containers for that Pod using a container runtime. There are three possible container states: Waiting, Running, and Terminated.

> The restartPolicy applies to all containers in the Pod. restartPolicy only refers to restarts of the containers by the kubelet on the same node. After containers in a Pod exit, the kubelet restarts them with an exponential back-off delay(10s, 20s, 40s, ...), that is capped at five minutes. Once a container has executed for 10 minutes without any problems, the kubelet resets the restart backoff timer for that container.

> A Pod has a PodStatus, which has an array of PodConditions through which the Pod has or has not passed:
>- PodScheduled
>- ContainersReady
>- Initialized
>- Ready

> There are four different ways to check a container using a probe. Each probe must define exactly one of these four mechanisms:
>- exec: Executes a specified command inside the container. The diagnostic is considered successful if the command exits with a status code of 0.
>- grpc: Performs a remote procedure call using gRPC The target should implement gRPC health checks. 
>- httpGet: Perform an HTTP Get request against the Pod's IP address on a specified port and path.
>- tcpSocket: Performs a TCP check against the Pod's IP address on a specified port.

> Each probe has one of three results:
>- Success
>- Failure
>- Unknown

>- The kubelet can optionally perform and react to three kinds of probes on running containers:
>- livenessProbe: Indicates whether the container is running.
>- readinessProbe: Indicates whether the container is ready to respond to requests.
>- startupProbe: Indicates whether the application within the container is started.

> When you request deletion of a Pod, the cluster records and tracks the intended grace period before the Pod is allowed to be forcefully killed. With that forceful shutdown tracking in place, the kubelet attempt graceful shutdown. Typically, the container runtime sends a TERM signal to the main process in each container. Once the grace period has expired, the KILL signal is sent to any remaining processes, and the Pod is then deleted from the API Server. If the kubelet or the container runtime's management service is restarted while waiting for processes to terminate, the cluster retires from the start including the full original grace period.

> When a force deletion is performed, the API server doesn't wait for confirmation from the kubelet that the Pod has been terminated on the node it was running on. It removes the Pod in the API immediately so a new Pod can be created with the same name. On the node, Pods that are set to terminate immediately will still be given a small grace period before being force killed.

> For failed Pods, the API objects remain in the cluster's API until a human or controller process explicitly removes them. The control plane cleans up terminated Pods, when the number of Pods exceeds the configured threshold. This avoids a resource leak as Pods are created and terminated over time.

##### Init Containers
> Init containers that run before app containers in a Pod. Init containers can contain utilities or setup scripts not present in an app image.

> If a Pod's init container fails, the kubelet repeatedly restarts that init container until it succeeds. However, if the Pod has a restartPolicy of Never, and an init container fails during startup of that Pod, Kubernetes treats the overall Pod as failed.

> If you specify multiple init containers for a Pod, kubelet runs each init container sequentially. Each init container must succeed before the next can run. When all of the init containers have run to completion, kubelet initializes the application containers for the Pod and runs them as usual.

> During Pod startup, the kubelet delays running init containers until the networking and storage are ready. Then the kubelet runs the Pod's init containers in the order they appear in the Pod's spec.

> A Pod cannot be Ready until all init containers have succeeded. The ports on an init container are not aggregated under a Service. A Pod that is initializing is in the Pending state but should have a condition Initialized set to false.

> If the Pod restarts, or is restarted, all init containers must execute again.

> Changes to the init container spec are limited to the container image field. Altering an init container image field is equivalent to restarting the Pod.

> Because init containers can be restarted, retires, or re-executed, init container code should be idempotent. In particular, code that writes to files on EmptyDirs should be prepared for the possibility that an output file already exists.

> The Pod will not be restarted when the init container image is changed, or the init container completion record has been lost due to garbage collection.

##### Pod Topology Spread Constraints
> You can use topology spread constraints to control how Pods are spread across your cluster among failure-domains such as region, zones, nodes, and other user-defined topology domains. This can help to achieve high availability as well as efficient resource utilization.

##### Disruptions
> Pods do not disappear until someone(a person or a controller) destroys them, or there is an unavoidable hardware or system software error. We call these unavoidable cases involuntary disruption to an application.

> We call other cases voluntary disruptions. These include both actions initiated by the application owner and those initiated by a Cluster Administrator.

##### Ephemeral Containers
> A special type of container that runs temporarily in an existing Pod to accomplish user-inititated actions such as troubleshooting. You use ephemeral containers to inspect services rather than to build applications.

#### Workload Resources
##### Deployments
> You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

> The pod-template-hash label is added by the Deployment controller to every ReplicaSet that a Deployment creates or adopts. Do not change this label.

> A Deployment's rollout is triggered if and only if the Deployment's Pod template is changed, for example if the labels or container images of the template are updated. Other updates, such as scaling the Deployment, do not trigger a rollout.

> Deployment ensures that only a certain number of Pods are down while they are being updated. By default, it ensures that at least 75% of the desired number of Pods are up(25% max unavailable). <br/>
> Deployment also ensures that only a certain number of Pods are created above the desired number of Pods. By default, it ensures that at most 125% of the desired number of Pods are up(25% max surge).<br/>
> For example, if you look at the above Deployment closely, you will see that it first created a new Pod, then deleted some old Pods, and created new ones. It does not kill old Pods until a sufficient number of new Pods have come up, and does not create new Pods until a sufficient number of old Pods have been killed.

> If you update a Deployment while an existing rollout is in progress, the Deployment creates a new ReplicaSet as per the update and start scaling that up, and rolls over the ReplicaSet that it was scaling up previously - it will add it to its list of old ReplicaSets and start scaling it down.

> It is generally discouraged to make label selector updates and it is suggested to plan your selectors up front. In any case, if you need to perform a label selector update, exercise great caution and make sure you have grasped all of the implications.

> Kubernetes marks a Deployment as progressing when one of the following tasks is performed:
>- The Deployment creates a new ReplicaSet.
>- The Deployment is scaling up its newest ReplicaSet.
>- The Deployment is scaling down its oldest ReplicaSet(s).
>- New Pods become ready or available.

> Kubernetes marks a Deployment as complete when it has the following characteristics:
>- All of the replicas associated with the Deployment have been updated to the lastest version you've specified, meaning any updates you've requested have been completed.
>- All of the replicas associated with the Deployment are available.
>- No old replicas for the Deployment are running.

> Your Deployment may get stuck trying to deploy its newest ReplicaSet without ever completing.
>- Insufficient quota
>- Readiness probe failures
>- Image pull errors
>- Insufficient permissions
>- Limit ranges
>- Application runtime misconfiguration

##### ReplicaSet
> A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often used to guarantee the availability of a specified number of identical Pods.

> A ReplicaSet is defined with fields, including a selector that specifies how to identify Pods it can acquire, a number or replicas indicating how many Pods it should be maintaining, and a pod template specifying the data of new Pods it should create to meet the number of replicas crtieria. A ReplicaSet then fullfills its purpose by creating and deleting Pods as needed to reach the desired number. When a ReplicaSet needs to create new Pods, it uses its Pod template.

> A Deployment is a high-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features. Therefore, we recommend using Deployment instead of directly using ReplicaSets, unless you require custom update orchestration or don't require updates at all.


