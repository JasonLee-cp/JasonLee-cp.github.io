---
layout: post
title: "[Statistics] 2.8 Conditional Distributions"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Conditional Distributions

## Discrete Case

The conditional **PMF** is

$$ f*{X \lvert Y}(x \vert y) = P(X=x \vert Y = y) = \frac{P(X=x, Y=y)}{P(Y=y)}=\frac{f*{X,Y}(x,y)}{f_Y(y)} $$

if $$f_Y(y)>0$$

## Conditional Case

For continuous random variables, the conditional **PDF** is

$$ f*{X \lvert Y}(x \vert y) = \frac{f*{X,Y}(x,y)}{f_Y(y)} $$

assuming $$f_Y(y)>0$$. Then,

$$ P(X \in A \vert Y = y) = \int*A f*{X \vert Y}(x \vert y)dx $$

> # References

[1] All of Statistics by Larry A. Wasserman
