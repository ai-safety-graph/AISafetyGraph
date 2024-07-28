# Hyperparameter Optimization

## Summary
 Hyperparameter optimization is a crucial aspect of machine learning that can be formulated as a bilevel optimization problem. This approach involves finding the optimal hyperparameters that yield the best model parameters on the training set. Recent advancements in this field include the development of Self-Tuning Networks (STNs), which use structured best-response functions to adapt regularization hyperparameters for neural networks during training. These networks employ a gradient-based optimization algorithm that alternates between approximating the best-response around current hyperparameters and optimizing them using the approximate function. This method allows for the tuning of discrete hyperparameters, data augmentation hyperparameters, and dropout probabilities without requiring differentiation of the training loss with respect to the hyperparameters. STNs have shown superior performance compared to other hyperparameter optimization methods, particularly in large-scale deep learning problems, and can discover hyperparameter schedules that outperform fixed hyperparameter values.
## Research Papers

- [[Self-Tuning Networks Bilevel Optimization of Hyperparameters using Structured Best-Response Functions]]
