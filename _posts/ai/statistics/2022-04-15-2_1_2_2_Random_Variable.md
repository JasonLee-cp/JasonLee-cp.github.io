---
layout: post
title: "[Statistics] 2.1-2 Random Variable"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Random Variable

How do we **link** sample spaces and events to data? This is provided by random variable.

A **random variable** is a **mapping**

$$ X : \Omega \rightarrow \mathbb{R} $$

that assigns a real number $$X(w)$$ to each outcome $$w$$.

> # Distribution Functions and Probability Functions

## Cumulative Distribution Function (CDF)

The cumulative distribution function is the function $$F_X : \mathbb{R} \rightarrow [0,1]$$ defined by

$$ F_X(x) = P(X \leq x ) $$

Sometimes we write CDF just as $$F$$ instead of $$F_X$$.

Note that the CDF contains all the information about the random variable. In other words, the CDF **completely determines** the distribution of a random variable.

## 2.7 Theorem

Let $$X$$ have CDF $$F$$ and let $$Y$$ have CDF $$G$$. If $$F(x)=G(x)$$ for all $$x$$, then $$P(X \in A) = P(Y \in A)$$ for all $$A$$.

## 2.8 Theorem

A function $$F$$ mapping the real line to $$[0,1]$$ is a CDF for some probability $$P$$ **if and only if** $$F$$ satisfies the three conditions:

**(i)** $$F$$ is **non-decreasing**: $$x_1 < x_2 \rightarrow F(x_1) \leq F(x_2)$$

**(ii)** $$F$$ is **normalized**:

$$ \lim\_{x \rightarrow -\infty} F(x) = 0 $$

$$ \lim\_{x \rightarrow \infty} F(x) = 1 $$

**(iii)** $$F$$ is **right-continuous**: $$F(x) = F(x^+)$$ for all $$x$$

> # Discrete Random Variable

$$X$$ is **discrete\* if it takes **countably**\* many values $$\{x_1, x_2,...\}$$. The **probability function** or **probability mass function\*\* (pmf) for $$X$$ is defined by

$$ f_X(x) = P(X=x) $$

Notice that since a probability must be equal or greater than $$0$$, $$f_X(x) \geq 0$$ for all $$x \in \mathbb{R}$$ and $$\sum_i f_X(x_i)=1$$.

Sometimes we denote $$f_X$$ just as $$f$$.

## CDF of discrete random variable

The **CDF** of $$X$$ is related to $$f_X$$ by

$$ F*X(x) = P(X \leq x) = \sum*{x_i \leq x}f_X(x_i) $$

> # Continuous Random Variable

A random variable $$X$$ is **continuous** if there exists a function $$f_X$$ such that $$f_X(x) \geq 0$$ for all $$x$$, $$\int_{-\infty}^{\infty}f_X(x)dx = 1$$, and for every $$a \leq b$$,

$$ P(a < X < b) = \int_a^b f_X(x)dx $$

The function $$f_X$$ is called the **probability density function** (PDF).

## CDF of continuous random variable

$$ F*X(x) = \int*{-\infty}^x f_X(t)dt $$

and $$f_X(x) = F'_X(x)$$ at all points $$x$$ at which $$F_X$$ is **differentiable**.

Sometimes we write $$\int f(x)dx$$ or $$\int f$$ to denote $$\int_{-\infty}^{\infty}f(x)dx$$

**ex1**

Suppose a continuous random variable $$X$$ has PDF,

$$
f(x) =
\begin{cases}
0, & \text{if}\ x<0 \\\ \frac{1}{(1+x)^2}, & \text{otherwise}
\end{cases}
$$

Since $$\int f(x)dx = 1$$ (substitue $$u=x+1$$), this is a **well-defined PDF**.

On the other hand,

$$
f(x) =
\begin{cases}
0, & \text{if}\ x<0 \\\ \frac{1}{(1+x)}, & \text{otherwise}
\end{cases}
$$

is **not** a PDF since $$\int f(x)dx$$ = $$\log(\infty) = \infty$$

## Density is NOT Probability!

Keep in mind that we're dealing with probability **density** not a probability itself which means that $$f_X(x)$$ does not necessarily be in range $$[0,1]$$ but it's **unbounded**. We find density by **integrating** which means $$P(X=x)$$ = $$P(x \leq X \leq x) = \int_x^x f_X(x)dx = 0$$

> # Some useful properties of CDF

Let $$F$$ be the CDF for a random variable $$X$$. Then,

$$1.\ P(X=x) = F(x) - F(x^{-})$$

$$2.\ P(x < X \leq y) = F(y) - F(x)$$

$$3.\ P(X > x) = 1 - F(x)$$

$$4.\ If\ X\ is\ continuous\ then$$

$$ F(b) - F(a) = P(a < X < b) = P(a \leq X < b) $$

$$ = P(a < X \leq b) = P(a \leq X \leq b) $$

> # Quantile function (inverse CDF)

Let $$X$$ be a random variable with CDF $$F$$. The **inverse CDF** or **quantile function** is

$$ F^{-1}(q) = \inf \{ x: F(x) > q \} $$

for $$q \in [0,1]$$. If $$F$$ is **strictly increasing** and **continuous**, then $$F^{-1}(q)$$ is the **unique real number** $$x$$ such that $$F(x)=q$$.

[NOTE] $$\inf$$ can be thought of as the **minimum**.

We call $$F^{-1}(0.25)$$ the **first quartile**, $$F^{-1}(0.5)$$ the **median** (or second quartile), and $$F^{-1}(0.75)$$ the **third quartile**..

> # "Equal" in distribution

Two random variables $$X$$ and $$Y$$ are **equal in distribution** if for all $$x$$,

$$ F_X(x) = F_Y(x) $$

and we denote $$X \stackrel{d}{=} Y$$.

However, this **does not** mean that $$X$$ and $$Y$$ are **equal**. It means that all probability statements about $$X$$ and $$Y$$ are equal. For example, suppose $$P(X=1)=P(X=-1)=\frac{1}{2}$$ and $$Y=-X$$. Then, $$P(Y=1)=P(Y=-1)=\frac{1}{2}$$. Hence, $$X \stackrel{d}{=} Y$$ but $$X \neq Y$$. In fact, $$P(X=Y)=0$$.

> # References

[1] All of Statistics by Larry A. Wasserman
