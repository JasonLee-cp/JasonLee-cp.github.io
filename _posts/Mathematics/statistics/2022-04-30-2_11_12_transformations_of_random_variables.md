---
layout: null
title: "[Statistics] 2.11-12 Transformations of Random Variables"
categories: ["statistics"]
tag: [math]

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Transformations of Random Variables

Suppose $X$ is a random variable with **PDF** $f_X$ and **CDF** $F_X$.

Now let $Y=r(X)$ be a function of $X$. (ex. $Y=X^2, Y=e^X$.)

Then, we call $Y=r(X)$ a **transformation** of $X$.

How do we compute the **PDF** and **CDF** of $Y$?

## Discrete Case

For discrete case, the answer is straightforward. The mass function of $Y$ is given by $y_Y(y)$. Then,

\[[ f_Y(y)=P(Y=y)=P(r(X)=y) \]]

\[[ P(\{ x: r(x)=y \}) = P(X \in r^{-1}(y)) \]]

For example, if $Y=X^2$, if we want to find $f_Y(4)$, then we can find $P(X \in r^{-1}(4))$ which is $P(X=\pm 2)$

## Continuous Case

For continuous case, it gets little trickier. Below are the three steps for transformations:

**[1]** For each $y$, find the set $A_y = \{ x: r(x) \leq y \}$

**[2]** Find the **CDF**

\[[ F_Y(y) = P(Y \leq y) = P(r(X) \leq y) \]]

\[[ = P(\{ x; r(x) \leq y \}) \]]

\[[ = \int_{A_y}f_X(x)dx \]]

**[3]** The **PDF** is $f_Y(y) = F'_Y(y)$

This might be confusing but it's actually not that complicated. Let's take an example.

### 2.46 Example

Let $f_X(x) = e^{-x}$ for $x > 0$. Then, $F_X(x) = \int_0^x f_X(s)ds=1-e^{-x}$. Also, $Y=r(X)=log(X)$. Find the **PDF** and **CDF** of $Y$.

**[1]** We find the set $A_y = \{ x: r(x) \leq y  \}$

What this means is that since the definition of **CDF** of $Y$ is $P(Y \leq y)$ or $P(\{ y: Y \leq y  \})$. However, since $Y$ is a transformation of $X$, we can **express the CDF in terms of** $X$ - $A_y = \{ x: r(x) \leq y \}$.

Hence, $A_y=\{ \log X \leq y\}$. So,

\[[ A_y = \{ x: x \leq e^{y}\} \]]

**[2]** Find the CDF

\[[ F_Y(y) = P(Y \leq y) = P(\log X \leq y) \]]

\[[ = P(X \leq e^y) = F_X(e^y) = 1 - e ^{-e^{y}} \]]

**[3]** Find the PDF

Therefore, $f_Y(y) = F'_Y(y) = e^ye^{-e^y}$ for $y \in \mathbb{R}$.

> # Transformations of Several Random Variables

In cases we're interested in transformations of several random variablses($X/Y, X+Y$), the steps are the same as before:

**[1]** For each $z$, find the set $A_z = \{ (x,y):r(x,y)<z \}$

**[2]** Find the CDF

\[[ F_Z(z) = P(Z \leq z ) = P(r(X,Y) \leq z) \]]

\[[ = P(\{ ((x,y) ; r(x,y) \leq z\}) = \int \int_{A_z}f_{X,Y}(x,y)dxdy \]]

**[3]** Then $f_Z(z) = F'_Z(z)$

> # References

[1] All of Statistics by Larry A. Wasserman
