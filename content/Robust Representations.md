# Robust Representations

## Summary
 Robust representations in AI aim to create models that can generalize well across different domains and maintain performance under distribution shifts. This subtopic focuses on developing techniques to reduce the model's reliance on superficial statistics of training data and instead capture more semantic, distribution-agnostic signals. Two key approaches in this area include: (1) using methods like the gray-level co-occurrence matrix (GLCM) to identify and project out superficial features, thereby encouraging the model to learn more robust representations, and (2) employing test-time adaptation and augmentation strategies, such as minimizing the entropy of the model's average output distribution across various augmentations of a test input. These techniques aim to improve out-of-sample performance and achieve state-of-the-art results on distribution shift benchmarks, demonstrating the potential for creating more robust AI systems that can handle unexpected perturbations and domain changes.
## Research Papers

- [[Learning Robust Representations by Projecting Superficial Statistics Out]]
- [[MEMO Test Time Robustness via Adaptation and Augmentation]]
