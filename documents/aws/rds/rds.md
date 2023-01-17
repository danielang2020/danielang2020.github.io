# Amazon Relational Database service

## What is Amazon RDS?
### Multi-AZ deployments
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

## Microsoft SQL Server on Amazon RDS
### Options for SQL Server
#### Transparent Data Encryption
> Amazon RDS supports using Transparent Data Encryption(TDE) to encrypt stored data on your DB instances running Microsoft SQL Server. TDE automatically encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.

## Oracle on Amazon RDS
### Options for Oracle
#### Transparent Data Encryption
> Amazon RDS supports Oracle Transparent Data Encryption(TED), a feature of the Oracle Advanced Security option available in Oracle Enterprise Edition. This feature automatically encrypts data before it is writted to storage and automatically decrypts data when the data is read from storage.



