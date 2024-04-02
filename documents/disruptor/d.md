# 3. Design of the LMAX Disruptor
## 3.2 Teasing Apart the Concerns
> On most processors there is a very high cost for the remainder calculation on the sequence number, which determines the slot in the ring. This cost can be greatly reduced by making the ring size a power of 2. A bit mask of size minus one can be used to perform the remainder operation efficiently.

