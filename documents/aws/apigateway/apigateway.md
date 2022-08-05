# Amazon API Gateway
## Working with REST APIs
### Develop
#### Access control
##### Use Lambda authorizers
> A Lambda authorizer is useful if you want to implement a custom authorization schema that uses a bearer token authentication strategy such as OAuth or SAML, or that uses request parameters to determine the caller's identity.

### Publish
#### Deploying a REST API
> Every time you upate an API, you must redeploy the API to an existing stage or to a new stage. Updating an API includes modifying routes, methods, integrations, authorizers, and anything else other than stage settings.  

#### Set up a stage
> A stage is a named reference to a deployment, which is a snapshot of the API.

### Optimize
#### Cache settings
> You can enable API caching in Amazon API Gateway to cache your endpoint's responses. With cahcing, you can reduce the number of calls made to your endpoint and also improve the latency of requests to your API.

### Distribute
#### Usage plans
> A usage plan specifies who can access one or more deployed API stages and methods - and optionally sets the target request rate to start throttling requests. The plan uses API keys to identify API clients and who can access the associated API stages for each key.  



