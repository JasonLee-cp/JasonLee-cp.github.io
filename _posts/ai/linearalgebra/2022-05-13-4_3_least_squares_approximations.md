---
layout: post
title: "[Linear Algbera] 4.3 Least Squares Approximation"
subtitle: ""
categories: ai
tags: linearalgebra
comments:
---

> # Keywords

**[1]** Solving $$A^TA\hat{x}=A^Tb$$ gives the projection $$p=A\hat{x}$$ of $$b$$ onto the column space of $$A$$

**[2]** When $$Ax=b$$ has no solution, $$\hat{x}$$ is the **least-squares solution**: $$\lVert b - A\hat{x} \rVert^2$$ = minimum

**[3]** Setting partial derivatives of $$E = \lVert Ax - b \rVert^2$$ to zero also produces $$A^TA \hat{x}=A^Tb$$

**[4]** To fit points $$(t_1,b_1),...,(t_m,b_m)$$ by a straight line, $$A$$ has columns $$(1,...,1)$$ and $$(t_1,...,t_m)$$

**[5]** In that case $$A^TA$$ is the 2 by 2 matrix $$\begin{bmatrix} m & \sum t_i \\\ \sum t_i & \sum t_i^2 \end{bmatrix}$$ and $$A^Tb$$ is the vector $$\begin{bmatrix} \sum b_i \\\ \sum t_ib_i \end{bmatrix}$$

> # Intuition

Often times $$Ax=b$$ has **no solution** usually becuase there're **too many equations**. In other words, we cannot always get the error $$e = b - Ax$$ down to **zero**. If the error is zero, then $$x$$ is an exact solution to $$Ax=b$$. When there's no solution, we can make it that the **length** of $$e$$ is **as small as possible**. In this case, $$\hat{x}$$ is a **least squares solution**.

In the previous section, we mostly talked about $$p$$ **projection**. In this section, we focus on $$\hat{x}$$ (the least squares solution). They're connected by $$p=A\hat{x}$$. The fundamental equation is $$A^TA\hat{x}=A^Tb$$

> When $$Ax=b$$ has no solution, multiply by $$A^T$$ and solve $$A^TA\hat{x}=A^Tb$$

> # Minimizing the Error

How do we make the error $$e=b-Ax$$ as small as possible?

The part in the column space is $$p$$ and the perpendicular part is $$e$$. We cannot solve $$Ax=b$$ but but we can solve $$A\hat{x}=p$$ with $$\hat{x}=(A^TA)^{-1}A^Tb$$

The solution to $$A\hat{x}=p$$ leaves the **least possible error**

Using the right triangle formula, we have

$$ \lVert Ax - b \rVert^2 = \lVert Ax - p \rVert^2 + \lVert e \rVert^2 $$

We reduce $$Ax-p$$ to **zero** by choosing $$x=\hat{x}$$ which leaves the smallest possible error $$e$$ which we cannot further reduce. This means that the **squared length** of $$Ax-b$$ is minimized

> The least squares solution $$\hat{x}$$ makes $$E=\lVert Ax-b \rvert^2$$ as small as possible

> # Fitting a Straight Line

The line $$C+Dt$$ minimizes $$e_1^2+ \cdots + e_m^2 = \lVert Ax - b \rVert^2$$ when $$A^TA\hat{x}=A^Tb$$:

$$ A^TA\hat{x}=A^Tb $$

$$ \begin{bmatrix} m & \sum t_i \\\ \sum t_i & \sum t_i^2 \end{bmatrix} \begin{bmatrix} C \\\ D \end{bmatrix} = \begin{bmatrix} \sum b_i \\\ \sum t_ib_i \end{bmatrix} $$

> # References

[1] Introduction to Linear Algebra, 5th edition
