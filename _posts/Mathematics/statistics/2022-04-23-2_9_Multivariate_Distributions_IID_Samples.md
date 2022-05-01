---
layout: null
title: "[Statistics] 2.9 Multivariate Distributions and IID Samples"
categories: ["statistics"]
tag: [math]

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Multivariate Distributions and IID Samples

Let $X=(X_1, ..., X_n)$ where $X_1,...,X_n$ are random variables. We call $X$ a **random vector**. Let $f(x_1,...,x_n)$ denote the PDF.

We say that $X_1,...,X_n$ are **independent** if, for every $A_1,...,A_n$,

\[[ P(X_1 \in A_1,...,X_n \in A_n) = \prod_{i=1}^n P(X_i \in A_i) \]]

It suffices to check that $f(x_1,...,x_n) = \prod_{i=1}^nf_{X_i}(x_i)$

> # IID Samples

If $X_1,...,X_n$ are **independent** and each has the **same marginal distribution** with CDF $F$, we say that $X_1,...,X_n$ are **IID** (independent and identically distributed) and we write

\[[ X_1,...,X_n \sim F \]]

If $F$ has density $f$, we also write $X_1,...,X_n \sim f$. We also call $X_1,...,X_n$ a **random sample of size n from** $F$.

> # References

[1] All of Statistics by Larry A. Wasserman
