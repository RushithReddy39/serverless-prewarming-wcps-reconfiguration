# serverless-prewarming-wcps-reconfiguration
Multi-Level Optimization of Serverless Workflow Performance: ML-Based Pre-Warming, Weighted Critical Path Scheduling, and Lookahead Resource Reconfiguration

Project Overview:

This project, titled “Multi-Level Optimization of Serverless Workflow Performance: ML-Based Pre-Warming, Weighted Critical Path Scheduling, and Lookahead Resource Reconfiguration,” addresses key bottlenecks in serverless computing. While serverless systems provide scalability and reduced operational overhead, they face challenges such as cold-start delays, inefficient workflow scheduling, and suboptimal memory allocation. These issues impact both performance and cost-effectiveness, especially in complex workflows. Our project introduces a multi-level optimization framework designed to tackle these limitations.

Key Contributions:

The framework integrates three intelligent strategies to enhance serverless performance. First, a machine learning-based pre-warming predictor uses linear regression to forecast function invocation trends, significantly reducing cold-start latency. Second, a weighted critical path scheduling algorithm improves workflow execution by balancing runtime and cost, leading to smarter path selection. Third, a multi-step lookahead resource reconfiguration mechanism dynamically tunes memory allocation, ensuring cost efficiency without breaching Service Level Objectives (SLOs).

Results:

Extensive simulations demonstrated substantial improvements over baseline methods. The ML-based pre-warming model improved prediction accuracy by nearly 30%, reducing cold-start impact. Weighted critical path scheduling lowered workflow execution cost by approximately 11% while maintaining runtime performance. The lookahead resource reconfiguration strategy achieved 4–5% savings in memory-based costs without violating SLO constraints. Collectively, these optimizations enhanced container utilization, minimized overhead, and improved overall responsiveness.

Broader Impact:

Beyond technical improvements, this project aligns with UN Sustainable Development Goal 9 (Industry, Innovation, and Infrastructure) by promoting sustainable and efficient cloud computing practices. By intelligently managing compute and memory resources, the framework reduces wastage, improves infrastructure scalability, and supports environmentally responsible technology deployment. This makes the work relevant not only for academic research but also for real-world serverless applications in industries such as IoT, finance, and healthcare.
