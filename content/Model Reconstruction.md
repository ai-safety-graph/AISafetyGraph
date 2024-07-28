# Model Reconstruction

## Summary
 Model Reconstruction, as explored in the provided abstract, refers to the process of reverse-engineering or learning a machine learning model's structure and parameters using only its explanations or gradient information. The research demonstrates that gradient-based explanations can inadvertently reveal the underlying model, creating a tension between model transparency and proprietary protection. The paper presents both theoretical and practical approaches to this problem. Theoretically, it introduces an algorithm capable of learning a two-layer ReLU network using only gradient queries, with query efficiency independent of input dimension. Practically, it offers heuristics for model reconstruction that are significantly more efficient than methods relying on prediction interfaces alone. This work highlights the power of gradients as a learning primitive and raises important considerations for the balance between model explainability and confidentiality in AI systems.
## Research Papers

- [[Model Reconstruction from Model Explanations]]
