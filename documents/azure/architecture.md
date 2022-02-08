# [Application Architecture Guide](https://docs.microsoft.com/en-us/azure/architecture/guide/)

## Azure application architecture fundamentals
| Traditional on-premises | Modern cloud |
| ----------- | ----------- |
| Monolithic | Decomposed |
| Designed for predictable scalability | Designed for elastic scale |
| Relational database | Polyglot persistence(mix of storage technologies) |
| Synchronized processing| Asynchronous processing |
| Design to avoid failure(MTBF) | Design for failure(MTTR) |
| Occasional large updates| Frequent small updates |
| Maunal management| Automated self-management |
| Snowflake servers| Immutable infrastructure |
[MTBF & MTTR](https://www.atlassian.com/incident-management/kpis/common-metrics)

### Architecture styles
#### Overview
> N-tier is a traditional architecture for enterprise applications. Dependencies are managed by dividing the application into layers that perform logical functions, such as presentation, business logic, and data access. N-tier is a natural fit for migrating existing applications that already use a layered architecture. For this reason, N-tier is most often seen in infrastructure as a service(IaaS) solutions, or application that use a mix of IaaS and managed services.

> For a purely PaaS solution, consider a Web-Queue-Worker architecture. In this style, the application has a web front end that handles HTTP requests and a back-end worker that performs CPU-intensive tasks or long-running operations. The front end communicates to the worker through an asynchronous message queue.

> A microservices application is composed of many small, independent services. Each service implements a single business capability. Services are loosely coupled, communicating through API contracts.

> Event-Driven Architectures use a publish-subscribe(pub-sub) model, where producers publish events, and consumers subscribe to them. The producers are independent from the consumers, and consumers are independent from each other. Consider an event-driven architecture for applications that ingest and process a large volume of data with very low latency, such as IoT solutions. The style is also useful when different subsystems must perform different types of processing on the same event data.

> Big data divides a very large dataset into chunks, performing parallel processing across the entire set, for analysis and reporting. Big Compute, also called high-performance compute(HPC), makes parallel computations across a large number(thousands) of cores. Domains include simulations, modeling, and 3-D rendering.

| Architecture style | Dependency management | Domain type|
| ----------- | ----------- | ----------- |
| N-tier | Horizontal tiers divided by subnet | Traditional business domain. Frequently of updates is low. |
| Web-Queue-Worker | Front and backend jobs, decoupled by async messaging | Relatively simple domain with some resource intensive tasks.|
| Miscroservices | Vertially(functionally) decomposed services that call each other through APIs | Complicated domain. Frequent updates. |
| Event-driven architecture | Producer/consumer. Independent view per sub-system. | IoT and real-time systems |
| Big data | Divide a huge dataset into small chunks. Parallel processing on local datasets. | Batch and real-time data analysis. Predictive analysis using ML. |
| Big compute | Data allocation to thousand of cores. | Compute intensive domains such as simulation. |

> Here are some of the types of challenges to consider when selecting an architecture style:
>- Complexity
>- Asynchronous messaging and eventual consistency
>- Inter-service communication
>- Manageability

#### Big compute
> When to use this architecture
>- Computationally intensive operations such as simulation and number crunching.
>- Simulations that are computationally intensive and must be split across CPUs in mulitple computers(10 - 1000s).
>- Simulations that require too much memory for one computer, and must be split across multiple computers.
>- Long-running computations that would take too long to complete on a single computer.
>- Smaller computations that must be run 100s or 1000s of times, such as Monte Carlo simulation.

