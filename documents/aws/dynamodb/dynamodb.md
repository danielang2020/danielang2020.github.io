# Amazon DynamoDB
## What is Amazon DynamoDB?
### How it works
#### Supported data types and naming rules
> Attribute names must be at least one character long, and less than 64 KB in size. It is considered best practice to keep your attribute names as short as possible. This helps to reduce read request units consumed, as attribute names are included in metering of storage and throughput usage.  
#### Read consistency
> DynamoDB supports eventually consistent and strongly consistent reads.  
> When you request a strongly consistent read, DynamoDB returns a response with the most up-to-date data, reflecting the updates from all prior write operations that were successful. However, this consistency comes with some disadvantages.
#### Table classes
> DynamoDB offers two table classes designed to help you optimize for cost. The DyanmoDB Standard table class is the default, and is recommended for the vast majority of workloads. The DynamoDB Standard-Infrequent Access(DynamoDB Standard-IA) table class is optimized for tables where storage is the dominant cost.

## Working with DynamoDB
### Working with Tables
#### Working with Global Tables
> Amazon DynamoDB global tables provide a fully managed solution for deploying a multi-Region, multi-active database, without having to build and maintain your own replication solution.  

> Global tables provide automatic multi-active replication to AWS Regions worldwide.

### Working with read and write operations
#### DynamoDB API
##### Working with items
###### Expiring Items with Time to Live
> Amazon DynamoDB Time to Live(TTL) allows you to define a per-item timestamp to determine when an item is no longer needed. Shortly after the date and time of the specified timestamp, DynamoDB deletes the item from your table without consuming any write throughput. TTL is provided at no extra cost as a means to reduce stored data volumes by retaining only the items that remain current for your workload's needs.

#### PartiQL query language
> To ensure that a SELECT statement does not result in a full table scan, the WHERE clause condition must specific a partition key. Use the equality or IN operator.  

### Working with transactions
> Amazon DynamoDB transactions simplify the developer experience of making coordinated, all-or-nothing changes to mulitple items both within and across tables. Transactions provide atomicity, consistency, isolation, and durability(ACID) in DynamoDB, helping you to maintain data correctness in your applications.  

> You can use the DynamoDB transactional read and write APIs to manage complex business workflows that require adding, updating, or deleting multiple items as a single, all-or-nothing operation.  

### Working with Streams
#### Working with DynamoDB Streams
> Stream records are organized into groups, or shards. Each shard acts as a container for mulitple stream records, and contains information required for accessing and iterating through these records. The stream records within a shard are removed automatically after 24 hour.  

> Because shards have a lineage(parent and children), an application must always process a parent and before it processes a child shard.  



## In-memory acceleration with DAX
### Managing DAX clusters
> DAX maintains Item cache and Query cache for data that it reads from DynamoDB.  

> The default TTL for each of these caches is 5 minutes.  

