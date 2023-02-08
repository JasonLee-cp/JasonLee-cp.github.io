---
layout: post
title: "[Statistics] 3.5 Conditional Expectations"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Conditional Expectation

The **conditional expectation** of $$X$$ given $$Y=y$$ is

$$ \mathbb{E}[X \vert Y=y]=\sum xf\_{X \vert Y}(x \vert y)dx,\ \ \text{discrete case} $$

$$ \mathbb{E}[X \vert Y=y]=\int xf\_{X \vert Y}(x \vert y)dx,\ \ \text{continuous case} $$

If $$r(x,y)$$ is a function of $$x$$ and $$y$$ then,

$$ \mathbb{E}[r(X,Y) \vert Y=y]=\sum r(x,y) f\_{X \vert Y}(x \vert y)dx,\ \ \text{discrete case} $$

$$ \mathbb{E}[r(X,Y) \vert Y=y]=\int r(x,y) f\_{X \vert Y}(x \vert y)dx,\ \ \text{continuous case} $$

**[Important]** While $$\mathbb{E}[X]$$ is a number, $$\mathbb{E}[X \vert Y = y]$$ is a **function** of $$y$$. Before observing $$Y$$, we cannot know the value $$\mathbb{E}[X \vert Y = y]$$ so it is a **random variable** which we denote $$\mathbb{E}[X \vert Y]$$. In other words, $$\mathbb{E}[X \vert Y]$$ is the random variable whose value if $$\mathbb{E}[X \vert Y = y]$$ when $$Y=y$$.

> # The Rule of Iterated Expecations

For random variables $$X$$ and $$Y$$, assuming the expectations exist, we have

$$ \mathbb{E}[\mathbb{E}[Y \vert X]] = \mathbb{E}[Y] $$

$$ \mathbb{E}[\mathbb{E}[r(X,Y) \vert X] = \mathbb{E}[r(X,Y)] $$

> # Conditional Variance

$$ V(Y \vert X = x) = \int (y-\mu(x))^2 f(y \vert x)dy $$

where $$\mu(x)=\mathbb{E}[Y \vert X = x]$$

> # 3.27 Theorem

For random variables $$X$$ and $$Y$$,

$$ Var(Y) = \mathbb{E}[Var(Y \vert X)] + Var(\mathbb{E}[Y \vert X]) $$

> # References

[1] All of Statistics by Larry A. Wasserman
