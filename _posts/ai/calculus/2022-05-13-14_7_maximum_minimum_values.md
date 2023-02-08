---
layout: post
title: "[Calculus] 14.7 Maximum and Minimum Values"
subtitle: ""
categories: ai
tags: calculus
comments:
---

> # Local maximum and Local minimum

A function of two variables has a **local maximum** at $$(a,b)$$ if $$f(x,y) \leq f(a,b)$$ when $$(x,y)$$ is near $$(a,b)$$. This means $$f(x,y) \leq f(a,b)$$ for all points $$(x,y)$$ in some disk with center $$(a,b)$$. The number $$f(a,b)$$ is called a **local maximum value**. If $$f(x,y) \geq f(a,b)$$ when $$(x,y)$$ is near $$(a,b)$$, then $$f$$ has a **local minimum** at $$(a,b)$$ and $$f(a,b)$$ is a **local minimum value**.

If the inequalities hold for **all points** $$(x,y)$$ in the domain of $$f$$, then $$f$$ has an **absolute maximum** or **absolute minimum** at $$(a,b)$$

> # Local max/min and first-order partial derivative

If $$f$$ has a local maximum or minimum at $$(a,b)$$ and the first-order partial derivatives of $$f$$ exist there, then $$f_x(a,b)=0$$ and $$f_y(a,b)=0$$. We call the point $$(a,b)$$ a **critical point**.

> # Second Derivatives Test

Suppose the second partial derivatives of $$f$$ are continuous on a disk with center $$(a,b)$$, and suppose that $$f_x(a,b)=0$$ and $$f_y(a,b)=0$$ [that is, $$(a,b)$$ is a critical point of $$f$$]. Let

$$ D = D(a,b) = f*{xx}(a,b)f*{yy}(a,b) - f\_{xy}(a,b)^2 $$

$$ \text{or} $$

$$ D = \begin{vmatrix} f*{xx} & f*{xy} \\\ f*{yx} & f*{yy} \end{vmatrix} = f*{xx}f*{yy} - f\_{xy}^2 $$

**(i)** If $$D > 0$$ and $$f_{xx}(a,b) > 0$$, then $$f(a,b)$$ is a **local minimum**

**(ii)** If $$D > 0$$ and $$f_{xx}(a,b) < 0$$, then $$f(a,b)$$ is a **local maximum**

**(iii)** If $$D < 0$$, then $$f(a,b)$$ is **not** a local maximum or minimum.

If $$D=0$$, the test gives no information: $$f$$ could have a local maximum or minimum or could be a saddle point at $$(a,b)$$

## Saddle Point

In case **(iii)**, the point $$(a,b)$$ is called a **saddle point** of $$f$$.

> # Absolute Maximum an Minimum Values

## Extreme Value Theorem

If $$f$$ is continuous on a closed, bounded set $$D$$ in $$\mathbb{R}^2$$, then $$f$$ attains an absolute maximum value $$f(x_1,y_1)$$ and an absolute minimum value $$f(x_2,y_2)$$ at some points $$(x_1, y_1)$$ and $$(x_2, y_2)$$ in $$D$$.

---

To find the absolute maximum and minimum values of a continuous function $$f$$ on a closed, bounded set $$D$$:

A **closed set** in $$\mathbb{R}^2$$ is one that contains all its boundary points. A boundary point of $$D$$ is a point $$(a,b)$$ such that every disk with center $$(a,b)$$ contains points in $$D$$ and also points not in $$D$$.

A **bounded set** in $$\mathbb{R}^2$$ is one that is contained within some disk.

1. Find the values of $$f$$ at the critical points of $$f$$ in $$D$$.
2. Find the extreme values of $$f$$ on the boundary of $$D$$
3. The largest of the values from steps 1 and 2 is the absolute maximum value; the smallest of these values is the absolute minimum value

> # References

[1] Stewart Calculus, 8th edition
