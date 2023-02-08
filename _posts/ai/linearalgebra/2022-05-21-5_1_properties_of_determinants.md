---
layout: post
title: "[Linear Algbera] 5.1 Properties of Determinant"
subtitle: ""
categories: ai
tags: linearalgebra
comments:
---

> # Keywords

**[1]** The **determinant** of $$A = \begin{bmatrix} a & b \\\ c & d \end{bmatrix}$$ is $$ad-bc$$. Singular matrix $$A = \begin{bmatrix} a & xa \\\ c & xc \end{bmatrix}$$ has **det = 0**.

**[2]** **Row change reverses signs**: $$PA = \begin{bmatrix} 0 & 1 \\\ 1 & 0\end{bmatrix} \begin{bmatrix} c & d \\\ a & b \end{bmatrix}$$ has $$det(PA) = bc-ad=-det(A)$$

**[3]** The determinant of $$\begin{bmatrix} xa & yA & xb + yB \\\ c & d\end{bmatrix}$$ is $$x(ad-bc) + y(Ad-Bc)$$: Determinant is **linear** in **row 1** by itself.

**[4]** Elimination $$EA = \begin{bmatrix} a & b \\\ 0 & d-\frac{c}{a}b \end{bmatrix}$$, $$det(EA)=a(d-\frac{c}{a}b)$$ = **product of pivots** = $$det(A)$$

**[5]** If $$A$$ is $$n$$ by $$n$$ then **[1], [2], [3], [4]** remain true and always $$det(BA) = det(B)det(A)$$ and $$det(A^T)=det(A)$$

> # Determinant

The determinant of a square matrix is a **single number**.

The determinant has **zero** when the matrix has **no inverse**. When $$A$$ is invertible, $$det(A^{-1}) = 1\ /\ (det(A))$$

$$ A = \begin{bmatrix} a & b \\\ c & d \end{bmatrix} $$

$$ det(A) = \lvert A \rvert = ad - bc $$

$$ A^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\\ -c & a \end{bmatrix} $$

## Product of Pivots

The **product of the pivots** is the **determinant**:

$$ a\left(d - \frac{c}{a}b\right) = ad - bc = det(A) $$

> # Determinant Rules

## [1] The determinant of $$n$$ by $$n$$ **identity matrix** if $$1$$.

$$ \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} = 1 $$

## [2] The determinant changes sign when two rows are exchanged (sign reversal)

$$ \begin{vmatrix} c & d \\\ a & b \end{vmatrix} = -\begin{vmatrix} a & b \\\ c & d\end{vmatrix} $$

From this property, we can find $$det(P)$$ for any permutation matrix. If there was an **even** number of row changes, then $$det(P)=1$$, when there's an **odd** number of row exchanges, $$det(P)=-1$$.

## [3] The determinant is a **linear function** of **each row separately** (other rows stay fixed)

If the first row is multiplied by $$t$$, the determinant is multiplied by $$t$$. If the first rows are added, the determinants are added. Remember that this rule only applies when the **other rows don't change**!

$$ \begin{vmatrix} ta & tb \\\ c d \end{vmatrix} = t\begin{vmatrix} a & b \\\ c & d \end{vmatrix} $$

$$ \begin{vmatrix} a+a' & b+b' \\\ c & d\end{vmatrix} = \begin{vmatrix} a & b \\\ c & d\end{vmatrix} + \begin{vmatrix} a' & b' \\\ c & d \end{vmatrix} $$

This rule also applies to $$n$$ by $$n$$ matrix $$A$$ when **only one row changes**

$$ A = \begin{vmatrix} \textbf{4} & \textbf{8} & \textbf{8} \\\ 0 & 1 & 1 \\\ 0 & 0 & 1\end{vmatrix} = \textbf{4}\begin{vmatrix} \textbf{1} & \textbf{2} & \textbf{2} \\\ 0 & 1 & 1 \\\ 0 & 0 & 1\end{vmatrix} $$

$$ \begin{vmatrix} \textbf{4} & \textbf{8} & \textbf{8} \\\ 0 & 1 & 1 \\\ 0 & 0 & 1 \end{vmatrix} = \begin{vmatrix} \textbf{4} & \textbf{0} & \textbf{0} \\\ 0 & 1 & 1 \\\ 0 & 0 & 1\end{vmatrix} + \begin{vmatrix} \textbf{0} & \textbf{8} & \textbf{8} \\\ 0 & 1 & 1 \\\ 0 & 0 & 1\end{vmatrix} $$

**[WARNING!]** This linearity **DOES NOT** mean $$det(A+B) = det(A) + det(B)$$! This is false

For example, $$det(2I) \neq 2det(I)$$. To obtain $$2I$$, we have to multiply **both rows by 2**. Hence,

$$ \begin{vmatrix} t & 0 \\\ 0 & t\end{vmatrix} = t^2 $$

## [4] If two rows of $$A$$ are equal, then $$det(A)=0$$

Intuitively, a matrix with two equals rows is **singular** so its determinant must be zero. Another reasoning is from rule [2]. If we exchange the two identical rows, the sign changes but since it's still the same matrix, the only number which satisfies $$ -D=D $$ is $$0$$.

## [5] Subtracting a multiple of one row from another row leaves $$det(A)$$ unchanged

$$ \begin{vmatrix} a & b \\\ c-la & d-lb\end{vmatrix} = \begin{vmatrix} a & b \\\ c & d \end{vmatrix} $$

Rule [3] splits the left side into the right side plus $$-l\begin{vmatrix} a & b \\\ a & b\end{vmatrix}$$ which is equal to $$0$$ by rule [4].

The determinant is **not changed** by the usual elimination from $$A$$ to $$U$$ (except possibly sign): $$det(A)=\pm(U)$$.

## [6] A matrix with a row of zeros has $$det(A)=0$$

Add a non-zero row to a zero row then the matrix has two equal rows so $$det(A)=0$$.

## [7] If $$A$$ is triangular then $$det(A)=a_{11}a_{22}\cdots a_{nn}$$ = product of diagonal entries

Suppose all diagonal entries are **nonzero**. Remove the off-diagonal entries by elimination. By rule [5], the determinant is not changed. Using rule [3], factor each diagonal entry sequentially. Then the determinant becomes the **product of pivots**.

## [8] If $$A$$ is singular, then $$det(A)=0$$. If $$A$$ is invertible then $$det(A) \neq 0$$

If $$A$$ is **signular** then the eliminated matrix $$U$$ has a zero row so its determinant is $$0$$. If $$A$$ is invertible, then $$U$$ has the pivots along its diagonal.

## [9] $$det(AB) = det(A)det(B)$$

When $$B=A^{-1}$$, the formula becomes $$det(I) = det(A)det(A^{-1})$$ where $$det(I) = 1$$.

$$ det(A) det(A^{-1}) = 1 $$

## [10] $$det(A^T)=det(A)$$

For example,

$$ \begin{vmatrix} a & b \\\ c & d\end{vmatrix} = \begin{vmatrix} a & c \\\ b & d\end{vmatrix} $$

> # Every rule also works for columns!

Every rule for the rows we talked about also apply to the **columns** since $$\lvert A \rvert = \lvert A^T \rvert$$.

> # References

[1] Introduction to Linear Algebra, 5th edition
