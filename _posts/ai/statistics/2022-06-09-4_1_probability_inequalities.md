---
layout: post
title: "[Statistics] 4.1 Probability Inequalities"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Markov's Inequality

Let $$X$$ be a non-negative random variable and suppose that $$\mathbb{E}[X]$$ exists. For any $$t > 0$$,

$$ P(X > t) \leq \frac{\mathbb{E}[X]}{t} $$

## Proof

Since $$X>0$$,

$$ \mathbb{E}[X] = \int_0^{\infty}xf(x)dx = \int_0^t xf(x)dx + \int_t^{\infty}xf(x)dx $$

$$ \geq \int_t^{\infty} xf(x)dx \geq t\int_t^{\infty}f(x)dx $$

$$ = t P(X>t) $$

> # Chebyshev's Inequality

Let $$\mu = \mathbb{E}[X]$$ and $$\sigma^2 = Var(X)$$. Then,

$$ P(\lvert X - \mu \rvert \geq t) \leq \frac{\sigma^2}{t^2} $$

$$ P(\lvert Z \rvert \geq k) \leq \frac{1}{k^2} $$

where $$Z = \frac{X-\mu}{\sigma}$$. In particular, $$P(\lvert Z \rvert > 2) \leq \frac{1}{4}$$ and $$P(\lvert Z \rvert > 3) \leq \frac{1}{9}$$

## Proof

We can prove it with Markov's inequality

$$ P(\lvert X - \mu \rvert \geq t) = P(\lvert X - \mu \rvert^2 \geq t^2) \leq \frac{\mathbb{E}[X-\mu]^2}{t^2} = \frac{\sigma^2}{t^2} $$

If we set $$t=k\sigma$$, we get the second part.

> # Hoeffding's Inequality

Hoeffding's inequality is similar to Markov's inequality but it gives a "sharper" inequality.

Let $$Y_1,...,Y_n$$ be **independent observations** such that $$\mathbb{E}[Y_i]=0$$ and $$a_i \leq Y_i \leq b_i$$. Let $$\epsilon > 0$$. Then, for any $$t > 0$$,

$$ P\left(\sum*{i=1}^n Y_i \geq \epsilon \right) \leq e^{-t\epsilon}\prod*{i=1}^n e^{t^2(b_i-a_i)^2/8} $$

## 4.5 Theorem

Let $$X_1,...,X_n \sim Bernoulli(p)$$. Then, for any $$\epsilon > 0$$,

$$ P(\lvert \bar{X}\_n - p \rvert > \epsilon) \leq 2e^{-2n\epsilon^2} $$

where $$\bar{X}_n = n^{-1}\sum_{i=1}^n X_i$$

> # Mill's Inequality

Let $$Z \sim N(0,1)$$. Then,

$$ P(\lvert Z \rvert > t) \leq \sqrt{\frac{2}{\pi}}\frac{e^{-t^2/2}}{t} $$

> # References

[1] All of Statistics by Larry A. Wasserman
