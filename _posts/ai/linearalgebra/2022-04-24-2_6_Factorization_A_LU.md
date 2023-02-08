---
layout: post
title: "[Linear Algbera] 2.6 Factorization A=LU"
subtitle: ""
categories: ai
tags: linearalgebra
comments:
---

> # Keywords

[1] Each elimination step $$E_{ij}$$ is inverted by $$L_{ij}$$. Off the main diagonal change $$-l_{ij}$$ to $$+l_{ij}$$

[2] The The whole forward elimination process (with no row exchanges) is inverted by $$L$$:

$$ L = (L*{21}L*{31}...L*{n1})(L*{32}...L*{n2})(L*{43}...L*{n3})(L*{n\ n-1}) $$

[3] That product matrix $$L$$ is still **lower triangular**. Every multiplier $$l_{ij}$$ is in row $$i$$, column $$j$$.

[4] The original $$A$$ is recovered from $$U$$ by $$A=LU$$

[5] Elimination on $$Ax=b$$ reaches $$Ux=c$$. Then back-substitution solves $$Ux=c$$.

[6] Solving a triangular system takes $$n^2 / 2$$ multiply-subtracts. Elimination to find $$U$$ takes $$n^3/3$$.

> # LU Factorization

May key ideas of linear algebra are **factorizations** of a matrix. One such factorization comes from **elimination**.

The factors $$L$$ and $$U$$ are **triangular matrices**. The factorization that comes from elimination is

$$ A = LU $$.

The idea is simple. Remember the elimination brings a matrix down to the **upper triangular matrix** $$U$$. Then how do we reverse it? The **lower triangular matrix** $$L$$ reverses this process. Hence, if the elimination matrix was $$E$$ then the lower triangular matrix $$L$$ is actually the same as $$E^{-1}$$.

Let's see in details with a 2 by 2 matrix $$A = \begin{bmatrix} 2 & 1 \\\ 6 & 8 \end{bmatrix}$$.

We must **subtract 3 times row 1 from row 2** to eliminate which can be dong using elimination matrix $$E_{21}$$.

$$ E\_{21}A=U $$

$$ E\_{21}A = \begin{bmatrix} 1 & 0 \\\ -3 & 1\end{bmatrix} \begin{bmatrix} 2 & 1 \\\ 6 & 8 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\\ 0 & 5 \end{bmatrix} = U $$

Now, to reverse $$U$$ back to $$A$$, we multiply $$E_{21}^{-1}$$ to get $$A = E_{21}^{-1}U$$

$$ E\_{21}^{-1}U = A $$

$$ E\_{21}^{-1}U = \begin{bmatrix} 1 & 0 \\\ 3 & 1\end{bmatrix}\begin{bmatrix} 2 & 1 \\\ 0 & 5 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\\ 6 & 8 \end{bmatrix} = A $$

The second equation is our factorization $$A = LU$$. Instead of $$E_{21}^{-1}$$ **we write** $$L$$. So $$L$$ is just the **inverse** of the elimination matrix $$E$$.

## Summary

$$ (E*{32}E*{31}E*{21})A = U \Longrightarrow A = (E*{21}^{-1}E*{31}^{-1}E*{32}^{-1})U $$

$$ A = LU $$

> # Notes on A = LU

**(1)** $$A = LU$$ is elimination **without row changes**.

**(2)** The upper triangular $$U$$ has the **pivots** on its diagonal.

**(3)** The lower triangular $$L$$ has all **1's** on its diagonal.

**(4)** The multipliers $$l{ij}$$ are **below** the diagonal of $$L$$.

Let's look at an example. Given a matrix $$A$$, we'll factorize into $$LU$$.

$$ A = \begin{bmatrix} 2 & 1 & 0 \\\ 1 & 2 & 1 \\\ 0 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\\ \frac{1}{2} & 1 & 0 \\\ 0 & \frac{2}{3} & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 & 0 \\\ 0 & \frac{3}{2} & 1 \\\ 0 & 0 & \frac{4}{3} \end{bmatrix} = LU $$

Observe that all the **pivots** in $$U$$ are in its diagonal. The diagonal entries of $$L$$ are all **1's**. All the multipliers $$l_{ij}$$ in $$L$$ are **below** the diagonal.

> # Further into A = LDU

$$A=LU$$ is **unsymmetric** because $$U$$ has the **pivots** on its diagonal but $$L$$ has **1's** which is not that pretty. Fortunately, this is easy to change.

We can simply **Divide U by a diagonal matrix D that contains the pivots** which leaves a new triangular matrix with 1's on the diagonal:

$$ \text{Split U into } \begin{bmatrix}d*1 \\\ & d_2 \\\ & & \ddots \\\ & & & d_n\end{bmatrix} \begin{bmatrix}1 & u*{12}/d*1 & u*{13}/d*1 & \cdot \\\ & 1 & u*{23}/d_2 & \cdot \\\ & & \ddots & \vdots \\\ & & & 1 \end{bmatrix} $$

It is conveinient (but a little confusing) to **keep the same letter** $$U$$ for this new triangular matrix on the right side. It has **1's** on the diagonal (like $$L$$).

The diagonal matrix on the left side is written as $$D$$. Hence, we further factorized the matrix $$A$$ into $$LDU$$.

$$ A = LU\ \text{or }A = LDU $$

> # References

[1] Introduction to Linear Algebra, 5th Edition
