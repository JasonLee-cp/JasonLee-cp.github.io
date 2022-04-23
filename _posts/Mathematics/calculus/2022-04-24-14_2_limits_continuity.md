---
layout: null
title: "[Calculus] Limits and Continuity of Multivariate Functions"
categories: ["calculus"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Limits and Continuity

Let $f$ be a function of two variables whose domain $D$ includes points arbitrarily close $(a,b)$. Then, we say

\[[ \lim_{(x,y)\rightarrow (a,b)}f(x,y) = L \]]

if for every number $\epsilon > 0$, there's a corresponding $\delta > 0$ such that

if $(x,y) \in D$ and $0 < \sqrt{(x-a)^2 + (y-b)^2} < \delta$, then $\lvert f(x,y) - L \rvert < \epsilon$

> # Existence of Limit

Unlike univariate function where we can test by $\lim_{x \rightarrow a^{+}} f(x)= \lim_{x \rightarrow a^{-}}f(x)$ because there're only two directions.

However, it's not that simple for multivariate functions since there're infinite number of directions.

## Definition

If $f(x,y) \rightarrow \rightarrow L_1$ as $(x,y) \rightarrow (a,b)$ along a path $C_1$,

and $f(x,y) \rightarrow \rightarrow L_2$ as $(x,y) \rightarrow (a,b)$ along a path $C_2$,

where $L_1 \neq L_2$, then $\lim_{x,y \rightarrow a,b}f(x)$ does NOT exist.

**Example.** Show $\lim_{x,y \rightarrow 0,0} \frac{x^2-y^2}{x^2 + y^2}$ does not exit.

1. Approach along x-axis

-> $y=0$ gives $f(x,0)=1$, so $\lim_{x,y \rightarrow 0,0}f(x,0) = 1$

2. Approach along y-axis

-> $x=0$ gives $f(0,y) = -1$ so $\lim_{x,y \rightarrow 0,0}f(0,y)=-1$

Since $1 \neq -1$, the limit does not exist for $x,y \rightarrow 0,0$.

> # Continuity

A function of two variables is called continuous at $(a,b)$ if

\[[ \lim_{x,y \rightarrow a,b}f(x,y) = f(a,b) \]]

We say $f$ is is continuous on $D$ if $f$ is continuous at every point $(a,b)$ in $D$.

> # Exercises

## Q13

Find the limit, if it exists, or show that the limit does not exit.

\[[ \lim_{x,y \rightarrow 0,0} \frac{xy}{\sqrt{x^2+y^2}} \]]

To prove that the limit exists, we use the definition of the existence of limit.

Choose any $\epsilon > 0$. We must show that there exists $\delta > 0$ such that if $0 < \sqrt{x^2 + y^2} < \delta$, then $\rvert \frac{xy}{\sqrt{x^2+y^2}} \rvert < \epsilon$.

\[[ x^2 \leq x^2 + y^2 \]]

\[[ \lvert x \rvert \leq \sqrt{x^2 + y^2} \]]

\[[ \frac{\lvert x \rvert}{\sqrt{x^2+y^2}} \leq 1 \]]

\[[ \frac{\lvert x \rvert \lvert y \rvert}{\sqrt{x^2+y^2}} \leq \lvert y \rvert \]]

Also,

\[[ y^2 \leq x^2 + y^2 \]]

\[[ \lvert y \rvert \leq \sqrt{x^2+y^2} \]]

Therefore,

\[[ \frac{\lvert x \rvert \lvert y \rvert}{\sqrt{x^2+y^2}} \leq \lvert y \rvert \leq \sqrt{x^2+y^2} \]]

We made an assumption: $0 < \sqrt{x^2 + y^2} < \delta$. Hence,

\[[ \frac{\lvert x \rvert \lvert y \rvert}{\sqrt{x^2+y^2}} \leq \lvert y \rvert \leq \sqrt{x^2+y^2} < \delta \]]

If we choose $\delta = \epsilon$. Then,

\[[ \frac{\lvert x \rvert \lvert y \rvert}{\sqrt{x^2+y^2}} < \delta \]]

We showed that the limit indeed exists.

## Q17

Find the limit, if it exists, or show that the limit does not exist.

\[[ \lim_{x,y \rightarrow 0,0} \frac{x^2+y^2}{\sqrt{x^2+y^2+1}-1} \]]

For approaching along x-axis (y=0),

\[[ \lim_{x \rightarrow 0}\frac{x^2}{\sqrt{x^2+1}-1} = 0 \]]

For approaching along $y=\sqrt{2x}$,

\[[ \lim_{x \rightarrow 0} \frac{x^2 + 2x}{x+1-1} = 2 \]]

Since they're different, the limit does not exist.

## Q37

## Q39

Use polar coordinates to find the limit.

\[[ \lim_{x,y \rightarrow 0,0} \frac{x^3+y^3}{x^2+y^2} \]]

In polar coordinates, $x=r\cos{\theta}, y=r\sin{\theta}$.

\[[ \lim_{r \rightarrow 0^{+}}\frac{r^3\cos^3{\theta} + r^3\sin^3{\theta}}{r^2\cos^2{\theta}+r^2\sin^2{\theta}} \]]

\[[ \lim_{r \rightarrow 0^{+}}r(cos^3{\theta}+sin^3{\theta}) \]]

\[[ = 0 \]]

## Q41

Use polar coordinates to find the limit.

\[[ \lim_{x,y \rightarrow 0,0} \frac{e^{-x^2-y^2}-1}{x^2+y^2} \]]

Using the similar approach, we can show that the answer is $-1$.

## Q45

Show that the function $f$ giben by $f(x) = \lvert x \rvert$ is continuous on $\mathbb{R}^n$. Hint: Consider $\lvert x - a \rvert^2 = (x - a) \cdot (x-a)$.

We must show the limit $\lim_{x \rightarrow a}f(x) = L$ exists at an arbitrary $a$.

Then, we need to show that for every $\epsilon > 0$, there exists a corresponding $\delta > 0$ such that if $0 < \lvert x - a \rvert < \delta$, then $\lvert f(x) - L \rvert < \epsilon$.

By the reverse triangle inequality,

\[[ \lvert x - a \rvert \geq \lvert \lvert x \rvert - \lvert a \rvert \rvert \]]

By our assumption $0 < \lvert x - a \vert < \delta$, we have

\[[ \lvert \lvert x \rvert - \lvert a \rvert \rvert \leq \lvert x - a \rvert < \delta \]]

Since $f(x) = \lvert x \rvert$ and $\lim_{x \rightarrow a}\lvert x \rvert = \lvert a \rvert = L$

\[[ \lvert  f(x) - L  \rvert < \delta \]]

Hence, $f(x)$ is continuous on $\mathbb{R}^n$.

> # References

[1] Stewart Calculus 8th Edition
