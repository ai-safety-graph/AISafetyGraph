# Network Pruning

## Summary
 Network pruning is a technique used to reduce the complexity of neural networks by removing unnecessary connections or neurons. Recent research has focused on pruning at or near initialization, with the lottery ticket hypothesis suggesting that dense networks contain small, trainable subnetworks. Studies have shown that pruning very early in training (0.1% to 7% through) can yield better results than pruning at initialization for deeper networks. The stability of these pruned subnetworks to SGD noise has been identified as a key factor in their performance. Neuron Shapley has emerged as a new framework for quantifying individual neuron contributions, enabling the identification of critical filters for various tasks. Additionally, research has explored the importance of weight values, signs, and masking in pruned networks, leading to insights such as the discovery of "Supermasks" that can significantly improve performance when applied to randomly initialized networks.
## Research Papers

- [[Stabilizing the Lottery Ticket Hypothesis]]
- [[Linear Mode Connectivity and the Lottery Ticket Hypothesis]]
- [[Neuron Shapley Discovering the Responsible Neurons]]
- [[Deconstructing Lottery Tickets Zeros, Signs, and the Supermask]]
