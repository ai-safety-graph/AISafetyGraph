# Debugging Neural Networks

## Summary
 Debugging neural networks is a challenging task due to their complexity and opacity. To address this, researchers have developed automated testing techniques specifically tailored for neural networks, focusing on uncovering rare input errors. One such approach is coverage-guided fuzzing (CGF), which uses random mutations of inputs guided by a coverage metric to satisfy user-defined constraints. Fast approximate nearest neighbor algorithms can provide this coverage metric. CGF has been applied to various goals, including detecting numerical errors in trained networks, identifying disagreements between neural networks and their quantized versions, and exposing undesirable behavior in character-level language models. To facilitate the implementation of these techniques, an open-source library called TensorFuzz has been released, providing researchers and practitioners with tools to improve the debugging and testing of neural networks.
## Research Papers

- [[TensorFuzz Debugging Neural Networks with Coverage-Guided Fuzzing]]
