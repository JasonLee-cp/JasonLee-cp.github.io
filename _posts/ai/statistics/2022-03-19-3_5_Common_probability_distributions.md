---
layout: post
title: "[Statistics] Common Probability Distributions in Machine Learning"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> ## Bernoulli Distribution

A discrete random variable $$X$$ has a **bernoulli distribution** with parameter $$p$$, $$0 \leq p \leq 1$$, if its probability mass function is,

$$ p_X(1)=P(X=1)=p $$

$$ p_X(0)=P(X=0)=1-p $$

This distribution is denoted by $$Ber(p)$$.

$$ \mathbb{E}\_X[X]=p $$

$$ Var_X(X)=p(1-p) $$

> ## Binomial Distribution

A discrete random variable $$X$$ has a **binomial distribution** with parameters $$n$$ and $$p$$, where $$n$$=1,2,... and $$0 \leq p \leq 1$$, if its probability mass function is,

$$ p_X(k) = P(X=k) = \binom{n}{k}p^k(1-p)^{n-k},\ k=0,1,...,n $$

This distribution is denoted by $$Bin(n,p)$$

$$ \mathbb{E}[X]=np $$

$$ Var(X)=np(1-p) $$

> ## Geometric Distribution

A discrete random variable $$X$$ has a geometric distribution with parameter $$p$$, where $$0 < p \leq 1$$, if its probability mass function is,

$$ p_X(k)=P(X=k)=(1-p)^{k-1}p,\ k=1,2,.. $$

This distribution is denoted by $$Geo(p)$$

$$ \mathbb{E}[X]= \frac{1}{p} $$

$$ Var(X) = \frac{1-p}{p^2} $$

> ## Multinoulli(categorical) Distribution

Multinoulli distribution is a distribution over a **single** discrete variable with **k different states** where k is finite. Multinoulli distribution is parametrized by a **vector** $$p \in [0,1]^{k-1}$$ where $$p_i$$ gives the probability of the $$i^{th}$$ state. The final or $$k^{th}$$ state's probability is,

$$ p_k = 1 - \mathbb{1}^{\top}p,\ \mathbb{1}^{\top}p \leq 1 $$

Since multinoulli distribution is commonly used for distributions over **categories** of objects, state 1 does not usually refer to a numerical value 1. Therefore, we usually do not need to compute the expectation or variance.

> ## Gaussian(normal) Distribution

The most commonly used distribution is **normal distribution** or **Gaussian distribution**.

$$ \mathcal{N}(x;\mu,\sigma^2) = \sqrt{\frac{1}{2\pi \sigma^2}}exp \left(-\frac{1}{2\sigma^2}(x-\mu)^2 \right) $$

The normal distribution has two parameters: $$\mu \in \mathbb{R}$$ and $$\sigma \in (0, \infty)$$ which control the distribution. $$u$$ gives the **coordinate** of the central peak. So, $$\mathbb{E}[X]=\mu$$. The standard deviation of the distribution is given by $$\sigma$$ so the variance is $$Var(X)=\sigma^2$$.

Sometimes it's useful to transform the normal distribution to a simplified version where $$\mu=0, \sigma=1$$. This distribution is called **standard normal distribution**.

$$ \phi(X) = \frac{1}{\sqrt{2\pi}} exp \left(-\frac{1}{2}x^2 \right) $$

In the case where we need to evaluate pdf frequently with different parameters, a more efficient way of parametrizing the Gaussian distribution is to use a parameter $$\beta \in (0, \infty)$$ to control the **precision** or **inverse variance** of the distribution.

$$ \mathcal{N}(x;\mu,\beta^{-1}) = \sqrt{\frac{\beta}{2\pi}}exp \left(-\frac{1}{2}\beta(x-\mu)^2 \right) $$

Normal distribution is suitable for many applications. The two major reasons are,

1. Many distributions in real-world are indeed close to being normal distributions. The **central limit theorem** proves that the sum of many independent random variables is approximately normally distributed.
2. The normal distribution encodes the maximum amount of **uncertainty** over the real numbers.

> ## Multivariate Normal Distribution

The normal distribution generalized to $$\mathbb{R}^n$$. In this case, the distribution is called **multivariate normal distribution**. The distribution is now parametrized by $$\mu$$ and $$\Sigma$$. $$u$$ still refers to the mean of the distribution but it's in **vector** form. $$\Sigma$$ gives the **covariance matrix** of the distribution.

$$ \mathcal{N}(x;\mu,\Sigma) = \sqrt{\frac{1}{(2\pi)^n det(\Sigma)}} exp \left( -\frac{1}{2}(x-\mu)^{\top} \Sigma^{-1}(x-\mu) \right) $$

Similarly as above, when we evaluate the pdf many times with many different parameters, covariance is not a computationally efficient. Instead, we can use a **precision matrix** $$\beta$$.

$$ \mathcal{N}(x;\mu,\beta^{-1}) = \sqrt{\frac{det(\beta)}{(2\pi)^n}} exp \left( -\frac{1}{2}(x-\mu)^{\top} \beta(x-\mu) \right) $$

We often make the covariance matrix to be a **diagonal** matrix. An even simpler version is the **isotropic** Gaussian distribution whose covariance matrix is a scalar times the identity matrix.

> ## Exponential Distribution

A **continuous** random variable has an exponential distribution with parameter $$\lambda$$ if its pmf $$f$$ is given by $$f(x)=0$$, if $$x<0$$ and

$$ f(x) = \lambda e^{-\lambda x},\ x \geq 0 $$

This distribution is denoted by $$Exp(\lambda)$$

$$ F(x) = 1 - e ^ {-\lambda x},\ x \geq 0 $$

$$ \mathbb{E}[X] = \frac{1}{\lambda} $$

$$ Var(X) = \frac{1}{\lambda^2} $$

> ## Laplace Distribution

$$ Laplace(x: \mu, \gamma) = \frac{1}{2\gamma}exp \left( -\frac{\lvert x-\mu \rvert}{\gamma} \right) $$

> ## Dirac Distribution

In some cases, we want to make that all the mass in a probability distribution clusters around a **single point**. This can be accomplished by the **Dirac delta function** $$\delta(x)$$:

$$ f(x) = \delta(x - \mu) $$

The Dirac delta function is zero everywhere except $$0$$ but intergrates to $$1$$. The Dirac delta function is not an ordinary function with $$x$$ and real-valued output pair. Instead, it's a different kind of mathematical object called a **generalized function** that is defined in terms of its properties when integrated.

A common use of this distribution is as a component of an **empirical distribution**,

$$ \hat{p}(x) = \frac{1}{m} \sum\_{i=1}^m \delta(x- x^{(i)}) $$

which puts probability mass $$\frac{1}{m}$$ on each of the $$m$$ points $$x^{(1)},...,x^{(m)}$$. The Dirac delta distribution is only necessary to define the **empirical distribution** over **continuous variables**.

For discrete variables, an empirical distribution can be established as a **multinoulli distribution** where a probability associated with each input value is simply equal to the **empirical frequency** of the value in the training set.

> ## Mixtures of Distributions

Another way of defining probability distributions is by combining other probability distributions. One common way is to construct a **mixture distribution**. On each trial, the choice of which component distribution is determined by **sampling a component identity** from a **multinoulli distribution**:

$$ P(x) = \sum_i P(c=i)P(x\|c=i) $$

where $$P(c)$$ is the multinoulli distribution over component identities.

> ## Gaussian Mixture Model

Gaussian mixture model is a very powerful mixture model in which the components $$p(x \|c = i)$$ are Gaussians. Each component has a separately parametrized mean $$\mu^{(i)}$$ and covariance $$\Sigma^{(i)}$$. The parameters of a Gaussian mixture specify the **prior probability** $$\alpha_i = P(c=i)$$ given to each component $$i$$. $$P(c \| x)$$ is a **posterior probability**. A Gaussian mixture model is a **universal approximator** of densities.

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/) - chapter 3  
[2] _A Modern Introduction to Probability and Statistics by Dekking_
