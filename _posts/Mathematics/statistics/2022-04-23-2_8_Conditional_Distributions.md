---
layout: null
title: "[Statistics] 2.8 Conditional Distributions"
categories: ["statistics"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Conditional Distributions

## Discrete Case

The conditional **PMF** is

\[[ f_{X \lvert Y}(x \vert y) = P(X=x \vert Y = y) = \frac{P(X=x, Y=y)}{P(Y=y)}=\frac{f_{X,Y}(x,y)}{f_Y(y)} \]]

if $f_Y(y)>0$

## Conditional Case

For continuous random variables, the conditional **PDF** is

\[[ f_{X \lvert Y}(x \vert y) = \frac{f_{X,Y}(x,y)}{f_Y(y)} \]]

assuming $f_Y(y)>0$. Then,

\[[ P(X \in A \vert Y = y) = \int_A f_{X \vert Y}(x \vert y)dx \]]

> # References

[1] All of Statistics by Larry A. Wasserman
