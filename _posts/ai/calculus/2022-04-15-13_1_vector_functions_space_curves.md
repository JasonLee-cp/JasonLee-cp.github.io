---
layout: post
title: "[Calculus] 13.1 Vector Functions"
subtitle: ""
categories: ai
tags: calculus
comments:
---

> # Vector functions and space curves

Vector function is a function whose **domain** is a **set of real numbers** and whose **range** is a **set of vectors**. We're interested in vector function $$r$$. For every number $$t$$ in the domain of $$r$$, there's a **unique vector** in $$V_3$$ denoted by $$r(t)$$.

$$ r(t) = \begin{pmatrix} f(t) \\\ g(t) \\\ h(t) \end{pmatrix} = f(t)\hat{i}+g(t)\hat{j}+h(t)\hat{k} $$

where $$f, g, h$$ are **component functions**.

> # Limits and Continuity

If $$r(t) = \begin{pmatrix} f(t) \\\ g(t) \\\ h(t) \end{pmatrix}$$, then

$$ \lim*{t \rightarrow a}r(t) = \begin{pmatrix} \lim*{t \rightarrow a}f(t) \\\ \lim*{t \rightarrow a}g(t) \\\ \lim*{t \rightarrow a}h(t) \end{pmatrix} $$

provided that limits of component functions exist.

> # Continuity

A vector function $$r$$ is **continuous** at $$a$$ if

$$ \lim\_{t \rightarrow a} r(t) = r(a) $$

which means that $$r$$ is continuous if and only if $$f, g, h$$ are continuous at $$a$$.

> # Space Curves

![joint](/assets/img/MATH/calculus/ch13_1.png)

Suppose $$f, g, h$$ are **continuous real-valued functions** on $$I$$, then the set $$C$$ of **all points** $$(x,y,z)$$ in space, where

$$ x=f(t),\ y=g(t),\ z=h(t) \cdots (1) $$

and $$t$$ varies throughout $$I$$, is called **space curve**.

The equation $$(1)$$ is **parametric equation** of $$C$$ and $$t$$ is **parameter**.

$$r(t) = \begin{pmatrix} f(t) \\\ g(t) \\\ h(t) \end{pmatrix}$$ is the **position vector** of $$C$$.

> # Exercises

## Q1

Find the domain of the vector function

$$ r(t) = \left\langle \ln(t+1), \frac{t}{\sqrt{9-t^2}}, 2^t \right\rangle $$

It must satisfy $$t+1>0 \rightarrow t > -1$$ and $$t^2<9 \rightarrow -3<t<3$$,

$$\therefore -1 < t < 3$$

## Q5

Find the limit.

$$ \lim\_{t \rightarrow \infty} \left\langle \frac{1+t^2}{1-t^2}, tan^{-1}t, \frac{1-e^{-2t}}{t} \right\rangle $$

$$ = \lim\_{t \rightarrow \infty} \left\langle \frac{1/t^2+1}{1/t^2-1}, \frac{\pi}{2}, \frac{1-1/e^{2t}}{t} \right\rangle $$

$$
= \left\langle -1, \frac{\pi}{2}, 0
\right\rangle
$$

## Q19

Find a **vector equation** and **parametric equations** for the line segment that joins $$P$$ to $$Q$$.

$$ P=(0,-1,1),\ Q=(\frac{1}{2},\frac{1}{3},\frac{1}{4}) $$

Recall that the line segment from $$r_0$$ to $$r_1$$ is

$$ r(t)=r_0 + t(r_1-r_0), 0 \leq t \leq 1 $$

$$ = (1-t)r*0 + tr*, \ 0 \leq t \leq 1 $$

Hence, we can substitue $$P$$ and $$Q$$ in to the equation.

$$ r(t) = (1-t) \left\langle 0, -1, 1 \right\rangle + t \left\langle \frac{1}{2}, \frac{1}{3}, \frac{1}{4} \right\rangle,\ 0 \leq t \leq 1 $$

$$ = \left\langle \frac{1}{2}t, \frac{4}{3}t-1, -\frac{3}{4}t+1 \right\rangle,\ 0 \leq t \leq 1 $$

The parametric equations are

$$ x = \frac{1}{2}t $$

$$ y = \frac{4}{3}t-1 $$

$$ z = -\frac{3}{4}t+1 $$

for $$0 \leq t \leq 1$$

## Q27

Show that the curve with parametric equations $$x=t\cos{t}$$, $$y=t\sin{t}$$, $$z=t$$ lies on the cone $$z^2=x^2+y^2$$.

To show, we can simply put each parametric equation into the equation of cone.

$$ t^2 = t^2\cos^2{t}+t^2\sin^2{t} $$
$$ t^2 = t^2 $$

We can see that the parametric equations lie on the cone.

## Q43

The a vector function that represents the curve of intersection of the two surfaces:

$$ z=\sqrt{x^2+y^2} $$

$$ z = 1 + y $$

As we want to find the **curve** of the intersection, we're interested in all the points that satisfy **both** equations. Substitute $$z$$.

$$ (1+y)^2 = x^2 + y^2 $$

$$ x^2-2y-1=0 $$

$$ y = \frac{x^2-1}{2} $$

If we set $$x=t$$ to parametrize,

$$ x=t $$

$$ y = \frac{t^2-1}{2} $$

$$ z = \frac{t^2+1}{2} $$

Hence,

$$ r(t) = \left\langle t, \frac{t^2-1}{2}, \frac{t^2+1}{2} \right\rangle $$

> # References

[1] Stewart Calculus 8th Edition
