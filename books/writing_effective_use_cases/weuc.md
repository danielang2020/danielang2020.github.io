# Writing Effective Use Cases
## PRELIMINARIES
### 2. What is a use case?  
> A use case is a description of the possible sequences of interactions between the system under discussion and its external actors, related to a particular goal.  

### 3. The System-in-use story
> A system-in-use story(or user story) is a situated example of the use case in operation - a single, highly specific, example story of an actor using the system.  

### 5. Precision, Harness, Tolerance
> Precision is not the same as accuracy. Saying pi is 4.1415926 is speaking it with great precision, but simply wrong, inaccurate. Saying pi is "about 3" is not very precise - there aren't very many digits showing - but it is, at least, accurate for as much as was said.  

> I divide the energy of writing use cases into four stages, matching levels of precision, according to the amount of energy required and the value of pausing after each stage:  
>1. Actors & Goals. 
>2. Main Success Scenarios.  
>3. Failing conditions.  
>4. Failure handling.  

> On a large, life-critical project, such an atomic power plant, it may be appropriate to use a hardened form, a larger, fancier template for the use cases.  

## Base Concept
### 1. Actors & stakeholders
> An actor is anything having behavior. A more correct word would be "role". A "role" would mean the role that a particular person is playing when they use the system. 

### 8. Precondition, Success End Condition, Failure Protection
> Precondition: Sometimes the use case will only be triggered if the user is already logged on and validated, or some other condition is known to be true. Writing some condition of the world into the Precondition means that that condition is known to be true, and need not be checked again.  

> Success End Condition: The Success End Condition states what interests of the stakeholders have been satisfied at the end of the use case.

> Failure Protection Condition: There are dozens of ways to fail, and often little in common between them. However, sometimes there are some special interests that must be protected under failure conditions, and those get written in the Failure Protection Condition. Most typical is that the system has logged how far it got before failure, so that the transaction can be recovered, and the interests of the stakeholders protected.  

