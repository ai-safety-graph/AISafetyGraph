# Planning from Pixels

## Summary
 Planning from Pixels refers to the approach of using visual input (images) to learn and predict environmental dynamics for planning and decision-making in reinforcement learning tasks. This subtopic addresses the challenge of creating accurate dynamics models from image data, which has traditionally been difficult due to the complexity of visual information. The Deep Planning Network (PlaNet) is a notable example of this approach, combining a latent dynamics model with online planning in latent space. PlaNet uses both deterministic and stochastic transition components, along with a multi-step variational inference objective called latent overshooting, to accurately predict rewards over multiple time steps. This method has shown success in solving complex continuous control tasks with challenging aspects such as contact dynamics, partial observability, and sparse rewards, using fewer episodes and achieving performance comparable to or better than model-free algorithms.
## Research Papers

- [[Learning Latent Dynamics for Planning from Pixels]]
