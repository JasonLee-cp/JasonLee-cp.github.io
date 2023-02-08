---
layout: post
title: "[Linear Algbera] 3.3 Complete Solution to Ax=0"
subtitle: ""
categories: ai
tags: linearalgebra
comments:
---

> # Keywords

**[1]** **Complete solution** to $$Ax=b$$: $$x$$ = (one **particular solution** $$x_p$$) + (any $$x_n$$ in the nullspace)

**[2]** Elimination on $$[A\ b]$$ leads to $$[R\ d]$$. Then $$Ax=b$$ is equivalent to $$Rx=d$$

**[3]** $$Ax=b$$ and $$Rx=d$$ are solvable only when all zero rows of $$R$$ have zeros in $$d$$

**[4]** When $$Rx=d$$ is solvable, one very particular solution $$x_p$$ has all free variables equal to zero

**[5]** $$A$$ has **full column rank** $$r=n$$ when its nullspace $$N(A)$$ = zero vector: **no free variables**.

**[6]** $$A$$ has **full row rank** $$r=m$$ when its column space $$C(A)$$ is $$\mathbb{R}^m$$: $$Ax=b$$ is always solvable

**[7]** The four cases are:

(i) $$r=m=n$$: $$A$$ is invertible

(ii) $$r=m<n$$: Every $$Ax=b$$ is solvable

(iii) $$r=n<m$$: (Ax=b) has $$1$$ or $$0$$ solutions

(iv) $$r<m, r<n$$: $$0$$ or $$\infty$$ solutions

> # Augmented matrix [A b]

The nullspace handles the case $$Ax=0$$ when $$b$$ is zero. Elimination further reduces to $$Rx=0$$. Then, the free variables were given "special" values (0 or 1). The pivot variables were found by back substituion. However, we didn't mention the right side $$b$$ since it was zero anyways. Now, $$b$$ **is not zero**. The row operations now act on $$b$$ as well. $$Ax=b$$ is reduced to $$Rx=d$$. A clever way to organize the system is to construct **augmented matrix** with $$b$$.

$$ \begin{bmatrix} 1 & 3 & 0 & 2 \\\ 0 & 0 & 1 & 4 \\\ 1 & 3 & 1 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\\ x_2 \\\ x_3 \\\ x_4 \end{bmatrix} = \begin{bmatrix} \textbf{1} \\\ \textbf{6} \\\ \textbf{7} \end{bmatrix}\ \text{becomes}\ \begin{bmatrix} 1 & 3 & 0 & 2 & \textbf{1} \\\ 0 & 0 & 1 & 4 & \textbf{6} \\\ 1 & 3 & 1 & 6 & \textbf{7} \end{bmatrix} = [A\ b] $$

When we perform elimination on $$A$$ to get $$R$$, we also do the same for $$b$$:

$$ \begin{bmatrix} 1 & 3 & 0 & 2 \\\ 0 & 0 & 1 & 4 \\\ 0 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\\ x_2 \\\ x_3 \\\ x_4 \end{bmatrix} = \begin{bmatrix} \textbf{1} \\\ \textbf{6} \\\ \textbf{0} \end{bmatrix}\ \text{becomes}\ \begin{bmatrix} 1 & 3 & 0 & 3 & \textbf{1} \\\ 0 & 0 & 1 & 4 & \textbf{6} \\\ 0 & 0 & 0 & 0 & \textbf{0} \end{bmatrix} = [A\ b] $$

notice that the **third equation becomes** $$0 = 0$$. So the equations can be solved. If we've done nothing wrong, the right hand side $$b$$ must act the same way as $$A$$.

> # One Particular Solution $$Ax_p = b$$

One easy solutioin $$x_p$$ is when the **free variables are zero**: $$x_2 = x_4 = 0$$. Then, the two nonzero equations give the two pivot variables $$x_1=1, x_3=6$$. Hence, our **particular solution** to $$Ax=b$$ (and also $$Rx=d$$) is

$$ x_p = (1, 0, 6, 0) $$

> The particular solution is obtained when **free variables = 0** and **pivot variables from** $$d$$.

> For a solution to exist, **zero rows** in $$R$$ **must also be zero in** $$d$$. Since $$I$$ is in the **pivot rows and pivot columns of** $$R$$, the pivot variables in $$x_{particular}$$ come from $$d$$.

> # The complete Solution: $$x = x_p + x_n$$

We just learned how to get the **particular solution** $$x_p$$ for $$Ax=b$$. Remember that we could get the **special solutions** for $$Ax=0$$ using free variables.

> $$x_{particular}$$: The **particular solution solves** $$Ax_p = b$$

> $$x_{nullspace}$$: The $$n-r$$ **special solutions solve** $$Ax_n = 0$$

In the example above, we know that $$x_p = (1,0,6,0)$$.

The two special (nullspace) solutions to $$Rx=0$$ come from the two **free columns** of $$R$$: $$(-3, 1, 0, 0)$$ and $$(-2, 0, -4, 1)$$.

The **complete solution is the combination of the "one particular" and "many special" solutions**

## Complete solution: one $$x_p$$ and many $$x_n$$

$$ x = x_p + x_n = \begin{bmatrix} 1 \\\ 0 \\\ 6 \\\ 0 \end{bmatrix} + x_2 \begin{bmatrix} -3 \\\ 1 \\\ 0 \\\ 0\end{bmatrix} + x_4 \begin{bmatrix} -2 \\\ 0 \\\ {-4} \\\ 1 \end{bmatrix} $$

## Example: square invertible matrix $$m=n=r$$

Consider a **square invertible matrix** $$A$$, so $$m=n=r$$. What are $$x_p$$ and $$x_n$$?

$$x_p$$ is the **one and only solution** $$x_p = A^{-1}b$$. And there are so special solutions or free variables. $$R=I$$ has no zero rows. The only vector in $$N(A)$$ is $$x_n = 0$$. Hence, the complete solution is $$x = x_p + x_n = A^{-1}b + 0 = A^{-1}b$$

> # Full Column Rank (m > n)

Let's directly go to an example.

$$ A = \begin{bmatrix} 1 & 1 \\\ 1 & 2 \\\ -2 & -3 \end{bmatrix},\ b = \begin{bmatrix} b_1 \\\ b_2 \\\ b_3\end{bmatrix} $$

What are the conditions for $$Ax=b$$ to be **solvable**?

Using the augmented matrix and elimination, we get

$$ \begin{bmatrix} 1 & 0 & 2b_1 - b_2 \\\ 0 & 1 & b_2 - b_1 \\\ 0 & 0 & b_3 + b_1 + b_2\end{bmatrix} $$

The last equation is $$0 = 0$$ only if $$b_3 + b_1 + b_2 = 0$$

Also, this example has **no free variables** because $$n-r = 2 - 2 = 0$$. Hence, the **nullspace solution** or **special solutions** is $$x_n = 0$$. The **particular solution** to $$Ax=b$$ and $$Rx=d$$ lies at the top of the final column $$d$$:

$$ x_p = \begin{bmatrix} 2b_1 - b_2 \\\ b_2 - b_1\end{bmatrix} $$

Therefore, the **complete solution** to $$Ax = b$$ is

$$ x = x_p + x_n = \begin{bmatrix} 2b_1 - b_2 \\\ b_2 - b_1\end{bmatrix} + \begin{bmatrix} 0 \\\ 0 \end{bmatrix} $$

if $$b_3 + b_1 + b_2 = 0$$.

In this case, **there's only ONE solution!**.

If $$b_3 + b_1 + b_2 \neq 0$$, there is no solution $$Ax=b$$ (x_p and x don't exist).

This example is an extremely important case: $$A$$ has **full column rank**. **Every column has a pivot**. The **rank** $$r = n$$. The matrix is **tall and thin** ($$m \geq n$$). Row reduction puts $$I$$ **at the top** when $$A$$ is reduced to $$R$$ with rank $$n$$:

$$ R = \begin{bmatrix} I \\\ 0\end{bmatrix} = \begin{bmatrix} \text{n by n identity matrix} \\\ \text{m - n rows of zeros}\end{bmatrix} $$

There're **no free columns or free variables**. The **nullspace** $$N(A) = 0$$.

## Properties of full column rank (r = n) matrix

**[1]** All **columns** of $$A$$ are **pivot columns**

**[2]** There are **no free variables** or **special solutions**

**[3]** The **nullspace** $$N(A)$$ contains **only the zero vector** $$x = 0$$

**[4]** If $$Ax = b$$ has a solution (it might not!), then it has **only ONE solution** (since no nullspace solutions)

We also say that $$A$$ **has independent columns**. $$Ax=0$$ only happsn when $$x=0$$. The solution to $$Ax=b$$ is **unique if it exists**. There will be $$m - n$$ **zero rows** in $$R$$. So there are $$m - n$$ **conditions** on $$b$$ in order to have $$0=0$$ in those rows, and $$b$$ in the column space.

> With **full column rank**, $$Ax=b$$ has **one** solution OR **no** solution ($$m>n$$ is **overdetermined**)

> # Full Row Rank

The other extreme case is **full row rank** where $$Ax=0$$ has **one or infinitely many solutions**. In this case, $$A$$ must be **short and wide** ($$m \leq n$$). **A matrix has full row rank** if $$r = m$$ and we say **rows are independent**. Every row has a pivot.

$$ x + y + z = 3 $$

$$ x + 2y - z = 4 $$

These are two **planes** in $$xyz$$ space. They're not parallel so they **intersect in a line**. **The particular solution will be one point on that line**. Then, **adding the nullspace vectors** $$x_n$$ **will move us along the line**. Hence, $$x = x_p + x_n$$ gives the whole line of solutions

| ![joint](../../../assets/images/MATH/calculus/ch3_3.png) |
| :------------------------------------------------------: |
|      _Introduction to Linear Algebra, 5th edition_       |

Let's transform the above equation using the augmented matrix:

$$ \begin{bmatrix} 1 & 1 & 1 & \textbf{3} \\\ 1 & 2 & -1 & \textbf{4} \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 3 & \textbf{2} \\\ 0 & 1 & -2 & \textbf{1} \end{bmatrix} = \begin{bmatrix} R & d\end{bmatrix} $$

The **particular solution** has **free variable** $$x_3 = 0$$. And the **special solution** has $$x_3 = 1$$.

$$ x\_{particular} = (2, 1, 0) $$

$$ x\_{special} = s = (-3, 2, 1) $$

The **nullspace solution** $$x_n$$ is **any multiple of** $$s$$. Hence, the **complete solution is**

$$ x = x_p + x_n = \begin{bmatrix} 2 \\\ 1 \\\ 0 \end{bmatrix} + x_3 \begin{bmatrix} -3 \\\ 2 \\\ 1\end{bmatrix} $$

Any point on the line "could've been" the particular solution and we specifically chose the point with $$x_3=0$$. The **particular solution** is **not** multiplied by an arbitrary constant since the **special solution** needs that constant to produce all $$x_n$$ in the nullspace.

In summary, if $$m < n$$, the equation $$Ax = b$$ is **underdetermined** (many solutions).

## Properties of full row rank (r = m) matrix

**[1]** All rows have pivots and $$R$$ **has no zero rows**

**[2]** $$Ax=b$$ **has a solution for every right side b**

**[3]** The **column space** $$C(A)$$ is the whole space $$R^m$$

**[4]** There are $$n-r = n-m$$ **special solutions** in the nullspace of $$A$$.

In this case with $$m$$ pivots, we call that the rows are **linearly independent**. So the columns of $$A^{T}$$ are linearly independent. The nullspace of $$A^{T}$$ is the **zero vector**.

> # Four possibilities for linear equations

| ![joint](../../../assets/images/MATH/calculus/ch3_4.png) |
| :------------------------------------------------------: |
|      _Introduction to Linear Algebra, 5th edition_       |

Now, let's analyze in terms or $$R$$ which fall in the same cateogry as $$A$$. In case the **pivot columns happen to come first**, there're four possibilities for $$R$$. For $$Rx=d$$ to be solvable (so $$Ax=b$$), $$d$$ must end in $$m - r$$ **zeros**. $$F$$ is the **free part** of $$R$$.

| ![joint](../../../assets/images/MATH/calculus/ch3_5.png) |
| :------------------------------------------------------: |
|      _Introduction to Linear Algebra, 5th edition_       |

- Cases 1 and 2 have **full row rank** $$r=m$$

- Cases 1 and 3 have **full column rank** $$r = n$$

- Case 4 is the most general in theory but least common in practice

> # References

[1] Introduction to Linear Algebra, 5th edition
