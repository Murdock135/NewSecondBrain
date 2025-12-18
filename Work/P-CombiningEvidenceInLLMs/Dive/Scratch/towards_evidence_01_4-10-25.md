The following essay attempts to synthesize my thought process on how to arrive at a frame of discernment for LLMs.
 
---
# Towards an evidence theory
LLMs produce distributions over tokens, which do not neatly correspond to discrete hypotheses in a power set. These distributions are, for lack of a better causal notion, *influenced by* prior interactions (such as in fine tuning), prompts (the current input) and hidden training data. Should DST (Dempster Shafer Theory) or an adaptation of the theory be applied to LLMs, we must first realize that the so called sources of information; the language models, are not independent unless their hidden training data are *different*. Now we arrive at the first problem. **What does it mean for hidden training data to be different?** Could it be the difference between distributions over a high dimensional 'vocabulary space'? May be. An even deeper question is - **Should the sources (LLMs) actually be *independent*?**. In Dempster–Shafer theory, you can only combine evidence from two sources if they are _independent_.  If two sensors share the same noise source, combining them would exaggerate confidence.  The same risk applies to language models — two models might produce similar answers because they’ve learned from similar training data, not because the evidence is strong. This question is probably already studied in *ensembling techniques* (TODO: Search). There are several 'ad-hoc' methods for merging or aggregating generations such as majority vote, confidence-weighted averaging (TODO: cite). But they are not explainable techniques and do not express uncertainty. 
## Takeaways
1. How to define *independence* between language models?
2. What does it mean for training data to be different?
3. *Should* the training data be different?

Since there could be *similarity or association* between the hidden training data of 2 different language models, **can we develop *correlation*-aware output combination rules**? This is very difficult to do as every time we're tasked with combining outputs between $LLM_1$ and $LLM_2$, we require knowledge of their training data; what training data was used and how much similarity there was between the training data. Furthermore, we do not have access to the training data for closed sourced LLMs such as ChatGPT, Gemini, etc. The easy way out of this is to **take models from Huggingface that you know were trained on completely different datasets**.
We may be able to sidestep the above limitation of the training data being hidden by ***extrapolating* independence from the behavior of different LLMs.** A simple test recommended by ChatGPT (although this is very faulty) is to mark two differrent LLMs only if a number of their outputs are in conflict (low *similarity*).

---
Now we demonstrate an example where an evidence theory can be applied to combine outputs from LLMs. Two LLMs are asked whether a patient’s symptoms suggest a viral or bacterial infection. One model, drawing on its internal associations, produces a confident answer of “viral.” Another produces a nuanced response pointing toward bacterial causes, citing subtle risk factors. A human decision-maker is then faced with conflicting, partially overlapping evidence—where neither model can be dismissed outright, but their combination cannot be handled by simple majority vote or averaging probabilities. In domains like healthcare, law, or national security, such scenarios are not hypothetical: the ability to combine evidence from multiple AI systems with rigor and transparency may be critical to both safety and trust.

---
# Towards defining conflict (natural language level)
LLMs produce distributions over tokens, which do not neatly correspond to discrete hypotheses in a power set. These distributions are, for lack of a better causal notion, *influenced by* prior interactions (such as in fine tuning) $FT$, prompts (the current input) $P$ and hidden training data $D$. For each $\{FT, P, D\}$, the output of an LLM, $y$ can overlap with another LLM's output, $y'$. **The overlap can be either semantic or syntactic or both**. So we have to answer then- **When is the overlap semantic and when is it syntactic?**. Answering these will in turn help us determine *conflict and agreement* in the outputs (at this point, we are considering the outputs to be the evidence).
Can we use principles from computational linguistics to answer these questions? Have they been answered already? (TODO: Search for these)
In evidence theory, a basic probability assignment function (BPA) maps subsets of hypothesis space to belief masses. **What are hypotheses in the case of LLM outputs?** Are they the raw outputs themselves or a portion of the output? The output may be really large (or small) and not all of the text deserves to be classified as a 'hypotheses'.  A portion may be a hypotheses and the rest could be textual justification for the hypotheses. Do we care about this in the first place? If the end goal is to develop a general merging or combination strategy for any LLM output, then we need a way to combine natural language in general, not just hypotheses. To do this, **can we simply encode outputs into a limited vocabulary space?** 
Take for example the following case:
![[Pasted image 20251004170022.png]]
The above statement can be encoded into the following
```
ENTITY: Ducksound
TRANSFORM: Laplace
STATE: Undefined in Euclidean Space
CONDITION: Convergent if Surface = Mobius (Toast)
```
The above encoding is horrible. Firstly, as the vocabulary or alphabet is not general, the alphabet will explode as the number of random statements increases. Secondly, **it is very difficult to decode this into the original statement.** But, **can we find a vocabulary or alphabet that won't explode and is easy to decode?** Perhaps we can use RL (Reinforcement learning) to train a language model to find such an encoding that has the following properties
1. Easy to decode
2. Does not explode as the number of statements seen increases
3. **Hypotheses** can be derived from the encoding.
This, I believe is a form of *information extraction*, which originated in NLP. Of course, we can simply provide an LLM a set of entities to identify, but this skips the question of whether that set of entities is a good one. 
Once we get the encoding, we can develop methods to assess semantic similarity. For example, if we really do use the horrible vocabulary from the previous example, another language model might, just might produce an output that can be encoded into the following.
```
ENTITY: Cowsays
TRANSFORM: Fourier
STATE: Almost defined in Euclidean Space
CONDITION: Convergent if Surface = Mobius (Hot)
```
We need to figure out what **the amount of semantic overlap** between this and the previous statement is. 

# Extracting belief masses from LLM outputs
LLMs have been trained to 'talk a lot' for whatever reason. So merely counting the number of justifications for the LLM's hypotheses is not a good measure for its belief. Using the limited vocabulary concept in [[#Towards defining conflict (natural language level)]] evades this issue.

---
# Accounting for randomness
Recall that LLMs are stochastic in nature. Thus, a particular $\{FT, P, D\}$ may generate different $y$'s each time you call it. Thus, it may be a good idea to store multiple $y$'s and extrapolate a sense of how much the model itself believes in its output. For example, a prompt like `"say something completely random"` will most likely yield something completely different every single time.