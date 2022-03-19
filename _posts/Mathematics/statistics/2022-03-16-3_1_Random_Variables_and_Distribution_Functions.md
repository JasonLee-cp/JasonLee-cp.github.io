---
layout: null
title: "[Statistics] Random variables and distribution functions"
categories: ["statistics"]
tag: [math]
---

> ## Discrete Random Variable

Let $\Omega$ be a sample space. A **discrete random variable** is a function $X:\Omega \rightarrow \mathbb{R}$ that takes on a finite number of values $a_1, a_2,..,a_n$ or an infinite number of values $a_1, a_2,..$

In other words, a discrete random variable $X$ **transforms** $\Omega$ into a more **tangible** sample space $\tilde{\Omega}$. For example, $\Omega=\{(1,1),(2,2)\}$ is transformed into $\tilde{\Omega}=\{2,4\}$.

Now, it's important to determine the **probability distribution** of $X$ to describe how **probability mass** is distributed over possible values of $X$. This information lies in the **probability mass function (pmf)**

> ## Probability Mass Function (pmf)

The **probability mass function** p of a **discrete** random variable $X$ is the function $p:\mathbb{R}\rightarrow[0,1]$, defined by

\[[p(a)=P(X=a),\ -\infty<a<\infty\]]

If $X$ is a **discrete** random variable that takes on the values $a_1,a_2,..$, then $P$ must satisfy:

1. The domain of $P$ must be the set of all possible states of $a$
2. $\forall a  \in X,\ 0 \leq p(a) \leq 1$
3. $\sum_{a\in \tilde{\Omega}} p(a)=1$ and this property is referred to as being **normalized**. All the other $p(a)=0$

> ## Continuous Random Variable

A continuous random variable is a random variable which takes on continuous values rather than discrete values.

> ## Probability Density Function (pdf)

A random variable $X$ is **continuous** if for some function $f: \mathbb{R} \rightarrow \mathbb{R}$ and for any numbers $a$ and $b$ with $a \leq b$,

\[[ P(a \leq X \leq b) = \int_{a}^{b}f(x)dx \]]

It must satisfy:

1. The domain of $p$ must be the set of all possible states of x
2. $\forall a \in X,\ p(a) \geq 0$. We do note required $p(x) \leq 1$
3. $\int_{-\infty}^{\infty}f(x)dx=1$

Note that $p(x)$ **does not** give the probability of a specific state directly but it tells the probability of a state being inside the infinitesimal region or how likely it is that $X$ is **near** $a$.

Also, if the interval gets smaller, $p(x) \rightarrow 0$. For any positive $\epsilon$,

\[[ P(a-\epsilon \leq X \leq a + \epsilon) = \int_{a-\epsilon}^{a+\epsilon}f(x)dx \]].

If $\epsilon \rightarrow 0$, then

\[[ P(X=a)=0 \]]

which implies that we can be careless about the interval form

\[[ P(a \leq X \leq b)=P(a \lt X \lt b) \]]

> ## Cumulative Distribution Function (cdf)

So far we've seen what discrete and continuous random variables are the corresponding pmf and cdf which show their probability distributions. However realize that

1. Discrete R.Vs do not have **pdf (f)**
2. Continuous R.Vs do not have **pmf (p)**

Using the **cumulative distribution function**, both discrete and continuous random variables can be treated equally. The cumulative distribution function is sometimes referred to as **distribution function** ommitting cumulative.

**Cumulative Distribution Function**

The distribution function $F$ of a random variable $X$ is the function $F: \mathbb{R} \rightarrow [0,1]$, defined by

\[[F(a)=P(X \leq a),\ -\infty \lt a \lt \infty\]]

> ## 3 properties of cdf

1. For $a \leq b$, $F(a) \leq F(b)$ since $a \leq b$ implies that the event $\{X \leq a\} \subset \{X \leq b\}$
2. Since $F(a)$ is a **probability**, $0 \leq F(a) \leq 1$. Moreoever,

\[[ \lim_{a \rightarrow +\infty}F(a) = \lim_{a \rightarrow +\infty}p(x \leq a) = 1 \]]
\[[ \lim_{a \rightarrow -\infty}F(a) = \lim_{a \rightarrow -\infty}p(x \leq a) = 0 \]]

3. $F$ is **right-continuous**. So, $\lim_{\epsilon \rightarrow a^+}f(a+\epsilon)=F(a)$

> ## Relationship b/w pmf and cdf

If $X$ attains values $a_1, a_2,$.., such that $p(a_i) \gt 0, p(a_1)+p(a_2)+...=1$, then,

\[[ F(a) = \sum_{a_i \leq a}p(a_i) \]]

Also, for discrete random variable, $F$ **jumps** at each $a_i$ and the height of that each jump is $p(a_i)$. Hence,

\[[ p(a_i)=F(a_i)-F(a_{i-1}) \]]

> ## Relationship b/w pdf and cdf

For $a < b$,

\[[ \{X \leq b\} = \{X \leq a\} + \{a < X \leq b\} \]]

Consequently,

\[[ P(a < X \leq b) = P(X \leq b) - P(X \leq a) = F(b) - F(a) \]]

Also, the **Fundamental Theorem of Calculus** further gives us insights about the relationship between $f$ and $F$.

\[[ F(b) = \int_{-\infty}^b f(x)dx \]]

\[[ f(x) = \frac{d}{dx}F(x)\]]

by the **Fundamental Theorem of Calculus**.

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/)  
[2] _A Modern Introduction to Probability and Statistics by Dekking_
