# Shared Model Governance

## Summary
 Shared Model Governance through model splitting is proposed as a scalable alternative to current techniques like homomorphic encryption and secure multiparty computation, which are impractical for large neural networks due to computational and communication overhead. The approach involves dividing a deep learning model among multiple parties, and its security is evaluated through the "model completion problem." This problem assesses how difficult it is to recover a model's original performance given a subset of its parameters and either the full training dataset or an environment simulator. The study empirically investigates this concept in both supervised learning and reinforcement learning scenarios, revealing that the difficulty of model completion is influenced more by the type and location of missing parameters than their quantity. Additionally, the research finds that model completion is more challenging in reinforcement learning due to the absence of trained agent trajectories. These findings suggest that model splitting could be a viable method for shared model governance in scenarios where training is resource-intensive.
## Research Papers

- [[Scaling shared model governance via model splitting]]
