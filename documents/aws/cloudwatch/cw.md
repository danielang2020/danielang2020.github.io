# Amazon CloudWatch
## What is Amazon CloudWatch?
### Concepts
> Each metric data point must be associated with a time stamp. The time stamp can be up to two weeks in the past and up to two hours into the future. If you do not provide a time stamp, CloudWatch creates a time stamp for you based on the time the data point was received.  

## Dashboards
### Create a dashboard
> All dashboards are global. They are not Region-specific.

## Metrics
### Basic monitoring and detailed monitoring
> CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring.  
> Many AWS services offer basic monitoring by publishing a default set of metrics to CloudWatch with no charge to customers. By default, when you start using one of these AWS services, basic monitoring is automatically enabled.  
> Detailed monitoring is offered by only some services. It also incurs charges. To use it for an AWS service, you must choose to activate it.

### Publishing custom metrics
> High-resolution metrics can give you more immediate insight into your application's sub-minute activity. Keep in mind that every PutMetricData call for a custom metric is charged, so calling PutMetricData more often on a high-resolution metric can lead to higher charges.  

## Application Signals
### Use CloudWatch RUM
#### Viewing the Cloudwatch RUM dashboard
##### How CloudWatch RUM sets Apdex scores
> The Apdex score indicates the end users' level of satisfaction Scores range from 0(least satisfied) to 1(most satisfied). The scores are based on application performance only. Users are not asked to rate the application.

> Each individual Apdex score falls into one of three thresholds. Based on the Apdex threshold and actual application response time, there are three kinds of performance, as follows:
>- Satisfied - The actual application response time is less than or equal to the Apdex threshold. For CloudWatch RUM, this threshold is 2000 ms or less.
>- Tolerable - The actual application response time is greater than the Apdex threshold, but less than or equal to four times the Apdex threshold. For CloudWatch RUM, this range is 2000 - 8000 ms.
>- Frustrating - The actual application response time is greater than four times the Apdex threshold. For CloudWatch RUM, this range is over 8000 ms.

> The total 0 - 1 Apdex score is calculated using the following formula:
>```Apdex = (positive scores + tolerable scores / 2) / total scores * 100```
> OR
>```Apdex = (satisfactory + 0.5 × tolerable + 0 × frustrating) / total events```