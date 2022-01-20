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