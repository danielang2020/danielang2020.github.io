# [Hazelcast 5.0](https://docs.hazelcast.com/hazelcast/latest)
## Get Started
### hazelcast overview
#### Architecture Overview
> The fundamental key components of Hazelcast are as follows:
>- A member is the computational and data storage unit in Hazelcast. Typically it is a JVM.
>- A Hazelcast cluster is a set of members communicating with each other. Members which run Hazelcast automatically discover one another and form a cluster at runtime.
>- Partitions are the memory segments that store portions of data. They are distributed evenly among the available cluster members. Then can contain hundreds or thousands of data entries each, depending on the memory capacity of your system. Hazelcast also automatically creates backups of these partitions which are also distributed in the cluster. This makes Hazelcast resilient to data loss.

