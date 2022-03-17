---
layout: single
title: "[Statistics] Joint & Marginal Distributions"
categories: ["statistics"]
tag: [math]
---

> ## Joint Distribution

In the last post, we looked at random variables and probability distributions of a single random variable. What about probability distributions involving multiple random variables? That's where join distributions come in.

> ## Joint Probability Mass Function (discrete)

The **joint probability mass function** $p$ of two discrete random variables $X$ and $Y$ is the function $p: \mathbb{R}^2\rightarrow [0,1]$,

\[[p(a,b) = P(X=a, Y=b),\ -\infty<a,b<\infty\]]

> ## Joint Probability Density Function (continuous)

|          ![joint](../../assets/images/statistics/images/joint.png)           |
| :--------------------------------------------------------------------------: |
| _[columbia.edu](http://www.columbia.edu/~ad3217/joint_pmf_and_pdf/pdf.html)_ |

Since we have two random variables, our probability density function lies in 3D. Recall that with one variable, we found the **area** of the curve for an interval to find the probability. With multiple variables, we have to find the **volumne**.

Random variables $X$ and $Y$ have a **joint continuous distributioin** if for some function $f: \mathbb{R}^2\rightarrow \mathbb{R}$ and for all numbers $a_1, a_2$ and $b_1, b_2$ with $a_1 \leq b_1,\ a_2 \leq b_2$,

\[[P(a_1 \leq X \leq b_1, a_2 \leq Y \leq b_2) = \int_{a_1}^{b_1}\int_{a_2}^{b_2}f(x,y)dxdy\]]

where

1. $f(x,y) \geq 0$ for all $X$ and $Y$
2. $\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,y)dxdy=1$

Here, $f$ is the **joint pdf** of $X$ and $Y$. A joint pdf of 2 variables is often called **bivariate pdf**.

> ## Joint Distribution Function (cdf)

The **joint cdf** $F$ of two random variables $X$ and $Y$ is the function $F: \mathbb{R}^2 \rightarrow (0,1)$ defined by

\[[F(a,b) = P(X \leq a, Y \leq b),\ -\infty<a,b<\infty\]]

> ## Relationship b/w joint pdf and joint cdf

From the definition of joint cdf and joint pdf,

\[[F(a,b) = \int_{-\infty}^a\int_{-\infty}^b f(x,y)dxdy\]]

\[[f(x,y) = \frac{\partial^2}{\partial x \partial y}F(x,y)\]]

> ## Marginal Distribution Function (cdf)

Let $F$ be the joint distribution function of random variables $X$ and $Y$. Then,

The **marginal distribution function** of $X$ is given for each $a$ by

\[[F_X(a)=P(X \leq a) = F(a, +\infty) = \lim_{b \rightarrow \infty}F(a,b)\]]

Similarly for $Y$,

\[[F_Y(b)=P(Y \leq b) = F(+\infty, b) = \lim_{a \rightarrow \infty}F(a,b)\]]

> ## From joint pdf to marginal pdf

For **continuous** random variables, we can use integrals.

Let $f$ be the **joint pdf** of random variables $X$ and $Y$. Then, the **marginal pdf** of $X$ and $Y$ is,

\[[f_X(x) = \int_{-\infty}^{\infty}f(x,y)dy\]]

\[[f_Y(y) = \int_{-\infty}^{\infty}f(x,y)dx\]]

Note) For **marginal probabilities** for discrete random variables can be obtained by simply **summing over the joint probabilities** while pinned to the target random variable.

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/)  
[2] _A Modern Introduction to Probability and Statistics by Dekking_
