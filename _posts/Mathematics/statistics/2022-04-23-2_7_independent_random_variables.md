---
layout: null
title: "[Statistics] Independent Random Variables"
categories: ["statistics"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Independence

Two random variables $X$ and $Y$ are **independent** if for every $A$ and $B$,

\[[ P(X \in A, Y \in B) = P(X \in A)P(Y \in B) \]]

and we write $X  \perp\\!\\!\\!\perp Y$. Otherwise, we say $X$ and $Y$ are **dependent** and we write $X \not\\!\perp\\!\\!\\!\perp Y$.

In principle, to check whether $X$ and $Y$ are independent, we need to check the above equation for **all subsets** $A$ and $B$. Fortunately, we have the following theorem for continuous random variables and it's true for discrete random variables too.

## 2.30 Theorem

Let $X$ and $Y$ have joint PDF $f_{X,Y}$. Then $X \perp\\!\\!\\!\perp Y$ **if and only if** $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ for all values $x$ and $y$.

**2.32 Example**

Suppose $X$ and $Y$ are independent and both have the same density

\[[ f(x) = \begin{cases} 2x & 0 \leq x \leq 1 \\\ 0 & \text{otherwise} \end{cases} \]]

Find $P(X+Y \leq 1)$.

(Solution)

Since $X$ and $Y$ have the same PDF and they're independent, the joint PDF is

\[[ f(x,y)=f_X(x)f_Y(y)=\begin{cases} 4xy & 0 \leq x \leq 1,\ 0 \leq y \leq 1 \\\ 0 & \text{otherwise} \end{cases} \]]

Then,

\[[ P(X+Y \leq 1) = \int \int_{x+y \leq 1}f(x,y)dydx \]]

\[[ = \int_0^1 \int_0^{1-x}f(x,y)dydx \]]

\[[ = 4\int_0^1 x \left( \int_0^{1-x}ydy \right) dx \]]

\[[ = 2 \int_0^1 x(1-x)^2dx = \frac{1}{6} \]]

## 2.33 Theorem

Here's a useful formula for verifying indepdence.

Suppose that the **range** of $X$ and $Y$ is a (possibly infinite) **rectangle**. If $f(x,y) = g(x)h(y)$ for some functions $g$ and $h$ (not necessarily PDF), then $X$ and $Y$ are independent.

**Examples**

Let $X$ and $Y$ have density

\[[ f(x,y)=f_X(x)f_Y(y)=\begin{cases} 2e^{-(x+2y)} & x>0,\ y>0 \\\ 0 & \text{otherwise} \end{cases} \]]

The range of $X$ and $Y$ is the rectangle $(0, \infty) \times (0, \infty)$. Hence, we can write, for example, $f(x,y) = g(x)h(y)$ where $g(x)=2e^{-x}$ and $h(y)=e^{-2y}$. Thus they're independent.

> # References

[1] All of Statistics by Larry A. Wasserman
