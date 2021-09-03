# [Hazelcast 4.2](https://docs.hazelcast.com/imdg/latest/index.html)
## Overview
### What is Hazelcast IMDG?
> Hazelcast IMDG is peer-to-peer; there is no single point of failure in a Hazelcast IMDG; each member in the cluster is configured to be functionally the same. They all store equal amount of data and do equal amounts of processing. You can embed Hazelcast IMDG in your existing application or use it in client and server mode where your application is a client to Hazelcast members.

> Data is resilient to member failure. Data backups are distributed across the cluster. This is a big benefit when a member in the cluster crashed as data is not lost. Hazelcast keeps the backup of each data entry on mutilple members. On a member failure, the data is restored from the backup and the cluster continues to operate without downtime.

> It is designed to scale up to hundreds of members and thousands of clients. When you add new members, they automatically discover the cluster and linearly increate both the memory and processing capacity. The members maintain a TCP connection between each other and all communication is performed through this layer. Each cluster member is configured to be the same in terms of functionality. The oldest member(the first member created in the cluster) automatically performs the data assignment to cluster members. If the oldest member dies, the second oldest member takes over.

### Data Partitioning
> The momery segments in Hazelcast IMDG are called partitions. The partitions are distributed equally among the members of the cluster. Hazelcast also creates backups of these partitions which are also distributed in the cluster.

> By default, Hazelcast creates a single copy/replica of each partitions. You can configure hazelcast so that each partition can have multipler replicas. One of these replicas is called "primary" and others are called "backups". The cluster member which owns the "primary" replica of a partition is called the "partition owner". When you read or write a particular data entry, you transparently talk to the partition owner that contains the data entry.

> Thanks to the consistent hashing algorithm, only the minimum amount of partitions are moved to scale out Hazelcast.

> Hazelcast offers lite members. These members do not own any partition. Lite members are intended for use in computationally-heavy task executions and listener registrations. Althrough they do not own any partitions, they can access partitions that are owned by other members in the cluster.

> Rolling upgrade for patch versions is supported in the open source, Pro, or Enterprise editions of hazelcast IMDG.

## Configuration Options
> Hazelcast looks for static configuration options in the following order:
>  1. *Config* object provided by programmatic configuration
>  2. *hazelcast.config* system property
>  3. *hazelcast.xml* declarative configuration file in the working directory
>  4. *hazelcast.xml* declarative configuration file on the classpath
>  5. *hazelcast.yaml(or .yml)* declarative configuration file in the working directory
>  6. *hazelcast.yaml* declarative configuration file on the classpath

> If Hazelcast does not find any of these configuration options, it loads the default configuration file(*hazelcast-default.xml*),which comes with your Hazelcast package.

## Setting Up Clusters
### Discovery Mechanisms
> Please note that, after a cluster is formed, communication between cluster members is always via TCP/IP, regardless of the discovery mechanism used.

> By default, Hazelcast tries to automatically detect the applicable discovery mechanism based on the runtime enviroment. Note that using Auto Detection is not recommended for production. Note also that if Hazelcast finds no applicable discovery mechanism, then if falls back to Multicast.