---
layout: post
title: "[Linear Algbera] 4.4 Orthonormal bases and Gram-Schmidt"
subtitle: ""
categories: ai
tags: linearalgebra
comments:
---

> # Keywords

**[1]** The columns $$q_1,...,q_n$$ are orthonormal if $$q_i^Tq_j = \begin{cases} 0\ \text{for}\ i \neq j \\\ 1 \text{for}\ i = j \end{cases}$$

**[2]** If $$Q$$ is also square, then $$QQ^T=I$$ and $$Q^T=Q^{-1}$$. $$Q$$ is an "orthogonal matrix"

**[3]** The least squares solution to $$Qx=b$$ is $$\hat{x}=Q^Tb$$. Projection of $$b$$: $$p=QQ^Tb = Pb$$

**[4]** The **Gram-Schmidt** process takes independent $$a_i$$ to orthonormal $$q_i$$. Start with $$q_1 = \frac{a_1}{\lVert a_1 \rVert}$$

**[5]** $$q_i$$ is $$(a*i - projection p_i) / \lVert a_i - p_i \rVert$$; projection $$p_i = (a_i^Tq_1)q_1 + \cdots + (a_i^Tq*{i-1})q\_{i-1}$$

**[6]** Each $$a_i$$ will be combination of $$q_1$$ to $$q_i$$. Then $$A=QR$$: orthogonal $$Q$$ and triangular $$R$$.

> # Orthonormal

Orthogonality is good. When the dot products are zero so $$A^TA$$ will be diagonal. It becomes so easy to find $$\hat{x}$$ and $$p=A\hat{x}$$.

## Orthogonal vectors

The vectors $$q_1,...,q_n$$ are **orthogonal** when their dot products $$q_i \cdot q_j$$ are **zero**. More exactly, $$q_i^Tq_j=0$$ whenever $$i \neq j$$.

## Orthonormal

From orthogonal vectors, if we **divide each vector by its length**, we get **orthogonal unit vectors**. Their lengths are all $$1$$. This basis is called **orthonormal**

The vectors $$q_1,...,q_n$$ are **orthonormal** if

$$ q_i^Tq_j = \begin{cases} 0\ \text{for}\ i \neq j \\\ 1 \text{for}\ i = j \end{cases} $$

A matrix with **orthonormal columns** is assigned the special letter $$Q$$.

## $$Q^TQ = I$$

The matrix $$Q$$ with orthonormal columns satisfy $$Q^TQ=I$$. Notice that $$Q$$ **doesn't have to be square**.

The reason $$Q^Q=I$$ is that $$q_i^Tq_j = 0$$ if $$i \neq j$$ and $$q_i^Tq_j=1$$ if $$i = j$$.

## Square $$Q$$

When $$Q$$ happens to be **square**, then $$Q^TQ=I$$ implies $$Q^T=Q^{-1}$$: transpose = inverse. It also satifies $$QQ^T=I$$.

In this square case, we call $$Q$$ an **orthogonal matrix**.

> # References

[1] Introduction to Linear Algebra, 5th edition
