# Computer Network
## 1 Computer Networks and the Internet
### 1.3.1 Packet Switch
> To send a message from a source end system to a destination end system, the source breaks long messages into smaller chunks of data known as **packets**. Between source and destination, each packet travels through communication links and **packets switches**(for which there are two predominant types, **routers** and **link-layer switches**).

#### Store-and-Forward Transmission
> Store-and-forward transmission means that the packet switch must receive the entire packet before it can begin to transmit the first bit of the packet onto the outbound link.
> ![](img/111.png)

#### Queuing Delays and Packet Loss
> Each packet switch has multiple links attached to it. For each attached link, the packet switch has an **output buffer**(also called an **output queue**), which stores packets that the router is about to send into that link. If an arriving packet needs to be transmitted onto a linke but finds the link busy with the transmission of another packet, the arriving packet must wait in the output buffer. Thus, in addition to the store-and-forward delays, packets suffer output buffer **queuing delays**. These delays are variable and depend on the level of congestion in the network. Since the amount of buffer space is finite, an arriving packet may find that the buffer is completely full with other packets waiting for transmission. In this case, **packet loss** will occur-either the arriving packet or one of the already-queued packets will be dropped.
> ![](img/112.png)

52