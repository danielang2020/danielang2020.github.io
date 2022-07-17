# Financial Services Industry Lens
## Pillars of the Well-Architected Framework
### Security Pillar
#### Data Protection
##### Use envelope encryption with AWS KMS keys
> Envelope encryption is the practice of encrypting plaintext data with a data key, and then encrypting the data key under another key. Use KMS keys to generate, encrypt, and decrypt the data keys that you use outside of AWS KMS to encrypt your data. KMS keys are created in AWS KMS and never leave AWS KMS unencrypted.  

