# Machine Learning Theory

## Summary
 Machine Learning Theory is undergoing a significant shift in understanding the fundamental principles that govern model performance and generalization. Recent research challenges the classical bias-variance trade-off, which traditionally suggested a U-shaped risk curve as model complexity increases. Instead, studies have revealed a "double descent" phenomenon, where model performance can improve beyond the point of interpolation, particularly in overparameterized models like neural networks. This behavior is characterized by a unimodal or bell-shaped variance curve, coupled with a monotonically decreasing bias, resulting in various risk curve shapes depending on the relative scales of bias and variance. Surprisingly, in some cases, increasing the number of samples can actually hurt performance in overparameterized linear regression. These findings have important implications for both the theory and practice of machine learning, prompting a reevaluation of classical analyses and highlighting the need for new frameworks to understand the behavior of modern machine learning models.
## Research Papers

- [[Reconciling modern machine learning practice and the bias-variance trade-off]]
- [[More Data Can Hurt for Linear Regression Sample-wise Double Descent]]
- [[Rethinking Bias-Variance Trade-off for Generalization of Neural Networks]]
