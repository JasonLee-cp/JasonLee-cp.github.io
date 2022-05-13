---
layout: null
title: "[Statistics] 3.3 Variance and Covariance"
categories: ["statistics"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Variance

Intuitively, the variance measures the **spread** of a distribution.

## Definition

Let $X$ be a random variable with mean $\mu$. The **variance** of $X$, denoted by $\sigma^2$ or $\sigma_X^2$ or $V(X)$, or $\text{Var}(X)$ is defined by

\[[ \text{Var}(X) = \sigma^2 = \mathbb{E}(X-\mu)^2 = \int (x-\mu)^2 dF(x) \]]

assuming this expectation exists. The **standard deviation** $\text{std(X)}=\sqrt{\text{Var}(X)} = \sigma = \sigma_X$

## Properties

**[1]** $\text{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \mathbb{E}[X^2]-\mu^2$

**[2]** If $a$ and $b$ are constants, then $\text{Var}(aX+b) = a^2\text{Var}(X)$

**[3]** If $X_1,...,X_n$ are **independent** and $a_1,...,a_n$ are constants, then

\[[ \text{Var}\left( \sum_{i=1}^n a_iX_i \right) = \sum_{i=1}^n a_i^2 \text{Var}(X_i) \]]

> # Sample mean and Sample variance

If $X_1,...,X_n$ are random variables then we define the **sample mean** to be

\[[ \overline{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \]]

and the **sample variance** is

\[[ S_n^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline{X}_n) \]]

## 3.17 Theorem

Let $X_1,...,X_n$ be **IID** and let $\mu=\mathbb{E}[X_i], \sigma^2=\text{Var}(X_i)$. Then,

\[[ \mathbb{E}[\overline{X}_n] = \mu \]]

\[[ \text{Var}(\overline{X}_n)=\frac{\sigma^2}{n} \]]

\[[ \mathbb{E}(S_n^2) = \sigma^2 \]]

> # Covariance and Correlation

Let $X$ and $Y$ be random variables with means $\mu_X$ and $\mu_Y$ and standard deviations $\sigma_X$ and $\sigma_Y$.

The **covariance** between $X$ and $Y$ is defined by

\[[ \text{Cov}(X,Y) = \mathbb{E}\left[(X-\mu_X)(Y-\mu_Y)\right] \]]

The **correlation** is defined by

\[[ \rho = \rho_{X,Y}=\rho(X,Y)=\frac{\text{Cov}(X,Y)}{\rho_X\rho_Y} \]]

## Properties

\[[ \text{Cov}(X,Y) = \mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y] \]]

\[[ -1 \leq \rho(X,Y) \leq 1 \]]

If $Y = aX + b$ then,

$\rho(X,Y)=1$ if $a > 0$ and

$\rho(X,Y)=-1$ if $a<0$

If $X$ and $Y$ are **independent**, then $\text{Cov}(X,Y)=\rho=0$. The converse is generally not true

## 3.20 Theorem

\[[ \text{Var}(X+Y)=\text{Var}(X)+\text{Var}(Y)+2\text{Cov}(X,Y) \]]

\[[ \text{Var}(X-Y)=\text{Var}(X)+\text{Var}(Y)-2\text{Cov}(X,Y) \]]

More generally, for random variables $X_1,...,X_n$,

\[[ \text{Var}\left( \sum_i a_iX_i \right) = \sum_i a_i^2 \text{Var}(X_i) + 2 \sum \sum_{i<j}a_ia_j \text{Cov}(X_i,X_j) \]]

> # References

[1] All of Statistics by Larry A. Wasserman
