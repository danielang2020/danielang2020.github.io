# AWS Lambda(Operator Guide)
## Application design
### Choosing and managing runtimes in Lambda functions
#### Runtimes and performance
> Different runtimes have different performance profiles in on-demand compute services like Lambda. For example, both Python and Node.js are both fast to initialize and offer reasonable overall performance. Java is much slower to initialize but can be extremely fast once running. Go can be extremely performant for both start-up execution. If performance is critical to your application, then profiling and comparing runtime performance is an important first step before coding applications.

## Performance optimization
### Memory and computing power
> The amount of memory also determines the amount of virtual CPU available to a function. Adding more memory proportionally increases the amount of CPU, inreasing the overall computational power available. If a function is CPU-, network- or memory-bound, then changing the memory setting can dramatically improve its performance.

