---
layout: null
title: "[Statistics] 3.6 Moment Generating Functions"
categories: ["statistics"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Moment Generating Functions

The **moment generating function** $MGF$, or **Laplace Transform**, of $X$ is defined by

\[[ \psi_X(t) = \mathbb{E}[e^{tX}] = \int e^{tx}dF(x) \]]

where $t$ varies over the real numbers

\[[ \psi '(0)= \left[ \frac{d}{dt} \mathbb{E}[e^{tX}] \right]_{t=0} = \mathbb{E} \left[ \frac{d}{dt}e^{tX} \right]_{t=0} = \mathbb{E}[Xe^{tX}]_{t=0}=\mathbb{E}[X] \]]

Taking $k$ derivatives, we get $\psi^{(k)}(0)=\mathbb{E}[X^k]$

> # Properties of MGF

**[1]** If $Y=aX+b$, then $\psi_Y(t)=e^{bt}\psi_X(at)$

**[2]** If $X_1,...,X_n$ are independent and $Y = \sum_i X_i$, then $\psi_Y(t)=\prod_i \psi_i(t)$ where $\psi_i$ is the $MGF$ of $X_i$.

> # Same MGF, Same Distribution

Let $X$ and $Y$ be random variables. If $\psi_X(t)=\psi_Y(t)$ for all $t$ in an open interval around $0$, then $X \overset{d}{=} Y$.

> # MGF for Common Distribution

The left is the distribution and the right is the MGF $\psi(t)$

- $Bernoulli(p)$: $pe^t + (1-p)$

- $Binomial(n,p)$: $(pe^t + (1-p))^n$

- $Poisson(\lambda)$: $e^{\lambda (e^t-1)}$

- $Normal(\mu, \sigma)$: $exp\left( \mu t + \frac{\sigma^2 t^2}{2} \right)$

- $Gamma(\alpha, \beta)$: $\left( \frac{1}{1-\beta t} \right)^{\alpha}$ for $t < 1 / \beta$

> # References

[1] All of Statistics by Larry A. Wasserman
