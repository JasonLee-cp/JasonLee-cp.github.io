---
layout: post
title: "[Statistics] 3.4 Expectations and Variance of Important Random Variables"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Expectation and Variance

| ![joint](..//assets/img/MATH/statistics/ch3_1.png) |
| :------------------------------------------------: |
|                _All of Statistics_                 |

> # Multivariate Models

The last two distributions are **multivariate** models which involve a **random vector** $$X$$ instead of a single random variable,

$$ X = \begin{pmatrix} X_1 \\\ \vdots \\\ X_k \end{pmatrix} $$

The **mean** of a random vector $$X$$ is defined as

$$ \mu = \begin{pmatrix} \mu_1 \\\ \vdots \\\ \mu_k \end{pmatrix} = \begin{pmatrix} \mathbb{E}[X_1] \\\ \vdots \\\ \mathbb{E}[X_k] \end{pmatrix} $$

## Variance-covariance matrix $$\Sigma$$

Then, the **variance-covariance matrix** $$\Sigma$$ is defined as

$$ V(X) = \begin{pmatrix} V(X_1) & Cov(X_1,X_2) & \cdots & Cov(X_1, X_k) \\\ Cov(X_2,X_1) & V(X_2) & \cdots & Cov(X_2, X_k) \\\ \vdots & \vdots & \vdots & \vdots \\\ Cov(X_k, X_1) & Cov(X_k, X_2) & \cdots & V(X_k)\end{pmatrix} $$

Notice the diagonals hold the variance of each random variable $$X_i$$.

> # 3.21 Lemma

If $$a$$ is a **vector** and $$X$$ is a random vector with **mean** $$\mu$$ and **variance** $$\Sigma$$, then

$$ \mathbb{E}[a^TX]=a^T\mu $$

$$ V(a^TX)=a^T \Sigma a $$

If $$A$$ is a **matrix**, then

$$ \mathbb{E}[AX]=A\mu $$

$$ V(AX)=A \Sigma A^T $$

> # References

[1] All of Statistics by Larry A. Wasserman
