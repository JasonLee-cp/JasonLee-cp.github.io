---
layout: null
title: "[Statistics] 2.10 Multinomial and Multi Gaussian Distribution"
categories: ["statistics"]
tag: [math]

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Multinomial

Multinomial is the multivariate version of a Binomial. Consider drawing a single ball from a box which contains balls with $k$ different colors labeled "color 1, color 2, ..., color k". Let $p=(p_1,...,p_k)$ where $p_j \geq 0$ and $\sum_{j=1}^kp_j=1$. Also, $p_j$ is the probability of drawing a ball of color $j$. We draw $n$ times (independent draws with replacement) and let $X = (X_1,...,X_k)$ where $X_j$ is the number of times that color $j$ appears. Hence, $n=\sum_{j=1}^kX_j$. Then, $X$ has a **Multinomial(n,p)** distribution written $X \sim \text{Multinomial}(n,p)$. The probability function is

\[[ f(x) = \binom{n}{x_1 \cdots x_k}p_1^{x_1}\cdots p_k^{x_k} \]]

where

\[[ \binom{n}{x_1 \cdots x_k} = \frac{n!}{x_1! \cdots x_k!} \]]

## 2.42 Lemma

Suppose $X \sim \text{Multinomial}(n,p)$ where $X=(X_1,...,X_k)$ and $p=(p_1,...,p_k)$. The marginal distribution of $X_j$ is $\text{Binomial}(n,p_j)$.

> # Multivariate Normal (Gaussian)

The univariate Normal has two parameters: $\mu$ and $\sigma$. In the multivariate version, $u$ is a **vector** and $\sigma$ is replaced by a **matrix** $\Sigma$.

## Standard Multivariate Normal Distribution

Let

\[[ Z = \begin{pmatrix} Z_1 \\\ \vdots \\\ Z_k \end{pmatrix} \]]

where $Z_1,...,Z_k \sim N(0,1)$ are independent. Then, the **PDF** of $Z$ is

\[[ f(x) = \prod_{i=1}^k f(z_i) = \frac{1}{(2\pi)^{k/2}}exp \left( -\frac{1}{2} \sum_{j=1}^k z_j^2 \right) \]]

\[[ = \frac{1}{(2\pi)^{k/2}}exp \left( -\frac{1}{2}z^Tz \right) \]]

We say that $Z$ has a **standard mulrivariate Normal distribution** written $Z \sim N(0,I)$ where $0$ denotes a vector of $k$ zeros and $I$ is $k \times k$ identity matrix.

## Standard Multivariate Normal Distribution

A **vector** $X$ has a multivariate Normal distribution, denoted $X \sim N(\mu, \Sigma)$, if its **PDF** is

\[[ f(x; \mu, \Sigma) = \frac{1}{(2\pi)^{k/2} \lvert (\Sigma) \rvert^{1/2}}exp \left( -\frac{1}{2}(x-\mu)^T \Sigma^{-1}(x-\mu) \right) \]]

where $\lvert \Sigma \rvert$ denotes the **determinant** of $\Sigma$, $\mu$ is a vector of length $k$ and $\Sigma$ is a $k \times k$ **symmetric, positive definite** matrix. If we set $\mu = 0, \Sigma=I$, we get the standard multivariate normal.

Since $\Sigma$ is symmetric and positive definite, it can be shown that there exists a matrix $\Sigma^{1/2}$, the square root of $\Sigma$ with the following properties

(i) $\Sigma^{1/2}$ is symmetric

(ii) $\Sigma = \Sigma^{1/2}\Sigma^{1/2}$

(iii) $\Sigma^{1/2}\Sigma^{-1/2} = \Sigma^{-1/2}\Sigma^{1/2} = I$ where $\Sigma^{-1/2} = (\Sigma^{1/2})^{-1}$

## 2.43 Theorem

If $Z \sim N(0,1)$ and $X = \mu + \Sigma^{1/2}Z$, then $X \sim N(\mu, \Sigma)$.

Conversely, if $X \sim N(\mu, \Sigma)$, then $\Sigma^{-1/2}(X-\mu) \sim N(0,1)$

## 2.44 Theorem

Suppose we partition a random Normal vector $X$ as $X = (X_a, X_b)$. We can also partition $\mu = (\mu_a, \mu_b)$ and

\[[ \Sigma = \begin{pmatrix} \Sigma_{aa} & \Sigma_{ab} \\\ \Sigma_{ba} & \Sigma_{bb} \end{pmatrix} \]]

Now, let $X \sim N(\mu, \Sigma)$. Then,

(i) The marginal distribution of $X_a$ is $X_a \sim N(\mu_a, \Sigma_{aa})$

(ii) The conditional distribution of $X_b$ given $X_a = x_a$ is

\[[ X_b \vert X_a = x_a \sim N(\mu_b + \Sigma_{ba}\Sigma_{aa}^{-1}(x_a - \mu_a), \Sigma_{bb}-\Sigma_{bb}\Sigma_{aa}^{-1}\Sigma_{ab}) \]]

(iii) If $a$ is a vector then $a^TX \sim N(a^T\mu, a^T\Sigma a)$

(iv) $V = (X - \mu)^T \Sigma^{-1}(X-\mu) \sim \chi_k^2$

> # References

[1] All of Statistics by Larry A. Wasserman
