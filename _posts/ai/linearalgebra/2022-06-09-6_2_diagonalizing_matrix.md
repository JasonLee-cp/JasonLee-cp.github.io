---
layout: post
title: "[Linear Algbera] 6.2 Diagonalizing Matrix"
subtitle: ""
categories: ai
tags: linearalgebra
comments:
---

> # Keywords

**[1]** The columns of $$AX=X\Lambda$$ are $$Ax_k = \lambda_k x_k$$. The eigenvalue matrix $$\Lambda$$ is diagonal

**[2]** $$n$$ independent eigenvectors in $$X$$ diagonalize $$A$$: $$A=X\Lambda X^{-1}$$ and $$\Lambda = X^{-1}AX$$

**[3]** The eigenvector matrix $$X$$ also diagonalizes all powers $$A^k$$: $$A^k = X \Lambda^k X^{-1}$$

**[4]** Solve $$u_{k+1} = Au_k$$ by $$u_k = A^k u_0=X\Lambda^k X^{-1}u_0 = c_1(\lambda_1)^kx_1 + \cdots + c_n(\lambda_n)^k x_n$$

**[5]** **No equal eigenvalues** $$\rightarrow$$ $$X$$ is **invertible** and $$A$$ can be **diagonalized**

**Equal eigenvalues** $$\rightarrow$$ $$A$$ "might" have too few independent eigenvectors. Then $$X^{-1}$$ fails

**[6]** Every matrix $$C=B^{1}AB$$ has the **same eigenvalues** as $$A$$. These $$C's$$ are **similar** to $$A$$

> # Diagonalization

The matrix $$A$$ turns into a **diagonal matrix** $$\Lambda$$ using **eigenvectors**.

Suppose the $$n$$ by $$n$$ matrix $$A$$ has $$n$$ linearly independent eigenvectors $$x_1,...,x_n$$. Put them into the columns of an **eigenvector matrix** $$X$$. Then $$X^{-1}AX$$ is the **eigenvalue matrix** $$\Lambda$$.

$$ X^{-1}AX = \Lambda = \begin{bmatrix} \lambda_1 & & \\\ & \ddots & \\\ & & \lambda_n \end{bmatrix} $$

> # $$AX = X \Lambda$$

The "big formula" is

$$ AX = X\Lambda $$

Let's see why. Notice that $$A$$ multiplies its **eigenvectors** which are columns of $$X$$.

$$ AX = A \begin{bmatrix} & & \\\ x_1 & \cdots & x_n \\\ & & \end{bmatrix} = \begin{bmatrix} & & \\\ \lambda_1x_1 & \cdots & \lambda_nx_n \\\ & & \end{bmatrix} $$

This is because each $$Ax_1 = \lambda x_1$$ by the definition of eigenvalue. Now, let's look at $$X \Lambda$$

$$ X \Lambda = \begin{bmatrix} & & \\\ x_1 & \cdots & x_n \\\ & & \end{bmatrix} \begin{bmatrix} \lambda_1 & & \\\ & \ddots & \\\ & & \lambda_n \end{bmatrix} = \begin{bmatrix} & & \\\ \lambda_1x_1 & \cdots & \lambda_nx_n \\\ & & \end{bmatrix} $$

$$ \therefore AX=X\Lambda $$

From this formula, we also have

$$ A = X\Lambda X^{-1} $$

$$ \Lambda = X^{-1}AX $$

**[NOTE]** We **assume** that the **eigenvectors of A** are **linearly independent**!! Without $$n$$ **independent eigenvectors, we CANNOT diagonalize**.

Now, $$A$$ and $$\Lambda$$ have **same eigenvalues** $$\lambda_1,...,\lambda_n$$ but their **eigenvectors are different**. The job of the original eigenvectors $$x_1,...,x_n$$ was to **diagonlize** $$A$$.

> # $$A^k = X \Lambda^k X^{-1}$$

Now we have a cool formula $$A = X\Lambda X^{-1}$$, it's extremely easy to compute $$A^k$$.

$$ A^k = (X\Lambda X^{-1})(X\Lambda X^{-1})\cdots (X\Lambda X^{-1}) = X\Lambda^k X^{-1} $$

> # 4 Remarks

## Remark 1

Suppose the eigenvalues $$\lambda_1,...,\lambda_n$$ are all different. Then, the eigenvectors $$x_1,...,x_n$$ are **automatically independent**. Consequently, the **eigenvector matrix** $$X$$ will be **invertible**.

> Any matrix that has **no repeated eigenvalues** can be diagonalized

## Remark 2

> We can **multiply** eigenvectors by any **nonzero constants**

$$A(cx) = \lambda(cx)$$ is true. It's good to normalize using this property so that eigenvectors have length 1: $$\lVert x \rVert = 1$$

## Remark 3

> The eigenvectors in $$X$$ come in the **same order** as the eigenvalues in $$\Lambda$$

## Remark 4

> Matrices with too **few eigenvectors** **cannot be diagonalized**

> # Invertibility and Diagonalizability

There is no connection between invertibility and diagonalizability!

> **Invertibility** is concerned with the **eigenvalues** $$\lambda=0$$ or $$\lambda \neq 0$$.

> **Diagonalizability** is concerned with the **eigenvectors** (too few or enough for $$X$$)

Each eigenvalue has at least one eigenvector. If $$(A-\lambda I)x=0$$ gives you $$x=0$$, then $$\lambda$$ is **not** an eigenvalue.

> # Independent $$x$$ from different $$\lambda$$

Eigenvectors $$x_1,...,x_j$$ that correspond to **distinct** eigenvalues are **linearly independent**. An $$n$$ by $$n$$ matrix that has $$n$$ different eigenvalues (no repeated $$\lambda's$$) must be diagonalizable. In short, eigenvectors for $$n$$ different $$\lambda's$$ are independent. Then we can diagonalize $$A$$

> # Similar Matrices: Same Eigenvalues

Suppose the eigenvalue matrix $$\Lambda$$ is fixed and we change the eigenvector matrix $$X$$. Then, we get a family of different matrices $$A=X\Lambda X^{-1}$$ - all with the same eigenvalues in $$\Lambda$$. All those matrices $$A$$ are called **similar**.

This idea extends to matrices that are not diagonalizable. We choose matric $$C$$ (not necessarily $$\Lambda$$) and invertible matrix $$B$$ (instead of $$X$$). Then, we have

$$ A = BCB^{-1} $$

These matrices $$A$$ and $$C$$ are called **similar** and share **same eigenvalues**.

> # Matrix Powers $$A^k$$

The solution to the difference equation $$u_{k+1}=Au_k$$ is

$$ u_k = A^ku_0 = c_1(\lambda_1)^kx_1 + \cdots + c_n (\lambda_n)^k x_n $$

since each step multiplies by $$A$$.

Here,

$$ A^k u_0 = X \Lambda^k X^{-1}u_0 $$

> # References

[1] Introduction to Linear Algebra, 5th edition
