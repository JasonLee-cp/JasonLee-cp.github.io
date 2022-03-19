---
layout: null
title: "[Statistics] Expectation, Variance, and Covariance"
categories: ["statistics"]
tag: [math]
---

> ## Expectation

### Discrete R.V

The **expectation** of a discrete random variable $X$ taking on the values $a_1, a_2,..$ and with probability mass function $p$ is defined by,

\[[ \mathbb{E}[X]=\sum_i a_i P(X=a_i) = \sum_ia_ip(a_i) \]]

### Continuous R.V

The **expectation** of a continuous random variable with its probability density function $p$ is defined by,

\[[ \mathbb{E}[X] = \int\_{-\infty}^{\infty}xf(x)dx \]]

> ## Linearity of Expectation

\[[ \mathbb{E}[\alpha f(x) + \beta g(x)] = \alpha \mathbb{E}[f(x)] + \beta \mathbb{E}[g(x)] \]]

**[Proof]**

For discrete random variables $X$ and $Y$ with values $a_1, a_2, ...$ and $b_1, b_2, ...$, respectively,

$\mathbb{E}[X+Y] = \sum_i\sum_j (a_i + b_j)P(X=a_i,Y=b_j)$

$= \sum_i\sum_j a_i P(X=a_i, Y=b_j) + \sum_i\sum_j b_j P(X=a_i, Y=b_j)$

$= \sum_ia_i(\sum_j P(X=a_i, Y=b_j)) + \sum_j b_j(\sum_i P(X=a_i, Y=b_j))$

$= \sum_i a_i P(X=a_i) + \sum_j b_j P(Y=b_j)$

$= \mathbb{E}[X] + \mathbb{E}[Y]$

$\therefore \mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]$

> ## The Change of Variable Formula

Let $X$ be a random variable and let $g: \mathbb{R} \rightarrow \mathbb{R}$ a function, then

If $X$ is **discrete** taking $a_1, a_2,..$,

\[[\mathbb{E}[g(X)]=\sum_ig(a_i)P(X=a_i)\]]

If $X$ is **continuous** with probability density function $f(x)$,

\[[\mathbb{E}[g(X)] = \int\_{-\infty}^{\infty}g(x)f(x)dx\]]

> ## Variance

The variance $Var(x)$ of a random variable $X$ is

\[[Var(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] \]]

Using the change of variable formula above, we can further simplify the variance equation.

$Var(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]$

$= \int_{-\infty}^{\infty}(x-\mathbb{E}[X])^2f(x)dx$

$= \int_{-\infty}^{\infty}(x^2 - 2x\mathbb{E}[X]+\mathbb{E}[X]^2)f(x)dx$

$= \int_{-\infty}^{\infty}x^2f(x)dx - 2\mathbb{E}[X] \int_{-\infty}^{\infty}xf(x)dx + \int_{-\infty}^{\infty} \mathbb{E}[X]^2f(x)dx$

$= \mathbb{E}[X^2] - 2\mathbb{E}[X]^2 + \mathbb{E}[X]^2 \int_{-\infty}^{\infty}f(x)dx$

$= \mathbb{E}[X^2] - 2\mathbb{E}[X]^2 + \mathbb{E}[X]^2$

$= \mathbb{E}[X^2] - \mathbb{E}[X]^2$

Hence, we can also express variance by,

\[[Var(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2\]]

Note that the square root of variance $\sqrt{Var(X)}$ is known as the **standard deviation**.

> ## Expectation and Variance under change-of-units

\[[\mathbb{E}[r X + s]=r \mathbb{E}[X]+s\]]

\[[Var(r X + s)=r^2Var(X)\]]

> ## Covariance

Let $X$ and $Y$ be random variables. The **covariance** between $X$ and $Y$ is defined by,

\[[Cov(X,Y) = \mathbb{E}[(X - \mathbb{E}[ X])(Y-\mathbb{E}[ Y])]\]]

Now, where does the above equation come from? Recall that,

$Var(X+Y)=\mathbb{E}[(X+Y-\mathbb{E}[X + Y])^2]\ \cdot \cdot\ \cdot\ (1)$

From the above equation, we can write

$X+Y-\mathbb{E}[X+Y] = X - \mathbb{E}[X] + Y - \mathbb{E}[Y]$.

$(X+Y-\mathbb{E}[X+Y])^2 = (X-\mathbb{E}[X])^2 + (Y-\mathbb{E}[Y])^2 + 2(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])$

Put into $(1)$,

$\mathbb{E}[(X+Y-\mathbb{E}[X + Y])^2] = \mathbb{E}[(X-\mathbb{E}[X ])^2 + (Y-\mathbb{E}[Y])^2 + 2(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]$

$= Var(X) + Var(Y) + 2 \mathbb{E}[(X-\mathbb{E}[X ])(Y-\mathbb{E}[Y])]$

\[[\therefore Var(X+Y) = Var(X) + Var(Y) + 2 \mathbb{E}[(X -\mathbb{E}[X])(Y-\mathbb{E}[Y])]\ \cdot \cdot \cdot (2)\]]

The half of the last term in $(2)$ denotes the **covariance**.

> ## Alternative definition of covariance

\[[ Cov(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] \]]

> ## Meanings of Covariance

1. $Cov(X,Y)>0 \Longrightarrow$ **Positively** correlated
2. $Cov(X,Y)<0 \Longrightarrow$ **Negatively** correlated
3. $Cov(X,Y)=0 \Longrightarrow$ **Uncorrelated**

Here, positive correlation means that if $X$ has a realization **larger than** $\mathbb{E}[X]$, then it is likely that $Y$ will also have a realization **larger than** $\mathbb{E}[Y]$, similarly for negative correlation.

Note that $\mathbb{E}[XY] \neq \mathbb{E}[X]\mathbb{E}[Y]$ unless $X$ and $Y$ are uncorrelated.

> ## Independence vs Uncorrelation

1. $X$ and $Y$ are **uncorrelated**

\[[ \mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y] \]]

\[[ Cov(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]=0 \]]

2. $X$ and $Y$ are **independent**

\[[ P_{XY}(x,y) = P_X(x)P_Y(y) \]]

> ## Independence guarantees Uncorrelation

[1] For **discrete**

$\mathbb{E}[XY] = \sum_i\sum_j a_ib_j P(X=a_i, Y=b_j)$. By the definition of **independence**,

$= \sum_i\sum_j a_i b_j P(X=a_i)P(Y=b_j)$

$= \sum_i a_i P(X=a_i) \cdot \sum_j b_j P(Y=b_j)$

$= \mathbb{E}[X] \mathbb{E}[Y]$

[2] For **continuous**,

$\mathbb{E}[XY] = \iint_{xy}P_{XY}(x,y)dxdy$. By the definition of **independence**,

$= \iint xP_X(x) \cdot yP_Y(y)dxdy$

$= \int xP_X(x)dx \cdot \int yP_Y(y)dy$

$= \mathbb{E}[X] \mathbb{E}[Y]$

\[[\therefore\ independence \Longrightarrow uncorrelation\]]

> ## Covariance Matrix

The **covariance matrix** of a random vector $x \in \mathbb{R}^n$ is an $n \times n$ matrix, such tat

\[[Cov(x)_{i,j} = Cov(x_i, y_j)\]]

The **diagonal** elements of the covariance matrix give the **variance**:

\[[Cov(x_i, x_i) = Var(x_i)\]]

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/)  
[2] _A Modern Introduction to Probability and Statistics by Dekking_
