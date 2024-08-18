# AWS Identity and Access Management
## Access management
### Policies and permissions
#### Permissions boundaries
> AWS supports permissions boundaries for IAM entities(users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries.  

#### Identity vs resource
> Identity-based policies are attached to an IAM user, group, or role. These policies let you specify what that identity can do(its permissions)  

> Resource-based policies are attached to resource. e.g. S3 bucket policy.

## Reference
### Policy reference
#### Policy evaluation logic
> An explicit deny in any of these policies overrides the allow.  

> If an action is allowed by an identity-based policy, a resource-based policy, or both, then AWS allows the action. An explicit deny in either of these policies overrides the allow.  

> An implicit denial occurs when there is no applicable Deny statement but also no applicable Allow statement. Because an IAM principal is denied access by default, they must be explicitly allowed to perform an action. Otherwise, they are implicitly deniel access.

> ![](img/flow.png)
