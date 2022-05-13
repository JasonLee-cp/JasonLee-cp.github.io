---
layout: null
title: "[Statistics] 3.1 Expectation of Random Variables"
categories: ["statistics"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Expectation of a Random Variable

The **expected value**, or **mean** or **first moment** of a random variable $X$ is defined to be

\[[ \mathbb{E}(X) = \int xdF(x) \]]

that is,

## Discrete

\[[ \mathbb{E}(X) = \sum_{x}xf(x) \]]

## Continuous

\[[ \mathbb{E}(X) = \int_{x}xf(x)dx \]]

assuming that the sum or integral is well defined. The equivalent notations for expectation of $X$ is,

\[[ \mathbb{E}(X) = \mathbb{E}X = \int xdF(x) = \mu = \mu_{X} \]]

To ensure that $\mathbb{E}(X)$ is well defined, we say $\mathbb{E}(X)$ exists if $\int_{x} \lvert x\rvert dF_X (x) < \infty$, otherwise the expectation does not exist.

> # The Rule of the Lazy Statistician

Let $Y = r(X)$. Then,

\[[ \mathbb{E}(Y) = \mathbb{E}(r(X)) = \int r(x) dF_X(x) \]]

Functions of several variables are handled in a similar way. If $Z = r(X,Y)$ then,

\[[ \mathbb{E}(Z) = \mathbb{E}(r(X,Y)) = \int \int r(x,y)dF(x,y) \]]

## Probability is a special case of expectation

Let $A$ be an event and let $r(x) = I_A(x)$, an indicator function, where $I_A(x) = 1$ if $x \in A$ and $I_A(x) = 0$ if $x \notin A$. Then,

\[[ \mathbb{E}(I_A(X)) = \int I_A(x)f_X(x)dx = \int_{A}f_{X}(x)dx = P(X \in A) \]]

## Example 1

Let $X \sim \text{Unif}(0,1)$. Let $Y=r(x)=e^{X}$. Find $\mathbb{E}(Y)$

\[[ \mathbb{E}(Y) = \int_0^1 e^x f(x)dx = \int_0^1 e^xdx = e-1 \]]

since the PDF of a uniform distribution is $\frac{1}{\beta - \alpha}$

> # $k^{th}$ moment

The $k^{th}$ moment of $X$ is defined to be $\mathbb{E}(X^k)$

assuming that $\mathbb{E}(\lvert X \rvert^k) < \infty$

## 3.10 Theorem

> If the $k^{th}$ moment exists and if $j < k$, then the $j^{th}$ moment exists

**Proof**

Consider $j^{th}$ moment where $j<k$. Then we have

\[[ \mathbb{E}(\lvert X \rvert^j) = \int_{-\infty}^{\infty}\lvert x \vert^j f_X(x)dx \]]

\[[  = \int*{\lvert x \rvert \leq 1} \lvert x \rvert^j f_X(x)dx + \int*{\lvert x \rvert > 1}\lvert x \rvert^j f_X(x)dx \]]

\[[ \leq \int_{\lvert x \rvert \leq 1}f_X(x)dx + \int_{\lvert x \rvert > 1} \lvert x \rvert^k f_X(x)dx \]]

\[[ \leq 1 + \mathbb{E}(\lvert X \rvert^k) < \infty \]]

## Central moment

The $k^{th}$ central moment is defined to be $\mathbb{E}((X - \mu)^k)$.

> # Independence

Let $X_1,...,X_n$ be **independent** random variables. Then,

\[[ \mathbb{E}\left(\prod_{i=1}^n X_i \right) = \prod_i \mathbb{E}(X_i) \]]

> # References

[1] All of Statistics by Larry A. Wasserman
