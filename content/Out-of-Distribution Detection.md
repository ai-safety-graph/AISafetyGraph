# Out-of-Distribution Detection

## Summary
 Out-of-Distribution (OOD) detection is a critical area of research in AI alignment, focusing on enhancing the safe deployment of neural networks by identifying inputs that differ significantly from the training distribution. This task is crucial because models often produce overconfident predictions on OOD data, which can lead to erroneous and potentially dangerous outcomes in real-world applications. Recent approaches to address this challenge include ReAct, which reduces model overconfidence by analyzing internal activations, likelihood ratio methods that correct for confounding background statistics in deep generative models, and VOS, which synthesizes virtual outliers to regularize the model's decision boundary during training. These techniques aim to improve OOD detection performance across various domains, including image classification, object detection, and even genomic sequence analysis for bacteria identification. By developing more robust OOD detection methods, researchers seek to create AI systems that can reliably identify when they are operating outside their area of expertise, thus improving their safety and applicability in diverse real-world scenarios.
## Research Papers

- [[ReAct Out-of-distribution Detection With Rectified Activations]]
- [[Likelihood Ratios for Out-of-Distribution Detection]]
- [[VOS Learning What You Don't Know by Virtual Outlier Synthesis]]
