# Contrastive Learning

## Summary
 Contrastive learning is an unsupervised approach to visual representation learning that has shown significant progress in recent years. This method involves creating a dynamic dictionary of encodings and learning to distinguish between similar and dissimilar examples. Two notable implementations of this approach are Momentum Contrast (MoCo) and SimCLR. MoCo utilizes a queue-based dictionary and a moving-averaged encoder to build a large and consistent set of representations on-the-fly, while SimCLR introduces design improvements such as an MLP projection head and enhanced data augmentation. These techniques have demonstrated competitive performance on various computer vision tasks, often surpassing supervised pre-training methods. The success of contrastive learning suggests that the gap between unsupervised and supervised representation learning is narrowing, making state-of-the-art unsupervised learning more accessible and effective for downstream tasks.
## Research Papers

- [[Improved Baselines with Momentum Contrastive Learning]]
- [[Momentum Contrast for Unsupervised Visual Representation Learning]]
