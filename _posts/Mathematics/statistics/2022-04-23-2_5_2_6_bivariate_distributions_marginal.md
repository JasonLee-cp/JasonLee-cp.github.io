---
layout: null
title: "[Statistics] Bivariate distributions and Marginal Distributions"
categories: ["statistics"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Joint mass function

Given a pair of **discrete** random variables $X$ and $Y$, The **joint mass function** is defined by

\[[ f(x,y) = f_{X,Y}(x,y) = P(X=x, Y=y) \]]

> # Joint density function

In the **continuous case**, we call a function $f(x,y)$ a PDF for the random variables $(X,Y)$ if

(i) $f(x,y) \geq 0$ for all $(x,y)$

(ii) $\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x,y)dxdy = 1$

(iii) for any set $A \subset \mathbb{R} \times \mathbb{R}, P((X,Y) \in A) = \int \int_A f(x,y)dxdy$

> # Joint CDF

For both discrete and continuous case, the **joint CDF** is defined as

\[[ F_{X,Y}(x,y) = P(X \leq x, Y \leq y) \]]

> # Marginal Distributions

## Marginal mass function

If $(X,Y)$ have joint distribution with mass function $f_{X,Y}$, then the **marginal mass function** for $X$ is,

\[[ f_X(x) = P(X=x) = \sum_y P(X=x, Y=y) = \sum_y f(x,y) \]]

and the **marginal mass function** for $Y$ is,

\[[ f_Y(y) = P(Y=y) = \sum_x P(X=x, Y=y) = \sum_x f(x,y) \]]

## Marginal density function

For continuous random variables, the marginal densities are

\[[ f_X(x) = \int f(x,y)dy \]]

\[[ f_Y(y) = \int f(x,y)dx \]]

The corresponding marginal distribution functions are denoted by $F_X$ and $F_Y$

> # References

[1] All of Statistics by Larry A. Wasserman
