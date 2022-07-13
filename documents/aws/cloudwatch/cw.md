# Amazon CloudWatch
## What is Amazon CloudWatch?
### Concepts
> Each metric data point must be associated with a time stamp. The time stamp can be up to two weeks in the past and up to two hours into the future. If you do not provide a time stamp, CloudWatch creates a time stamp for you based on the time the data point was received.  

## Using dashboards
### Create a dashboard
> All dashboards are global. They are not Region-specific.

## Using metrics
### Basic monitoring and detailed monitoring
> CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring.  
> Many AWS services offer basic monitoring by publishing a default set of metrics to CloudWatch with no charge to customers. By default, when you start using one of these AWS services, basic monitoring is automatically enabled.  
> Detailed monitoring is offered by only some services. It also incurs charges. To use it for an AWS service, you must choose to activate it.

### Publishing custom metrics
> High-resolution metrics can give you more immediate insight into your application's sub-minute activity. Keep in mind that every PutMetricData call for a custom metric is charged, so calling PutMetricData more often on a high-resolution metric can lead to higher charges.  