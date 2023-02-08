---
layout: post
title: "[Statistics] 2.4 Continuous Random Variable and Important Distributions"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Continuous Uniform Distribution

$$X$$ has a $$\text{Uniform}(a,b)$$ distribution, written $$X \sim \text{Uniform}(a,b)$$, if

$$
f(x) =
\begin{cases}
\frac{1}{b-a}, & x \in [a,b] \\\ 0, & \text{otherwise}
\end{cases}
$$

where $$a<b$$.

The **CDF** is

$$
F(x) =
\begin{cases}
0, & x<a \\
\frac{x-a}{b-a}, & x \in [a,b] \\\ 1, & x > b
\end{cases}
$$

> # Gaussian(Normal) Distribution

$$X$$ has a Normal or Gaussian distribution with parameters $$\mu$$ and $$\sigma$$, denoted by $$X \sim N(\mu, \sigma^2)$$ if

$$ f(x)=\frac{1}{\sigma \sqrt{2 \pi}}exp \left( -\frac{1}{2}\frac{(x-\mu)^2}{\sigma^2} \right), x \in \mathbb{R} $$

where $$\mu \in \mathbb{R}$$ and $$\sigma > 0$$. The parameter $$\mu$$ is the **center** or **mean** of the distribution and $$\sigma$$ is the **spread** or **standard deviation** of the distribution.

## Standard Normal Distribution

|               ![joint](..//assets/img/MATH/statistics/ch2_1.png)                |
| :-----------------------------------------------------------------------------: |
| _[all-of-statistics](https://link.springer.com/book/10.1007/978-0-387-21736-9)_ |

$$X$$ has a **standard normal distribution** if $$\mu=0$$ and $$\sigma=1$$ in the normal distribution.

Conventionally, a **standard normal distribution** is denoted by $$Z$$. The **PDF** and **CDF** of $$Z$$ are denoted by $$\phi$$ and $$\Phi$$.

## Some useful facts

$$(i)$$ If $$X \sim N(\mu, \sigma^2)$$, then $$Z = \frac{X-\mu}{\sigma} \sim N(0,1)$$

$$(ii)$$ If $$Z \sim N(0,1)$$, then $$X = \mu + \sigma Z \sim N(\mu, \sigma^2)$$

$$(iii)$$ If $$X_i \sim N(\mu_i, \sigma_i^2)$$, $$i=1,...,n$$ are independent, then

$$ \sum*{i=1}^n X_i \sim N \left( \sum*{i=1}^n \mu*i, \sum*{i=1}^n \sigma_i^2 \right) $$

It follows from $$(i)$$ that if $$X \sim N(\mu, \sigma^2)$$, then

$$ P(a < X < b) = P \left( \frac{a - \mu}{\sigma} < Z < \frac{b - \mu}{\sigma} \right) $$

$$ = \Phi \left( \frac{b-\mu}{\sigma} \right) - \Phi \left( \frac{a-\mu}{\sigma} \right) $$

Thus, we can compute any probabilities if we can compute **CDF** $$\Phi(z)$$ of a **standard Normal**. We usually compute $$\Phi(z)$$ and $$\Phi^{-1}(q)$$.

**Example** Suppose $$X \sim N(3,5)$$. Find $$P(X>1)$$.

$$P(X>1) = 1 - P(X<1) = 1 - P \left( Z < \frac{1-3}{\sqrt{5}} \right) = 1 - \Phi(-0.8944)=0.81$$

> # Exponential Distribution

$$X$$ has an exponential distribution with parameter $$\beta$$, denoted by $$X \sim \text{Exp}(\beta)$$, if

$$ f(x)=\frac{1}{\beta}e^{-x/\beta}, x>0 $$

where $$\beta > 0$$.

> # Gamma Distribution

For $$\alpha > 0$$, the **Gamma function** is defined by

$$ \Gamma(\alpha)=\int_0^{\infty}y^{\alpha-1}e^{-y}dy $$

$$X$$ has a **Gamma distribution** with parameters $$\alpha$$ and $$\beta$$, denoted by $$X \sim \text{gamma}(\alpha, \beta)$$ if,

$$ f(x)=\frac{1}{\beta^{\alpha}\Gamma(\alpha)} x^{\alpha-1}e^{-x/\beta}, x>0 $$

where $$\alpha, \beta > 0$$. The **exponential distribution** is actually $$\text{Gamma}(1,\beta)$$ distribution.

> # Beta Distribution

$$X$$ has a Beta distribution with parameters $$\alpha>0$$ and $$\beta>0$$, denoted by $$X \sim \text{Beta}(\alpha, \beta)$$, if

$$ f(x) = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha) \Gamma(\beta)}x^{\alpha - 1}(1-x)^{\beta - 1}, 0<x<1 $$

> # t and Cauchy Distribution

$$X$$ has a **t distribution** with $$v$$ degrees of freedom, denoted by $$X \sim t_v$$, if

$$ f(x) = \frac{\Gamma(\frac{v+1}{2})}{\Gamma(\frac{v}{2})} \frac{1}{(1+\frac{x^2}{v})^{(v+1)/2}} $$

The **t distribution** is similar to a Normal but it has thicker tails. The normal distribution corresponds to a $$t$$ with $$v=\infty$$.

The **Cauchy distribution** is a **t distribution** with $$v=1$$. The PDF of Cauchy distribution is

$$ f(x) = \frac{1}{\pi(1+x^2)} $$

> # Chi Distribution

$$X$$ has a $$\chi^2$$ distribution with $$p$$ degrees of freedom, denoted by $$X \sim \chi_p^2$$, if

$$ f(x) = \frac{1}{\Gamma(p/2)2^{p/2}}x^{(p/2)-1}e^{-x/2}, x>0 $$

> # References

[1] All of Statistics by Larry A. Wasserman
