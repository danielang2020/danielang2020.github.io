# Amazon Relational Database service

## What is Amazon RDS?
### Multi-AZ deployments
> Multi-AZ deployments can have one standby or two standby DB instances. When the deployment has one standby DB instance, it's called a Multi-AZ DB instance deployment. A Multi-AZ DB instance deployment has one standby DB instance that provides failover support, but doesn't serve read traffic. When the deployment has two standby DB instances, it's called a Multi-AZ DB cluster deployment. A Multi-AZ DB cluster deployment has standby DB instances that provide failover support and can also serve read traffic.  
#### Multi-AZ DB instance deployments
> In a Multi-AZ DB instance deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone.  

## Managing a DB instance
### Maintaining a DB instance
> Running a DB instance as a Multi-AZ deployment can further reduce the impact of a maintenance event, because Amazon RDS applies operating system updates by following these step:
>1. Perform maintenance on the standby.
>2. Promote the standby to primary.
>3. Perform maintenance on the old primary, which becomes the new standby.

> When you modify the database engine for your DB instance in a Multi-AZ deployment, then Amazon RDS upgrades both the primary and secondary DB instances at the same time. In this case, the database engine for the entire Multi-AZ deployment is shut down during the upgrade.  

### Working with read replicas
> You can use read replica promotion as a data recovery schema if the primary DB instance fails.

## Using RDS Proxy
### Planning where to use RDS Proxy
> AWS Lambda functions can also be good candidates for using a proxy. These functions make frequent short database connections that benefit from connection pooling offered by RDS Proxy.  

### RDS Proxy concepts and terminology
> You store the database credientials used by RDS Proxy in AWS Secret Manager. Each database user for the RDS DB instance or Aurora DB cluster accessed by a proxy must have a corresponding secret in Secrets Manager. You can also set up IAM authentication for users of RDS Proxy. By doing so, you can enforce IAM authentication for database access even if the database use native password authentication. We recommend using these security features instead of embedding database credientials in your application code.  

### Getting started with RDS Proxy
> For each proxy that you create, you first use the Secret Manager service to store sets of user name and password credentials. You create a separate Secret Manager secret for each database user account that the proxy connects to on the RDS instance or Aurora DB cluster.  

[Connecting to a database from AWS Lambda function](https://ahmedahamid.com/connecting-to-a-database-from-aws/)  

## Microsoft SQL Server on Amazon RDS
### Options for SQL Server
#### Transparent Data Encryption
> Amazon RDS supports using Transparent Data Encryption(TDE) to encrypt stored data on your DB instances running Microsoft SQL Server. TDE automatically encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.

## Oracle on Amazon RDS
### Options for Oracle
#### Transparent Data Encryption
> Amazon RDS supports Oracle Transparent Data Encryption(TED), a feature of the Oracle Advanced Security option available in Oracle Enterprise Edition. This feature automatically encrypts data before it is writted to storage and automatically decrypts data when the data is read from storage.

## Security
### Identity and access management
#### IAM database authentication
> Use IAM database authentication when your application requires fewer than 200 new IAM database authentication connections per second.  
> The database engines that work with Amazon RDS don't impose any limits on authentication attempts per second. However, when you use IAM database authentication, your application must generate an authentication token. Your application then use that token to connection to the DB instance. If you exceed the limit of maximum new connections per second, then the extra overhead of IAM database authentication can cause connection throttling.  
[Create an authentication token java demo](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_rds_code_examples.html)  
[DIFFERENT WAYS TO BE AUTHENTICATED IN AN RDS DATABASE](https://blog.spikeseed.cloud/rds-authentication/)
>```json
>{
>   "Sid": "VisualEditor1",
>   "Effect": "Allow",
>   "Action": "rds-db:connect",
>   "Resource": "arn:aws:rds-db:us-east-1:839823279171:dbuser:prx-0879811c832dabd07/admin"
>}
>```
> arn:aws:rds-db:{region}:{account-id}:dbuser:{DbiResourceId}/{db-user-name}
> region = us-east-1  
> account-id = 839823279171   
> DbiResourceId(rds proxy arn suffix) = prx-0879811c832dabd07  
> db-user-name(database username) = admin  

### Using Amazon RDS with Amazon VPC
#### Working with a DB instance in a VPC
> A DB subnet group is a collection of subnets(typically private) that you create in a VPC and that you then designate for your DB instances.   

> Each DB subnet group should have subnets in at least two Availability Zones in a given AWS Regions.  


