---
layout: null
title: "[Calculus] 14.8 Lagrange Multipliers"
categories: ["calculus"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Lagrange Multiplier

Suppose a function $f$ has an **extreme value** at a point $P(x_0,y_0,z_0)$ on the surface $S$.

Let $C$ be a curve defined by a vector equation $r(t) = \left\langle x(t), y(t), z(t) \right\rangle$ that lies on $S$ and passes through $P$.

It $t_0$ is the parameter corresponding to $P$, then

\[[ r(t_0) = \left\langle x_0, y_0, z_0 \right\rangle \]]

Then, the composition function

\[[ h(t) = f(x(t), y(t), z(t)) \]]

represents the **values** that $f$ takes on the curve $C$. Since $f$ has an extreme value at $(x_0,y_0,z_0)$, $h$ has an extreme value at $t_0$. Hence,

\[[ h'(t_0) = 0 \]]

But if $f$ is differentiable, we can apply the chain rule for $h$,

\[[ h'(t_0)=0 \]]

\[[ f_x(x_0,y_0,z_0)x'(t_0) + f_y(x_0,y_0,z_0)y'(t_0) + f_z(x_0,y_0,z_0)z'(t_0) = 0 \]]

\[[ \nabla f(x_0,y_0,z_0) = r'(t_0) \]]

This shows that the **gradient vector** $\nabla f(x_0,y_0,z_0)$ is **orthogonal** to the **tangent vector** $r'(t_0)$ to every such curve $C$.

But we know that $\nabla g(x_0,y_0,z_0)$ is also **orthogonal** to the **tangent vector** $r'(t_0)$ for every such curve $C$.

Therefore, the two gradient vectors $\nabla f(x_0,y_0,z_0)$ and $\nabla g(x_0,y_0,z_0)$ must be **parallel**. So $\nabla g(x_0,y_0,z_0) \neq 0$, there is a number $\lambda$ such that

\[[ \nabla f(x_0,y_0,z_0) = \lambda \nabla g(x_0,y_0,z_0) \]]

The number $\lambda$ is called a **Langrage multiplier**.

> # Method of Lagrange Multipliers

To find the **maximum** and **minimum** values of $f(x,y,z)$ **subject to the constraint** $g(x,y,z) = k$ assuming that these extreme values exist and $\nabla g \neq 0$ on the surface $g(x,y,z) = k$,

**[i]** Find all values of $x,y,z,\lambda$ such that

\[[ \nabla f(x,y,z) = \lambda g(x,y,z) \]]

\[[ g(x,y,z) = k \]]

**[ii]** Evaluate $f$ at all the points $(x,y,z)$ that result from **[i]**. The **largest value** is the **maximum value** of $f$ and the **smallest value** is the **minimum value** of $f$.

> # Two Constraints

Tow constraints case work similarly

\[[ \nabla f(x_0,y_0,z_0) = \lambda \nabla g(x_0,y_0,z_0) + \mu \nabla h(x_0,y_0,z_0) \]]

> # References

[1] Stewart Calculus, 8th edition
