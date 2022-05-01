---
layout: single
title: "[Linear Algbera] 2.7 Transpose and Permutation"
categories: ["linearalgebra"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Keywords

**[1]** $(Ax)^{T} = x^{T}A^{T}$, $(AB)^{T}=B^{T}A^{T}, (A^{-1})^T = (A^T)^{-1}$

**[2]** The **dot product** (inner product) is $x \cdot y = x^Ty$. This is $(1 \times n)(n \times 1) = (1 \times 1)$.

**[3]** The idea behind $A^T$ is that $Ax \cdot y$ equals $x \cdot A^Ty$ because $(Ax)^Ty = x^TA^Ty = x \cdot A^Ty$

**[4]** A **symmetric matrix** $S$ has $S^T = S$ and the product $A^TA$ is always symmetric

**[5]** An **orthogonal matrix** $Q$ has $Q^T = Q^{-1}$. The columns of $Q$ are **orthogonal unit vectors**.

**[6]** A **permutation matrix** $P$ has the same rows as $I$ in any order. There are $n!$ different orders

**[7]** Then $Px$ puts the components $x_1,x_2,...,x_n$ in that new order. And $P^T$ equals $P^{-1}$.

> # Transpose

If $A$ is an $m \times n$ matrix, the **transpose** is $n \times m$:

\[[ A = \begin{bmatrix} 1 & 2 & 3 \\\ 0 & 0 & 4 \end{bmatrix}\ \text{then } A^T = \begin{bmatrix} 1 & 0 \\\ 2 & 0 \\\ 3 & 4\end{bmatrix} \]]

\[[ (A^T)\_{ij} = A\_{ji} \]]

## Transpose Rules

**Sum** $(A+B)^T = A^T + B^T$

**Product** $(AB)^T = B^TA^T$

**Inverse** $(A^{-1})^T = (A^T)^{-1}$

> # Why $(AB)^T = B^TA^T ?$

Notice that $(AB)^T = B^TA^T$ comes in **reverse order**. Let's get the sense of it. For simplicity, let's observe $(Ax)^T = x^TA^T$, where $x$ is a vector.

Remember that $Ax$ combines the **columns** of $A$.

\[[ \begin{bmatrix} a & b \\\ c & d \end{bmatrix} \begin{bmatrix} x_1 \\\ x_2\end{bmatrix} = \begin{bmatrix} a \\\ c \end{bmatrix}x_1 + \begin{bmatrix} b \\\ d\end{bmatrix}x_2 = \begin{bmatrix} ax_1 + bx_2 \\\ cx_1 + dx_2 \end{bmatrix} \]].

On the other hand, $x^TA^T$ combines the **rows** of $A^T$

\[[ \begin{bmatrix} x_1 & x_2\end{bmatrix} \begin{bmatrix} a & c \\\ b & d\end{bmatrix} = x_1 \begin{bmatrix} a & c\end{bmatrix} + x_2 \begin{bmatrix} b & d \end{bmatrix} = \begin{bmatrix} ax_1 + bx_2 & cx_1 + dx_2\end{bmatrix} \]]

> $Ax$ combines the columns of $A$ while $x^TA^T$ combines the rows of $A^T$

This is the **same combination** of the **same vectors**! In $A$, they're columns, in $A^T$ they're rows. Therefore, it makes sense that the transpose of the column $Ax$ is the row $x^TA^T$.

Now let's go back to $(AB)^T = B^TA^T$. Suppose $B = [x_1\ x_2]$ has two columns. We can apply the same idea above to each column. The columns of $AB$ are $Ax_1$ and $Ax_2$. Then,

\[[ \text{Transposing}\ AB = \begin{bmatrix} \\\ Ax_1 & Ax_2 \\\ \\\ \end{bmatrix}\ \text{gives} \begin{bmatrix} x_1^TA^T \\\ x_2^TA^T\end{bmatrix} = B^TA^T \]]

$B^TA^T$ comes out **a row at a time** while $AB$ comes out **a column at a time**.

\[[ AB = \begin{bmatrix} 1 & 0 \\\ 1 & 1\end{bmatrix}\begin{bmatrix} 5 & 0 \\\ 4 & 1\end{bmatrix} = \begin{bmatrix} 5 & 0 \\\ 9 & 1 \end{bmatrix} \]]

\[[ B^TA^T = \begin{bmatrix} 5 & 4 \\\ 0 & 1\end{bmatrix}\begin{bmatrix} 1 & 1 \\\ 0 & 1\end{bmatrix} = \begin{bmatrix} 5 & 9 \\\ 0 & 1 \end{bmatrix} \]]

The same rule applies to three or more factors: $(ABC)^T = C^TB^TA^T$.

> # Transpose of Inverse

Why is $(A^T)^{-1} = (A^{-1})^T$? We can use the $(AB)^T$ formula to prove it. Let's take transpose of $A^{-1}A=I$.

\[[ (A^{-1}A)^T = I^T \]]

\[[ A^T(A^{-1})^T = I \]]

Since $A^T$ and $(A^{-1})^T$ multiply to the identity matrix, we confirm that $(A^{-1})^T$ is the **inverse** of $A^T$.

Therefore,

\[[ (A^{-1})^T = (A^T)^{-1} \]]

Notice especially: $A^T$ **is invertible exactly when** $A$ **is invertible**.

> # Symmetric Matrices

A **symmetric matrix** has $S^T = S$. This means $s_{ji} = s_{ij}$. Since this is a very important matrix, we give special letter $S$.

\[[ S = \begin{bmatrix} 1 & 2 \\\ 2 & 5\end{bmatrix} = S^T \]]

## Inverse of S is also symmetric

We can simply prove it using $(A^{1})^T = (A^T)^{-1}$ property.

\[[ (S^{-1})^T = (S^T)^{-1} = S^{-1} \]]

Therefore, the transpose of a symmetric matrix is also symmetric (when $S$ is invertible).

## Symmetric Products $A^TA$, $AA^T$, $LDL^T$

Choose any matrix $A$. Then, $S = A^TA$ is automatically a **square symmetric matrix**.

Proof is simple. Let's observet the $(i,j)^{th}$ entry of $A^TA$.

$A^TA_{ij}$ is the dot product of row $A^T_i$ and column $A_j$. Now,

$A^TA_{ji}$ is the dot product of row $A^T_j$ and column $A_i$.

Then, using the definition of transpose, the row $A^T_j$ is equal to the column $A_j$ and column $A_i$ is equal to the row $A^T_i$. Hence, $A^TA$ is symmetric.

We can also show that $AA^T$ is also a **square symmetric matrix**. Keep in mind that it's a different matrix from $A^TA$.

## Symmetric Factorization $S=LDL^T$

$S^T = S$ makes elimination faster, maybe even beautiful. I sometimes think math is beautiful. Although it's true that nothing is in fact magical but perfectly logical and is the way it should be, it often gets me surprised. Symmetric factorization is one of them.

The symmetric does not lie in $S=LD$ but is in the **triple product** $S = LDU$. With a symmetric square matrix, $S=LDU$ becomes $S=LDL^T$ where $U$ is just the transpose of $L$.

\[[ \begin{bmatrix} 1 & 2 \\\ 2 & 7\end{bmatrix} = \begin{bmatrix} 1 & 0 \\\ 2 & 1\end{bmatrix} \begin{bmatrix} 1 & 0 \\\ 0 & 3\end{bmatrix} \begin{bmatrix} 1 & 2 \\\ 0 & 1\end{bmatrix} \]]

Now $U=L^T$. The diagonal matrix $D$ containing pivots is of course symmetric itself.

\[[ \text{The symmetric factorization of a symmetric matrix is }S = LDL^T \]]

> # Permutation Matrices

A permutation matrix $P$ "permutes" rows of a matrix. This means that a permutation matrix $P$ has the **rows of the identity matrix I in any order**. $P$ has a single $1$ in every row and every column. Hence, $P^T$ is also a permutation matrix. Any dot product $P_1P_2$ is again a permutation matrix. The simplest permutation matrix is $P = I$ (no exchanges). The next simplest permutation matrix is **row changes** $P_{ij}$ which exchanges row $i$ and $j$.

\[[ I = \begin{bmatrix} 1 & & \\\ & 1 & \\\ & & 1 \end{bmatrix}\ P_{21}= \begin{bmatrix} & 1 & \\\ 1 & & \\\ & & 1 \end{bmatrix} \]]

Of course, there are total of $n!$ permutation matrices of order $n$.

## $P^{-1}$ is also a permutation matrix

The inverse of $P$, $P^{-1}$, is also a permutation matrix. Intuitively it makes sense because the inverse matrix **undoes** that the original matrix did. The permutation matrix $P$ permuted a matrix so in order to get it back to the original, the inverse also must be a permutation matrix!

\[[ I = \begin{bmatrix} 1 & & \\\ & 1 & \\\ & & 1 \end{bmatrix}\ P_{21}= \begin{bmatrix} & 1 & \\\ 1 & & \\\ & & 1 \end{bmatrix}\ P_{32}P_{21}=\begin{bmatrix} & 1 & \\\ & & 1 \\\ 1 & & \end{bmatrix} \]]

\[[ P_{31} = \begin{bmatrix} & & 1 \\\ & 1 & \\\ 1 & & \end{bmatrix}\ P_{32}= \begin{bmatrix} 1 & & \\\ & & 1 \\\ & 1 & \end{bmatrix}\ P_{21}P_{32}=\begin{bmatrix} & & 1 \\\ 1 & & \\\ & 1 & \end{bmatrix} \]]

In the above matrices,

$I, P_{21}, P_{31}, P_{32}$ are their **own inverses** and **own transpose**.

$P_{32}P_{21}$ and $P_{21}P_{32}$ are **inverse** and **transpose**(proof next section) of **each other** since their **order is reversed**.

## $P^{-1} = P^T$

An important thing is that

\[[ P^{-1} = P^T \]]

The two matrices $P_{32}P_{21}$ and $P_{21}P_{32}$ are **transpose** and **inverse** of each other. The proof is simple.

When we multiply $PP^T$, the "1" in the first row of $P$ hits the "1" in the first column of $P^T$ since the first row of $P$ is the first column of $P^T$. It misses all the other ones in all the other columns. Hence, $PP^T=I$.

Therefore, $P^T = P^{-1}$.

> # PA = LU Factorization with Row Exchanges

Remember the elimination factorization $A=LU$. Previously, we assumed that there are no row exchanges. But we can't just assume it because in (most) cases, we need to perform row exchanges for elimination. Here the permutation matrix $P$ comes into play.

Before performing elimination, the permutation matrix $P$ puts the rows in the "right" order. Hence, we can now write full factorization as

\[[ PA = LU \]]

> # References

[1] Introduction to Linear Algebra, 5th Edition
