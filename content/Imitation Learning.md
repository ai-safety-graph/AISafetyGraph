# Imitation Learning

## Summary
 Imitation Learning is a machine learning approach where an agent learns to perform a task by observing demonstrations from an expert. Key aspects of imitation learning include:

1) Learning from demonstrations without explicit reward signals, often using behavioral cloning to directly map observations to actions. 

2) Dealing with distributional shift between the expert's and learner's policies, which can lead to compounding errors. Methods like DAgger address this by iteratively collecting data from both expert and novice policies.

3) Inverse reinforcement learning techniques that aim to recover the expert's underlying reward function. 

4) Adversarial approaches that frame imitation as a two-player game between policy and discriminator.

5) One-shot and few-shot learning methods that can imitate from very limited demonstrations.

6) Handling partially observable environments and extracting relevant features from raw sensory inputs like images. 

7) Addressing challenges like causal confusion, where spurious correlations in demonstrations can lead to poor generalization.

8) Combining imitation learning with reinforcement learning to exceed demonstrator performance in some cases.

Recent work has focused on sample-efficient algorithms, learning from suboptimal demonstrations, and scaling to complex real-world tasks. Overall, imitation learning provides a powerful paradigm for learning behaviors from human or expert demonstrations across robotics and other domains.
## Research Papers

- [[Adversarial Soft Advantage Fitting Imitation Learning without Policy Optimization]]
- [[Learning What To Do by Simulating the Past]]
- [[Making Efficient Use of Demonstrations to Solve Hard Exploration Problems]]
- [[IQ-Learn Inverse soft-Q Learning for Imitation]]
- [[Causal Confusion in Imitation Learning]]
- [[O2A One-shot Observational learning with Action vectors]]
- [[Replacing Rewards with Examples Example-Based Policy Search via Recursive Classification]]
- [[EnsembleDAgger A Bayesian Approach to Safe Imitation Learning]]
- [[Preventing Imitation Learning with Adversarial Policy Ensembles]]
- [[Better-than-Demonstrator Imitation Learning via Automatically-Ranked Demonstrations]]
- [[One-Shot Hierarchical Imitation Learning of Compound Visuomotor Tasks]]
- [[Imitating Latent Policies from Observation]]
- [[Discriminator-Actor-Critic Addressing Sample Inefficiency and Reward Bias in Adversarial Imitation Learning]]
- [[Offline Reinforcement Learning as One Big Sequence Modeling Problem]]
- [[VILD Variational Imitation Learning with Diverse-quality Demonstrations]]
- [[Reward Learning from Narrated Demonstrations]]
- [[Perceptual Values from Observation]]
- [[An Extensible Interactive Interface for Agent Design]]
- [[Multi-Agent Generative Adversarial Imitation Learning]]
- [[Auto-Encoding Variational Bayes]]
- [[What Matters in Learning from Offline Human Demonstrations for Robot Manipulation]]
