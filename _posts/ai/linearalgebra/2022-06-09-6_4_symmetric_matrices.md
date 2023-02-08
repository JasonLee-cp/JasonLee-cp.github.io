---
layout: post
title: "[Linear Algbera] 6.4 Symmetric Matrices"
subtitle: ""
categories: ai
tags: linearalgebra
comments:
---

> # Keywords

**[1]** A symmetric matrix $$A$$ has $$n$$ **real eigenvalues** $$\lambda_i$$ and $$n$$ **orthonormal eigenvectors** $$q_1,...,q_n$$

**[2]** Every real symmetric $$S$$ can be diagonalized: $$S=Q\Lambda Q^{-1} = Q \Lambda Q^T$$

**[3]** The number of positive eigenvalues of $$S$$ equals the number of positive pivots

**[4]** Antisymmetric matrices $$A=-A^T$$ have imaginary $$\lambda's$$ and orthonormal (complex) q's

> # Symmetric Matrices

Symmetric matrices $$S$$ are the most importance matrices in linear algebra. Eigenvalues and eigenvectors give us great insight about symmetric matrices. We'll look for special properties of the eigenvalues $$\lambda$$ and eigenvectors $$x$$ when $$S=S^T$$.

> What is special about $$Sx=\lambda x$$ when $$S$$ is symmetric?

The diagonalization $$S=X\Lambda X^{-1}$$ reflects the symmetric of $$S$$. If we transpose this equation, we get

$$[ S=X\Lambda X^{-1} $$]

$$[ S^T = (X^{-1})^T \Lambda X^T $$]

They're the same since $$S=S^T$$. Possibly $$X^{-1}$$ in the first equation equals $$X^T$$. Then,

$$[ X^TX=I $$]

which makes each **eigenvector** in $$X$$ **orthogonal** to the other eigenvectors when $$S=S^T$$.

## Key Facts

1. A symmetric matrix has only **real eigenvalues**

2. The **eigenvectors** can be chosen **orthonormal**

Those $$n$$ **orthonormal eigenvectors** go into the columns of $$X$$. **Every symmetric matrix can be diagonalized**. **Its eigenvector matrix** $$X$$ becomes an **orthogonal matrix** $$Q$$.

(Remember that orthogonal matrices have $$Q^{-1}=Q^T$$)

If it want to write $$Q$$ instead of $$X$$, we must "choose" **orthonormal eigenvectors**. The reasons we "choose" is that eigenvectors **do not have to be unit vectors**. Thus, we will choose unit vectors which are orthonormal. Then, $$A=X\Lambda X^{-1}$$ becomes

$$[ S = Q \Lambda Q^T $$]

## Example

Find the $$\lambda's$$ and $$x's$$ for

$$[ S = \begin{bmatrix} 1 & 2 \\\ 2 & 4 \end{bmatrix} $$]

First, we find $$\lambda's$$ by $$det(S-\lambda I)=0$$

$$[ \begin{bmatrix} 1-\lambda & 2 \\\ 2 & 4-\lambda \end{bmatrix} $$]

We have $$(1-\lambda)(4-\lambda)-4=0$$. Then, $$\lambda=0, 5$$. Correspondingly,

$$[ x_1 = \begin{bmatrix} 2 \\\ 1\end{bmatrix},\ \ x_2=\begin{bmatrix} 1 \\\ 2\end{bmatrix} $$]

Notice that the **nullspace** and **column space** are **perpendicular**. The fundamental theorem says the nullspace is perpendicular to **row space** not the column space. But our matrix is **symmetric**! So the row space and the column space are the same. Hence, the eigenvectors are perpendicular.

Now, to find the orthonormal vectors, we divide each eigenvector by its length which is $$\sqrt{5}$$. Finally, we have

## Spectral Theorem

Every symmetric matrix has the factorization $$S=Q\Lambda Q^T$$ with **real eigenvalues** in $$\Lambda$$ and **orthonormal eigenvectors** in the columns of $$Q$$:

$$[ S = Q \Lambda Q^{-1} = Q \Lambda Q^T $$]

since $$Q^{-1} = Q^T$$ for orthogonal matrices

Notice that $$Q \Lambda Q^T$$ is also symmetric. If you take the transpose of it, it's equal to $$Q \Lambda Q^T$$.

> **Real Eigenvalues**: All the eigenvalues of a real symmetric matrix are real

> **Orthogonal Eigenvectors**: Eigenvectors of a real symmetric matrix (when they correspond to different $$\lambda's$$) are always perpendicular

## 2 by 2 symmetric matrix

The eigenvectors of 2 by 2 symmetric matrix have a special form

$$[ S = \begin{bmatrix} a & b \\\ b & c\end{bmatrix} $$]

has

$$[ x_1 = \begin{bmatrix} b \\\ \lambda_1 - a\end{bmatrix}\ \ x_2 = \begin{bmatrix} \lambda_2 - c \\\ b \end{bmatrix} $$]

Notice that $$x_1^Tx_2 = 0$$ since $$\lambda_1 + \lambda_2 = a + c\ (trace)$$

Symmtric matrices $$S$$ have orthogonal eigenvector matrices $$Q$$. For 2 by 2 symmetric matrix,

$$[ S = Q \Lambda Q^T = \begin{bmatrix} \\\ q_1 & q_2 \\\ \end{bmatrix} \begin{bmatrix} \lambda_1 & \\\ & \lambda_2 \end{bmatrix} \begin{bmatrix} q_1^T \\\ q_2^T\end{bmatrix} $$]

This is (**rotation**)(**stretch**)(**rotate back**)

Columns $$q_1$$ and $$q_2$$ multiply rows $$\lambda_1q_1^T$$ and $$\lambda_2 q_2^T$$ to produce $$S=\lambda_1q_1q_1^T + \lambda_2q_2q_2^T$$

> # $$S=Q\Lambda Q^T = \lambda_1q_1q_1^T + \cdots + \lambda_nq_nq_n^T$$

Every symmetric matrix has

$$[ S=Q\Lambda Q^T = \lambda_1q_1q_1^T + \cdots + \lambda_nq_nq_n^T $$]

Here, the eigenvector matrix $$X$$ becomes orthogonal matrix $$Q$$: $$x_i = q_i$$ and $$X=Q$$

Also, $$Q\Lambda Q^T$$ in above equation has **columns** of $$Q\Lambda$$ times **rows** of $$Q^T$$.

> # References

[1] Introduction to Linear Algebra, 5th edition
