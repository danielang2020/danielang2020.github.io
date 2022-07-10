# Amazon CloudFront
## What is Amazon CloudFront
### CloudFront pricing 
#### Choosing the price class for a CloudFront distribution
> By default, CloudFront responds to requests based only on performance. Objects are served from the edge location that has the lowest latency for the viewer. If you’re willing to accept potentially higher latency for viewers in some geographic regions in return for lower cost, you can choose a price class that doesn’t include all geographic regions. Some viewers, especially those in geographic regions that are not in your price class, might see higher latency than if your content was served from all CloudFront edge locations. For example, if you choose Price Class 100, viewers in India might experience higher latency than if you choose Price Class 200.

## Getting started
### Getting started with a secure static website
> You can get started with Amazon CloudFront by using the solution described in this topic to create a secure static website for your domain name. A static website uses only static files - like HTML, CSS, Javascript, images, and videos - and doesn't need servers or server-side processing.  

## Configuring secure access and restricting access to content
### Restricting content with signed URLs and signed cookies
#### Choosing between signed URLs and signed cookies
> CloudFront signed URLs and signed cookies provide the same basic functionality: they allow you to control who can access your content.

### Restricting access to Amazon S3 content
> To restrict access to content that you serve from Amazon S3 buckets, follow these steps:
>1. Create a special CloudFront user called an origin access identity(OAI) and associate it with your distribution.
>2. Configure your S3 bucket permissions so that CloudFront can use the OAI to access the files in your bucket and serve them to your users. Make sure that users can't use a direct URL to the S3 bucket to access a file there.  
### Geographically restricting content
> You can use geographic restrictions, sometimes known as geo blocking, to prevent users in specific geographic locations from accessing content that you're distributing through a CloudFront distribution.  

## Customizing with edge functions
### Customizing with CloudFront Functions
> With CloudFront Functions in Amazon CloudFront, you can write lightweight functions in Javascript for high-scale, latency-sensitive CDN customizations. Your functions can manipulate the requests and responses that flow through CloudFront, perform basic authentication and authorization, generate HTTP responses at the edge, and more.