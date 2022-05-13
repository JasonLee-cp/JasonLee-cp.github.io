---
layout: null
title: "[Calculus] 15.1 Double Integrals over Rectangles"
categories: ["calculus"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Double Integral

The **double integral** of $f$ over the rectangle $R$ is

\[[ \iint_R f(x,y)dA = \lim\_{m,n \rightarrow \infty} \sum\_{i=1}^m \sum\_{j=1}^n f(x_{ij}^\*, y\_{ij}^\*) \Delta A \]]

If $f(x,y) \geq 0$, then the volumne $V$ of the solid that lies above the rectangle $R$ and below the surface $z=f(x,y)$ is

\[[ V = \iint_R f(x,y)dA \]]

> # Midpoint Rule for Double Integrals

\[[ \iint_R f(x,y)dA \sim \sum_{i=1}^m \sum_{j=1}^n f(\bar{x_i}, \bar{y_j}) \Delta A \]]

where $\bar{x_i}$ is the midpoint of $[x_{i-1},x_i]$ and $\bar{y_j}$ is the midpoint of $[y_{j-1},y_j]$.

> # Fubini's Theorem

If $f$ is continuous on the rectangle $R=\{ (x,y) \vert a \leq x \leq b, c \leq y \leq d \}$, then

\[[ \iint_R f(x,y)dA = \int_a^b \int_c^d f(x,y)dydx = \int_c^d \int_a^bf(x,y)dxdy \]]

> # Average Value

The **average value** of a function $f$ of two variables defined on a rectangle $R$ is

\[[ f_{ave} = \frac{1}{A(R)} \iint_R f(x,y)dA \]]

where $A(R)$ is the area of $R$.

> # References

[1] Stewart Calculus, 8th edition
