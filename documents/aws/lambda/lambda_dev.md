# AWS Lambda(Developer Guid)
## Lambda foundations
### Concepts
> An event is a JSON-formatted document that contains data for a Lambda function to process.
## Invoking functions
### Synchronous invocation
> When you invoke a function synchronously, Lambda runs the function and waits for a response. When the function completes, Lambda returns the response from the function's code with additional data, such as the version of the function that was invoked.

### Asynchronous invocation
> Several AWS services, such as Amazon Simple Storage Service(Amazon S3) and Amazon Simple Notification Service, invoke functions asynchronously to process events. When you invoke a function asynchronously, you don't wait for a response from the function code. 

> As an alternative to an on-failure destination, you can configure your function with a dead-letter queue to save discard events for further processing.  
## Working with other services
### API Gateway
> For a custom integration, the event is the body of the request. For a proxy integration, the event has a defined structure.
### CloudFront(Lambda@Edge)
> Lambda@Edge lets you run Node.js and Python Lambda functions to customize content that CloudFront delivers, executing the functions in AWS locations closer to the viewer. The functions run in response to CloudFront events, without provisioning or managing servers. You can use Lambda functions to change CloudFront requests and responses at the following points:
>1. After CloudFront receives a request from a viewer(view request)
>2. Before CloudFront forwards the request to the origin(origin request)
>3. After CloudFront receives the response from the origin(origin response)
>4. Before CloudFront forwards the response to the viewer(viewer response)

## Lambda Quotas
> Function timeout is 900 seconds(15 Minutes)
