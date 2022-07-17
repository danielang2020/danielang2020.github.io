# AWS Key Management Service
## Managing keys
### Rotating keys
> You might prefer to rotate keys manually so you can control the rotation frequently. It's also a good solution for KMS keys that are not eligible for automatic key rotation, sush as asymmetric KMS keys, HMAC KMS keys in custom key stores and KMS keys with imported key material.

## Special-purpose keys
### Multi-Region keys
> Use an AWS KMS multi-region key only when you need one. Multi-Region keys provide a flexible and scalable solution for workloads that move encrypted data between AWS Regions or need cross-Region access. Consider a multi-Region key if you must share, move, or back up protected data across Regions or need to create identical digital signatures of applications operating in different Regions.

