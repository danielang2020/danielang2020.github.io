# Amazon Simple Queue Service
## How Amazon SQS works
### FIFO queues
#### High throughput for FIFO queues
##### partitions and data distribution
> Amazon SQS stores FIFO queue data in partitions. A partition is an allocation of storage for a queue that is automatically replicated across multiple Availability Zones within an AWS Region.

### Dead-letter queues
> The redrive policy specifies the source queue, the dead-letter queue, and the conditions under which Amazon SQS moves messages from the former to latter if the consumer of the source queue fails to process a message a specified number of times.

### Visibility timeout
> When a consumer receives and processes a message from a queue, the message remains in the queue. Amazon SQS doesn't automatically delete the message. Because Amazon SQS is a distributed system, there's no guarantee that the consumer actually receives the message. Thus, the consumer must delete the message fromt he queue after receiving and processing it.  
> Immediately after a message is received, it remains in the queue. To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout, a period of time during which Amazon SQS prevents other consumers from receiving and processing the message.
> ![](img/vt.png)

> When you receive a message from a queue and begin to process it, the visibility timeout for the queue may be insufficient. You can shorten or extend a message's visibility by specifying a new timeout value using the ChangeMessageVisibility action.

> The visibility timeout begins when Amazon SQS returns a message. During this time, the consumer processes and deletes the message. However, if the consumer fails before deleting the message and your system doesn't call DeleteMessage action for that message before the visibility timeout expires, the message becomes visible to other consumers and the message is received again. If a message must be received only once, your consumer should delete it with in the duration on the visibility timeout.  