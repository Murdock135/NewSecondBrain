If we limit the types of conversations we have with LLMs to ones that invoke some form of abduction, we can imagine a scenario where multiple LLMs make inferences about the same object, in which case we require a way to judge the inferences. One approach is an adaptation of Dempster Schafer theory, where we combine *evidence* from multiple *independent* information sources.
Let $H=\{ h_1, h_2, ..., h_n\}$ be n hypotheses from n LMs (language models). Then there is a function $f:o \times x \times m \rightarrow h$, that maps a tuple (LLM output $o$, user_input $x$, misc_info $m$) to a hypothesis $h$. This is the same for any number of LMs. In fact, we can model $f$ as a random process that depends on the set of $o$'s, $x$'s and $m$. Thus, we can use a separate LM to carry out this mapping as a random process.
# Modelling $f$ as a random process
Let $f$ be a stochastic mapping with distribution:
$$
P(h|o,x,m)
$$
Extending this to multiple LMs, we have
$$
P(h|\mathbf{o}, x, m)
$$
where,
$\mathbf{o} = (o_1, o_2, ... , o_n)$ from LMs $l_1, l_2, ... l_n$
