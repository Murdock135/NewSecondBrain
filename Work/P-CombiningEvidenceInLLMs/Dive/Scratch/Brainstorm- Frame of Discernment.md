The following essay attempts to synthesize my thought process on how to arrive at a frame of discernment for LLMs.
 
---
# Towards an evidence theory
LLMs produce distributions over tokens, which do not neatly correspond to discrete hypotheses in a power set. These distributions are, for lack of a better causal notion, *influenced by* prior interactions (such as in fine tuning), prompts (the current input) and hidden training data. Should DST (Dempster Shafer Theory) or an adaptation of the theory be applied to LLMs, we must first realize that the so called sources of information; the language models, are not independent unless their hidden training data are *different*. Now we arrive at the first problem. **What does it mean for hidden training data to be different?** Could it be the difference between distributions over a high dimensional 'vocabulary space'? May be. An even deeper question is - **Should the sources (LLMs) actually be *independent*?**. This question is probably best answered by studying [mixture of experts](https://arxiv.org/pdf/2503.07137), which is an *ensembling technique*. There are several 'ad-hoc' methods for merging or aggregating generations such as majority vote, confidence-weighted averaging (TODO: cite). But they are not explainable techniques and do not express uncertainty. 
## Takeaways
1. How to define *independence* between language models?
2. What does it mean for training data to be different?
3. *Should* the training data be different?

---
# Towards combination rules (token level)

Since there could be *similarity or association* between the hidden training data of 2 different language models, **can we develop *correlation*-aware output combination rules**? This is very difficult to do as every time we're tasked with combining outputs between $LLM_1$ and $LLM_2$, we require knowledge of their training data; what the training data was used and how much similarity there was between the training data. This becomes infeasible as we will need a labelling system that encodes these for every single LLM being used. Furthermore, we do not have access to the training data for closed sourced LLMs such as ChatGPT, Gemini, etc.

---
Now we demonstrate an example where an evidence theory can be applied to combine outputs from LLMs. Two LLMs are asked whether a patient’s symptoms suggest a viral or bacterial infection. One model, drawing on its internal associations, produces a confident answer of “viral.” Another produces a nuanced response pointing toward bacterial causes, citing subtle risk factors. A human decision-maker is then faced with conflicting, partially overlapping evidence—where neither model can be dismissed outright, but their combination cannot be handled by simple majority vote or averaging probabilities. In domains like healthcare, law, or national security, such scenarios are not hypothetical: the ability to combine evidence from multiple AI systems with rigor and transparency may be critical to both safety and trust.

---
# Towards defining conflict (natural language level)
LLMs produce distributions over tokens, which do not neatly correspond to discrete hypotheses in a power set. These distributions are, for lack of a better causal notion, *influenced by* prior interactions (such as in fine tuning), prompts (the current input) and hidden training data. For each $\{FT, P, D\}$, the output of an LLM, $y$ can overlap with another LLM's output, $y'$. **The overlap can be either semantic or syntactic or both**. So we have to answer then- **When is the overlap semantic and when is it syntactic?**. Answering these will in turn help us determine *conflict and agreement* in the outputs (at this point, we are considering the outputs to be the evidence).
Can we use principles from computational linguistics to answer these questions? Have they been answered already? (TODO: Search for these)

---
In evidence theory, a basic probability assignment function (BPA) maps subsets of hypothesis space to belief masses. In LLMs, what is the **token-level equivalent** of hypotheses? We probably study that via [[#Outputs are influenced by ...]] instead. We can however make our lives easier by letting our research reside at the natural language level. And simply encode outputs into a limited vocabulary space. 
Take for example the following case:
![[Pasted image 20251004170022.png]]
The above statement can be encoded into the following
```
ENTITY: Ducksound
TRANSFORM: Laplace
STATE: Undefined in Euclidean Space
CONDITION: Convergent if Surface = Mobius (Toast)
```
The above encoding is horrible. Firstly, as the vocabulary or alphabet is not general, the alphabet will explode as the number of random statements increases. Secondly, **it is very difficult to decode this into the original statement.** But, **can we find a vocabulary or alphabet that won't explode and is easy to decode?** If we can, we can ignore token level evidence combination and focus on this programming language. Perhaps we can use RL (Reinforcement learning) to find such an encoding that has the following properties
1. Easy to decode
2. Does not explode as the number of statements seen increases
3. **Hypotheses** can be derived from the encoding.