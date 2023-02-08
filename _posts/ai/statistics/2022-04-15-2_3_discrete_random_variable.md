---
layout: post
title: "[Statistics] 2.3 Discrete Random Variable and Important Distributions"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Important Discrete Distributions

## Point Mass Distribution

$$X$$ has a **point mass distribution** at $$a$$, written as $$X \sim \delta_a$$, if $$P(X=a)=1$$. In other words, the **PMF** is $$f(x)=1$$ for $$x=a$$ and $$0$$ otherwise.

The **CDF** is,

$$
F(x) = \begin{cases}
0, & x < a \\\ 1, & x \geq a
\end{cases}
$$

## Discrete Uniform Distribution

Let $$k > 1$$ be a given integer. $$X$$ has a **uniform distribution** on $$\{ 1,...,k \}$$ if its **PMF** is

$$
f(x) =
\begin{cases}
\frac{1}{k}, & \text{for}\ x = 1,...,k \\\ 0, & \text{otherwise}
\end{cases}
$$

## Bernoulli Distribution

Suppose a discrete random variable $$X$$. If $$P(X=1)=p$$ and $$P(X=0)=1-p$$ for some $$p \in [0,1]$$, we say $$X$$ has a **Bernoulli distribution**, written in $$X \sim \text{Bernoulli}(p)$$. The **PMF** is

$$ f(x) = p^x(1-p)^{1-x},\ x \in \{0,1\} $$

The bernoulli distribution can be thought as assigning probability $$p$$ for **success** and $$1-p$$ for **failure**.

$$ \mathbb{E}[X]=p $$

$$ Var(X)=p(1-p) $$

## Binomial Distribution

The binomial distribution is simply "multiple" bernoulli. Supppose we have a coin which falls heads up with probability $$p$$ for some $$0 \leq p \leq 1$$. Then, flip the coin $$n$$ times and let $$X$$ be the **number of heads**, assuming each toss is independent. Then the **PMF** is given by

$$
f(x) =
\begin{cases}
\binom{n}{x}p^x(1-p)^{n-x}, & x=0,...,n \\\ 0, & \text{otherwise}
\end{cases}
$$

A random variable $$X$$ with this PMF is called a **Binomial random variable** and we denote $$X \sim \text{Binomial}(n,p)$$.

Note that if $$X-1 \sim \text{Binomial}(n_1,p)$$ and $$X_2 \sim \text{Binomial}(n_2,p)$$, then $$X_1 + X_2 \sim \text{Binomial}(n_1 + n_2, p)$$

$$ \mathbb{E}[X]=np $$

$$ Var(x) = np(1-p) $$

$$\mathbb{E}[X] = np$$ since using the **linearity of expectation**, binomial random variable is the sum of $$n$$ bernoulli random variables.

$$Var(x)=np(1-p)$$ since each bernoulli trial is **independent**, thus **uncorrelated**, thus the **covariance** is $$0$$. Therefore, the variance of a binomial random variable is also the sum of variance of $$n$$ bernoulli random variable.

## Geometric Distribution

$$X$$ has a **geometric distribution** with **parameter** $$p \in (0,1)$$, written $$X \sim Geom(p)$$, if

$$ P(X=k) = p(1-p)^{k-1},\ k \geq 1 $$

We can see that it satisfies the requirement:

$$ \sum*{k=1}^{\infty}P(X=k) = p \sum*{k=1}^{\infty}(1-p)^{k-1} = \frac{p}{1-(1-p)}=1 $$

using **infinite geometric series** formula $$\sum_{k=0}^{\infty}ar^k = \frac{a}{1-r}$$.

You can view a geometric random variable $$X$$ as the number of trials **until the first success**.

$$ \mathbb{E}[X] = \frac{1}{p} $$

$$ Var(X)=\frac{1-p}{p^2} $$

> # Poisson Distribution

$$X$$ has a Poisson distribution with parameter $$\lambda$$, written $$X \sim \text{Poisson}(\lambda)$$ if

$$ f(x)= e^{-\lambda} \frac{\lambda^x}{x!},\ x \geq 0 $$

The Poisson is often used as a model for **counts of rare events** like traffic accidents.

If $$X_1 \sim \text{Poisson}(\lambda_1)$$ and $$X_2 \sim \text{Poisson}(\lambda_1)$$ then $$X_1+X_2 \sim \text{Poisson}(\lambda_1 + \lambda_2)$$

$$ \mathbb{E}[X]=\mu $$

$$ Var(X)=\mu $$

> # Random variable vs Parameter

Note that $$X$$ is a **random variable** and $$x$$ denotes a **particular value** of $$X$$. Values such as $$n$$, $$p$$, $$\lambda$$ are **parameters** which are fixed real numbers. The parameters are usually **unknown** and must be **estimated** from data which is what **statistical inference** is about.

> # References

[1] All of Statistics by Larry A. Wasserman
