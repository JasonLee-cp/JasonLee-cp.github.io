---
layout: single
title: "[Linear Algbera] 2.5 Inverse Matrices"
categories: ["linearalgebra"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Keywords

[1] If the square matrix $A$ has an inverse, then $A^{-1}A=I$ and $AA^{-1}=I$

[2] The **algorithm** to test invertibility is **elimination**: $A$ must have $n$ nonzero pivots

[3] The **algebra** test for invertibility is the **determinant** of $A$: $det(A)$ must not be zero

[4] The **equation** that tests for invertibility is $Ax=0$: $x=0$ must be the **only solution**.

[5] If $A$ and $B$ (same size) are invertible, then $AB$ is also invertible: $(AB)^{-1}=B^{-1}A^{-1}$.

[6] $AA^{-1}=I$ is $n$ equations for $n$ columns of $A^{-1}$. Gauss-Jordan eliminates $[AI]$ to $IA^{-1}$

> # Inverse matrix and Invertible

Suppose $A$ is a square matrix. Intuitively, the **inverse** matrix $A^{-1}$ (same size) is a matrix that **undoes** what $A$ does. Hence, their product is the identity matrix which does nothing to a vector so $A^{-1}A=x$.

The matrix $A$ is **invertible** if there exists a matrix $A^{-1}$ such that

\[[ A^{-1}A = I\ \text{and}\ AA^{-1}=I \]]

However, a matrix does not always have an inverse. Below are some notes about $A^{-1}$.

**[Note 1]** The inverrse exists if and only if elimination produces $n$ pivot

**[Note 2]** $A$ cannot have two different inverses

**[Note 3]** If $A$ is invertible, the only and only solution to $Ax=b$ is $x=A^{-1}b$

**[Note 4]** Suppose there is a nonzero vector $x$ such that $Ax=0$. Then $A$ is not invertible.

**[Note 5]** $A$ is invertible if and only if its determinant is not zero

**[Note 6]** A diagonal matrix has an inverse provided no diagonal entries are zero

> # Inverse of a Product AB

The product $AB$ has an inverse if and only if $A$ and $B$ of the same size are separately invertible. Note that the $A^{-1}$ and $B^{-1}$ come in the **reverse order**

If $A$ and $B$ are invertible then so is $AB$. The inverse of $AB$ is

\[[ (AB)^{-1} = B^{-1}A^{-1} \]]

The reasons it comes in reverse order is $(AB)(B^{-1}A^{-1})=I$ and $(B^{-1}A^{-1})(AB) = I$

> # Calculate Inverse by Gauss-Jordan Elimination

Elimination goes directly to $x$ without needing to calculate $A^{-1}$. The Gauss-Jordan elimination is to solve $AA^{-1}=I$, finding each column of $A^{-1}$. $A$ multiplies the first column of $A^{-1}$ (call $x_1$) to give the first column of $I$ (call $e_1$). So each of the columns $x_1, x_2, x_3$ of $A^{-1}$ is multiplied by $A$ to produce a column of $I$:

\[[ AA^{-1} = A[x_1\ x_2\ x_3] = [e_1\ e_2\ e_3] = I \]]

To invert $A$, we have to solve three systems of equations: $Ax_1 = e_1$, $Ax_2=e_2$, and $Ax_3=x_3$. Gauss-Jordan elimination finds $A^{-1}$ by solving **all n equations together**.

The **augmented matrix** $[A\ I]$ is used where $e_1, e_2, e_3$ are in the columns of $I$. With the similar elimination strategy, we perform elimination on this augmented matrix. Our goal is to make the left-side $A$ down to $I$. What this means is that if $A$ turns into $A^{-1}$ by elimination, our elimination matrix is indeed $A^{-1}$. Since the elimination is equally performed on $A$ and $I$, we get $IA^{-1} = A^{-1}$ on the right side. Hence, finally we get our target $A^{-1}$.

Let's find the inverse of matrix $K$.

\[[ K=\begin{bmatrix}2 & -1 & 0 \\\ -1 & 2 & -1 \\\ 0 & -1 & 2 \end{bmatrix} \]]

[1] Construct Augmented matrix $[K\ I]$

\[[ K=\begin{bmatrix}2 & -1 & 0 & 1 & 0 & 0 \\\ -1 & 2 & -1 & 0 & 1 & 0 \\\ 0 & -1 & 2 & 0 & 0 & 1\end{bmatrix} \]]

[2] Perform elimination to get **reduced echelon form** $R=I$.

\[[ K=\begin{bmatrix}1 & 0 & 0 & \frac{3}{4} & \frac{1}{2} & \frac{1}{4} \\\ 0 & 1 & 0 & \frac{1}{2} & 1 & \frac{1}{2} \\\ 0 & 0 & 1 & \frac{1}{4} & \frac{1}{2} & \frac{3}{4} \end{bmatrix} \]]

We got from $[K\ I]$ to $[I\ ?]$. Since $K$ becomes $I$, it turns out that we in fact multiplied the augmented matrix by the **inverse matrix** $K^{-1}$.

## Summary

\[[ \text{Multiply}\ [A\ I]\ \text{by}\ A^{-1}\ \text{to get}\ [I\ A^{-1}] \]]

> # Diagonally dominant matrices are invertible

Diagonally dominant matrices are invertible. Each $a_{ii}$ on the diagonal is larger than the total sum along the rest of row $i$. On every row,

\[[ \lvert a_{ii} \rvert > \sum_{j \neq i} \lvert a_{ij} \vert \]]

For example,

\[[ A = \begin{bmatrix} 3 & 1 & 1 \\\ 1 & 3 & 1 \\\ 1 & 1 & 3 \end{bmatrix} \]]

$A$ is a diagonally dominant matrix. Hence, $A$ is invertible.

> # Exercises

## Q7

If $A$ has row 1 + row 2 = row 3, show that $A$ is not invertible:

Set $A = \begin{bmatrix} \vec{a_1} \\\ \vec{a_2} \\\ \vec{a_3} \end{bmatrix}$ and $\vec{a_1} + \vec{a_2} = \vec{a_3}$

(a) Explain why $Ax = (0,0,1)$ cannot have a solution. Add eqn 1 + eqn 2

It must satisfy that $\vec{a_1} \cdot x = 0$, $\vec{a_2} \cdot x = 0$ and $\vec{a_3} \cdot x = 1$

However, since $\vec{a_3} \cdot x = 1$ is $(\vec{a_1}+\vec{a_2}) \cdot x = 1$, it gives $0=1$ which is contradictory.

(b) Which right sides $(b_1, b_2, b_3)$ might allow a solution to $Ax = b$?

$b_1 + b_2 = b_3$. Otherwise, it gives contradition like (a).

(c) In elimination, what happens to equation 3?

Row 3 becomes a row of zeros so there's no pivot. Hence, it's not invertible.

> # References

[1] Introduction to Linear Algebra, 5th Edition
