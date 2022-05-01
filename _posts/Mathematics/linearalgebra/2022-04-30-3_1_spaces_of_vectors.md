---
layout: single
title: "[Linear Algbera] 3.1 Spaces of Vectors"
categories: ["linearalgebra"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Keywords

[1] The standard $n$-dimensional space $\mathbb{R}^n$ contains all real column vectors with $n$ components

[2] If $v$ and $w$ are in a **vector space** $S$, every combination $cv + dw$ must be in $S$

[3] The "vectors" in $S$ can be matrices or functions of $x$. The 1-point space $Z$ consists of $x=0$

[4] A **subspace** of $\mathbb{R}^n$ is a vector space inside $\mathbb{R}^n$. Example: The line $y=3x$ inside $\mathbb{R}^2$

[5] The **column space** of $A$ contains all combinations of the columns of $A$: a subspace of $\mathbb{R}^m$

[6] The column space contains all the vectors $Ax$. So $Ax=b$ is solvable when $b$ is in $C(A)$.

> # Vector Space

The most important vector spaces are $\mathbb{R}^1, \mathbb{R}^2, \mathbb{R}^3, \mathbb{R}^4,...$. Each space $\mathbb{R}^n$ conists of a whole collection of vectors. $\mathbb{R}^5$ consists of **all vectors with 5 components**. This is called **5-dimensional space**.

> The space $\mathbb{R}^n$ consists of all column vectors $v$ with $n$ components.

For example, the vector space $\mathbb{R}^2$ consists of **all possible vectors** with 2 components.
\[[ \mathbb{R}^2 = \begin{bmatrix} x \\\ y \end{bmatrix} \]]

The components of $v$ are **real numbers** which is why we denote as $\mathbb{R}$. A vector with complex components lies in the space $\mathbb{C}^n$

> Linear combinations of any vectors in $\mathbb{R}^n$ and scalar multiplication **stays in the space**

For example, if we multiply $v \in \mathbb{R}^n$ by $3$ and add $u \in \mathbb{R}^n$, the result stays in $\mathbb{E}^n$.

Now, let's look at some other vector spaces other that $\mathbb{R}^n$

**M** - The vector space of **all real 2 by 2 matrices**

**F** - The vector space of **all real functions** $f(x)$

**Z** - The vector space that consists only of a **zero vector**

In **M**, the "vectors" are actually matrices. In **F**, the vectors are functions. In **Z**, the only addition is $0 + 0 = 0$.

The space **Z** is **zero-dimensional** and the **smallest possible vector space**. We do not call it $\mathbb{R}^0$. The vector space **Z** contains **exactly one vector (zero)**. Every space has its own zero vector - the zero matrix, the zero function, the vector $(0,0,0)$ in $\mathbb{R}^3$

> # 8 Rules for Vector Space

**[1]** $x+y = y+x$

**[2]** $x+(y+z) = (x+y)+z$

**[3]** There is a unique **zero vector** such that $x+0=x$ for all $x$

**[4]** For each $x$ there is a unique vector $-x$ such that $x + (-x)=0$

**[5]** $1$ times $x$ equals $x$

**[6]** $(c_1c_2)x = c_1(c_2x)$

**[7]** $c(x+y)=cx+cy$

**[8]** $(c_1+c_2)x = c_1x + c_2x$

> # Subspaces

There are vectors spaces **inside** $\mathbb{R}^n$. Those are **subspaces** of $\mathbb{R}^n$.

Let's take an example of $\mathbb{R}^n$. Consider a **plane** through the origin $(0,0,0)$. **That plane is a vector space in its own**. If we add two planes or multiply a plane by a scalar, it's still in the plane.

However, a **plane in three-dimensional space is NOT** $\mathbb{R}^2$ even if it looks like $\mathbb{R}^2$. The vectors have **three components** and they strictly belong to $\mathbb{R}^3$. The plane is a vector space **inside** $\mathbb{R}^3$. This is one of the most fundamental ideas in linear algebra. The **plane** going through (0,0,0) is a **subspace** of the full vector space $\mathbb{R}^3$.

> A **subspace** of a vector space is a set of vectors (including 0) that satisfies two requiresments: If $v$ and $w$ are vectors in the subspace and $c$ is any scalar, then **(i)** $v + w$ is in the subspace, **(ii)** $cv$ is in the subspace.

In other words, the set of vectors is **closed** under addition $v + w$ and multiplication $cv$. In short, **all linear combinations stay in the subspace**.

Since they're subspaces, they automatically follow the **eights required conditions** of the "host space" (parent space). So we just have to check the **linear combinations requirement** for a subspace.

## Every subspace contains the zero vector

The plane in $\mathbb{R}^3$ **must go through** $(0,0,0)$. As the rule (ii) says ($cv$ still is in the subspace), if we choose $c=0$, then the rule requires $0v$ to be in the subspace. Planes that don't contain the origin fail this test.

**Lines through the origin are also subspaces**.

Another subspace is **all of** $\mathbb{R}^3$. The whole space is always a subspace of itself.

Here's a list of all the possible subspaces of $\mathbb{R}^3$

**Z** = The single zero vector $(0,0,0)$

**L** - Any line through $(0,0,0)$

**P** - Any plane through $(0,0,0)$

$\mathbb{R}^3$ - The whole space

Now we combine the requirements into a single requirement for subspace

> A subspace containing $v$ and $w$ must contain **all linear combinations** $cv+dw$.

## Example

Inside the vector space $M$ of all 2 by 2 matrices, two possible subspaces are

\[[ (U)\ \text{All upper triangular matrices} \begin{bmatrix} a & b \\\ 0 & d \end{bmatrix} \]]

\[[ (D)\ \text{All diagonal matrices} \begin{bmatrix} a & 0 \\\ 0 & d \end{bmatrix} \]]

If we add any two matrices in $U$, the sum is in $U$. If we add any diagonal matrices, the sum is diagonal. In this case $D$ is also a subspace of $U$. When $a, b, d$ are all zero, then the zero matrix is in these subspaces, of course. $Z$ is always a subspace.

Multiples of the identity matrix $I$ also form a subspace. $2I+3I$ is in this subspace and so is 3 times $4I$. The matrices $cI$ form a "line of matrices" inside $M, U, D$.

However, the matrix $I$ is **NOT** a subspace **by itself**. Only the **zero matrix** is.

> # The Column Space of A

The most important subspaces are tied directly to matrix $A$. It's time to go deeper into $Ax-b$.

When we're trying to solve $Ax=b$, if $A$ is **not invertible**, the system is solvable for some $b$ and not solvable for other $b$. The **solvable** $b'$s form the **column space** of A: $C(A)$. Remember that $Ax$ is a **combination of the columns of** $A$. To get every possible $b$, we use every possible $x$.

**All the linear combinations of the columns of** $A$ **produce the column space of** $A$. It is a **vector space made up of column vectors** and we note the column space as $C(A)$.

> The **column space** consists of **all linear combinations of the columns**. The combinations are all possible vectors $Ax$. They fill the column space $C(A)$.

Now comes an extremely important idea in linear algebra: **To solve** $Ax=b$ is to **express** $b$ **as a combination of the columns**. The right side $b$ **MUST BE IN THE COLUMN SPACE** produced by $A$ or no solution!

> The system $Ax=b$ is solvable if and only if $b$ **is in the column space of** $A$

When $b$ is in $C(A)$, it is a combination of the columns. In other words, the **coefficients** of this combination give us the **solution** $x$ to the system $Ax=b$.

Suppose $A$ is $m \times n$ matrix. Its columns have $m$ components so the columns belong to $\mathbb{R}^m$. **The column space of** $A$ **is a subspace of** $\mathbb{R}^m$.

> # Span

Instead of columns in $\mathbb{R}^m$, we start with **any set** $S$ of vectors in a vector space $V$. To get a **subspace** $SS$ of $V$, we take **all combinations** of the vectors in that set $S$.

\[[ S = \text{set of vectors in}\ V\ \text{(probability not a subspace)} \]]

\[[ SS = \text{all combinations of vectors in}\ S\ \text{(definitely a subspace)} \]]

In summary

\[[ SS = \text{all}\ c_1v_1 + \cdots + c_Nv_N = \text{the subspace of}\ V\ \text{"spanned" by}\ S \]]

For example, when $S$ is the set of **columns**, $SS$ is the **column space**. Always, $SS$ is the **smallest subspace containing** $S$. To repeat: The columns **span** the column space.

> We write that the subspace $SS$ is the **span** of $S$, containing all combinations of vectors of $S$

> # References

[1] Introduction to Linear Algebra, 5th edition
