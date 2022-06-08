---
layout: single
title: "[Linear Algbera] 6.1 Eigenvalues and Eigenvectors"
categories: ["linearalgebra"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Keywords

**[1]** An **eigenvector** $x$ lies along the same line as $Ax$: $Ax=\lambda x$. The **eigenvalue** is $\lambda$.

**[2]** If $Ax=\lambda x$, then $A^2x=\lambda^2x$ and $A^{-1}x=\lambda^{-1}x$ and $(A+cI)x=(\lambda+c)x$; the same $x$

**[3]** If $Ax=\lambda x$, then $(A-\lambda I)x=0$ and $A-\lambda I$ is singular and $det(A-\lambda I)=0$: $n$ eigenvalues

**[4]** Check $\lambda's$ by $det(A) = (\lambda_1)(\lambda_2)\cdots(\lambda_n)$ and diagonal sum $a_{11}+a_{22}+ \cdots + a_{nn}=$ sum of $\lambda's$

**[5]** Projections have $\lambda=1$ and $0$. Reflections have $1$ and $-1$. Rotations have $e^{i \theta}$ and $e^{-i \theta}$: complex

> # Eigenvalues & Eigenvectors

Suppose you have a vector $x$ and you compute $Ax$. It's very likely that the **direction** of $x$ when multiplied with $A$ **will change**. However, there would be some $x$ that **will not change its direction** even multiplied with $A$ but only the **magnitude** will change. Those special vectors that don't change direction when you multiply by $A$ are called **eigenvectors**. Then, the resulting $Ax$ will be $x$ multiplied by some **constant**. We call this constant **eigenvalue** $\lambda$.

\[[ Ax=\lambda x \]]

Eigenvalue $\lambda$ tells whether the eigenvector $x$ is stretched, reveresed, shrunk, or unchanged when it's multiplied by $A$. $\lambda$ could be 0 too which means $x$ is in nullspace.

> When $A^n$, the **eigenvectors** stay the same. The **eigenvalues** are squared.

This is because eigenvectors stay in their own directions but only its magnitude (eigenvalue) changes. Other vectors change directions but they're **combinations** of the eigenvectors.

> # Projection Matrix $P$

For projection matrix $P$, when is $Px$ parallel to $x$? Recall that if you project more than once, the result is the same as projecting once. The eigenvectors for $\lambda=1$ and $\lambda=0$ **fill the column space** and **nullspace**. The column space doesn't move $(Px=x)$. The nullspace goes to zero $(Px=0x)$.

> # The Equation for the Eigenvalues

**[1]** Big Formula: $Ax=\lambda x$

**[2]** $(A-\lambda I)x=0$ : eigenvectors make up $N(A-\lambda I)$

**[3]** $\lambda$ is eigenvalue **if and only if** $A-\lambda I$ is **singular**

**[4]** Solve $det(A-\lambda I)=0$ to get $\lambda$'s (repeats ok)

**[5]** For each $\lambda$, solve $(A-\lambda I)x$ or $Ax=\lambda x$ to find **eigenvector**

**[NOTES]**

If $A$ is **invertible**, zero is not an eigenvalue. If $A$ is **singular**, the eigenvectors for $\lambda = 0$ fill the nullspace $N(A)$. Thus, we "shift" $A$ by $\lambda I$ to make it singular.

> # Determinant and Trace

**Elimination does not preserve the** $\lambda's$. The triangular $U$ has "its" eigenvalues sitting along the **diagonal**. But they're NOT the eigenvalues of $A$!

A good news is that we can quickly check if we got the correct eigenvalues by the product and the sum.

> The **product** of $n$ eigenvalues equals the **determinant**

> The **sum** of the $n$ eigenvalues equals the **sum of the n diagonal entries**

## Trace

The sum of the entries along the main diagonal is called the **trace** of $A$

\[[ \lambda_1 + \lambda_2 + \cdots + \lambda_n = \textbf{trace} = a_{11} + a_{22} + \cdots + a_{nn} \]]

> # Imaginary Eigenvalues

The eigenvalues might not be real numbers. For example, the 90 degrees rotation $Q=\begin{bmatrix}0 & -1 \\\ 1 & 0 \end{bmatrix}$ has no real eigenvectors.

\[[ \lambda_1 = i\ \ \ \ \lambda_2 = -i \]]

Then, $\lambda_1 \lambda_2 = \textbf{trace}=0$ and $\lambda_1\lambda_2=\textbf{determinant}=1$

> # Eigenvalues of $AB$ and $A+B$

Keep in mind that an eigenvalue $\lambda_1$ of $A$ times an eigenvalue $\lambda_2$ of $B$ usually **does not** give an eigenvalue of $AB$.

Instead, when all $n$ eigenvalues are **shared**, we can multiply eigenvalues.

> $A$ and $B$ share the same $n$ independent eigenvectors **if and only if** $AB=BA$

> # References

[1] Introduction to Linear Algebra, 5th edition
