# Self-Supervised Exploration

## Summary
 Self-Supervised Exploration is an innovative approach in reinforcement learning that aims to improve sample efficiency and generalization across tasks. This method, exemplified by the Plan2Explore algorithm, focuses on enabling agents to explore their environment efficiently without relying on task-specific rewards. Instead of retrospectively evaluating the novelty of observations, Plan2Explore uses planning to actively seek out expected future novelty during exploration. This proactive approach allows the agent to build a comprehensive world model that can be quickly adapted to various downstream tasks, even those unknown during the initial exploration phase. The self-supervised nature of this exploration technique enables the agent to perform well on multiple tasks with minimal or no additional training, potentially outperforming methods that rely on task-specific interactions and approaching the performance of oracle systems with access to reward information.
## Research Papers

- [[Planning to Explore via Self-Supervised World Models]]
