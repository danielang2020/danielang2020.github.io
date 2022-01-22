# [High Performance Computing Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/welcome.html)

## Definitions
> Some vocabulary of the AWS Cloud may differ from common HPC terminology. For example, HPC users may refer to a server as a "node" while AWS refers to a virtual server as an "instance." When HPC users commonly speak of "jobs," AWS refers to them as "workloads."

## Gerenal Design Principles
> The Well-Architectured Framework proposal a set of general design principles to facilitate good design in the cloud with high-performance computing:
>- Dynamic architectures: Avoid frozen, static architectures and cost estimates that use a steady-state model. Your architecture must be dynamic: growing and shrinking to match your demands for HPC over time. Match your architecture design and cost analysis explicitly to the natural cycles of HPC activity.
>- Align the procurement model to the workload: AWS makes a range of compute procurement models available for the various HPC usage patterns.
>- Start from the data: Before you begin designing your architecture, you must have a clear picture of the data. Consider data origin, size, velocity, and updates. A holistic optimization of performance and cost focuses on compute and includes data considerations. 
>- Automation to simplify architectural experimentation: Automation through code allows you to create and replicate your systems at low cost and avoid the expense of manual effort.
>- Enable collaboration: HPC work often occurs in a collaborative context, sometimes spanning many countries around the world. Beyond immediate collaboration, methods and results are often shared with the wider HPC and scientific community. It's important to consider in advance which tools, code, and data may be shared, and with whom.
>- Use cloud-native designs: Users can rely on a managed service, like AWS Batch, or serverless computing, like AWS Lambda, to manage the underlying infrastructure. Consider not using a traditional cluster scheduler, and instead use a scheduler only if your workload request it.
>- Test real-world workloads
>- Balance time-to-results and cost reduction: Analyze performance using the most meaningful parameters: time and cost.

## Scenarios
> HPC is divided into two categories based on the degree of interaction between the concurrently running parallel processes: loosely coupled and tightly coupled workloads. Loosely coupled HPC cases are those where the multiple or parallel processes don't strongly interact with each other in the course of the entire simulation. Tightly coupled HPC case are those where the parallel processes are simultaneously running and regularly exchanging information between each other at each iteration or step of the simulation.

> With loosely coupled workloads, the completion of an entire calculation or simulation often requires hundreds to millions of parallel processes. These processes occur in any order and at any speed through the course of the simulation. This offer flexibility on the computing infrastructure required for loosely coupled simulations.

> Tightly coupled workloads have processes that regularly exchange information at each iteration of the simulation. Typically, these tightly coupled simulations run on a homogenous cluster. The total core or processor count can range from tens, to thousands, and occasionally to hundreds of thousands if the infrastructure allows. The interactions of the processes during the simulation place extra demands on the infrastructure, such as the compute nodes and network inftrastructure.

> Consider the following fundamentals for both scenarios when selecting an HPC infrastructure on AWS:
>- Network: Network requirements can range from cases with low requirements, such as loosely coupled applications with minimal communication traffic, to tightly coupled and massively parallel applications that require a performant network with large bandwith and low latency.
>- Storage: HPC calculation use, create, and move data in unique ways. Storage infrastructure must support these requirements during each step of the calculation. Input data is frequently stored on startup, more data is created and stored while running, and output data is moved to a reservoir location upon run completion. Factors to be considerated include data size, media type, transfer speeds, shared access, and storage properties.
>- Compute: The EC2 instance type defines the hardware capabilities available for your HPC workload. Hardware capabilities include the processor type, core frequency, processor features, memory-to-core ratio, and network performance. On AWS, an instance is considered to be the same as an HPC node.


### Loosely Coupled Scenarios
> A loosely coupled workload entails the processing of a large number of smaller jobs. Generally, the smaller job runs on one node, either consuming one process or multiple processes with shared memory parallelization for parallelization with that node.

> The loss of one node or job in a loosely coupled workload usually doesn't delay the entire calculation. The lost work can be picked up later or omitted altogether. The nodes involved in the calculation can vary in specification and power.

### Tightly Coupled Scenarios
> Tightly coupled applications consist of parallel processes that are dependent on each other to carry out the calculation. Unlike a loosely coupled computation, all processes of a tightly coupled simulation iterate together and require communication with one another. An iteration is defined as one step of the overall simulation. Tightly coupled calculations rely on tens to thousands of processes or cores over one to millions of iteration. The failure of one node usually leads to the failure of the entire calculation. To mitigate the risk of complete failure, application-level checkpointing regularly occurs during a computation to allow for the restarting of a simulation from a known state.