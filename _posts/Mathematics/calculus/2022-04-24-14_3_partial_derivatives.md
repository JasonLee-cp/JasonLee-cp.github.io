---
layout: null
title: "[Calculus] Partial Derivatives"
categories: ["calculus"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Partial Deriviatives

If $f$ is a function of two variables $x$ and $y$, then

Partial derivative of $f$ w.r.t $x$ at $(a,b)$ is

\[[ f_x(a,b) = \lim_{h \rightarrow 0} \frac{f(a+h, b) - f(a,b)}{h} \]]

Partial derivative of $f$ w.r.t $y$ at $(a, b)$ is

\[[ f_y(a,b) = \lim_{h \rightarrow 0} \frac{f(a,b+h)-f(a,b)}{h} \]]

> # Notations for Partial Derivatives

If $z=f(x,y)$, we write

\[[ \frac{\partial f}{\partial x} = \frac{\partial}{\partial x}f(x,y) = \frac{\partial z}{\partial x} = f_x = D_xf=D_1f=f_1=f_x(x,y) \]]

Same for y.

> # Rules for finding Partial Derivatives of $z=f(x,y)$

**[1]** To find $\frac{\partial f}{\partial x}$, regard $y$ as a **constant** and differentiate $f(x,y)$ w.r.t $x$.

**[2]** To find $\frac{\partial f}{\partial y}$, regard $x$ as a **constant** and differentiate $f(x,y)$ w.r.t $y$.

> # Functions of more than two variables

If $u$ is a function of $n$ variables, $u=f(x_1,...,x_n)$, then its partial derivative w.r.t. $x_i$ is

\[[ \frac{\partial u}{\partial x_i} = \lim_{h \rightarrow 0} \frac{f(x_1,x_2,...,x_i+h,...,x_n)-f(x_1,...,x_n)}{h} \]]

> # Higher Derivatives

If $f$ is a function of two variables, then its partial derivatives $f_x$ and $f_y$ are also functions of two variables so we can consider their partial derivatives $(f_x)_x, (f_x)_y, (f_y)_x, (f_y)_y$ which are called the **second partial derivatives** of $f$. If $z=f(x,y)$, then the second partial derivatives are

\[[ (f_x)_y = \frac{\partial}{\partial y}(\frac{\partial f}{\partial x}) = \frac{\partial^2 f}{\partial y \partial x} \]]

\[[ (f_y)_x = \frac{\partial}{\partial x}(\frac{\partial f}{\partial y}) = \frac{\partial^2 f}{\partial x \partial y} \]]

> # Clairaut's Theorem

Suppose $f$ is defined on a Disk $D$ that contains the point $(a,b)$. If the function $f_{xy}$ and $f_{yx}$ are both continuous on $D$, then

\[[ f_{xy}(a,b) = f_{yx}(a,b) \]]

> # Exercises

## Q35

Find the first partial derivatives of the function

\[[ p = \sqrt{t^4 + u^2 \cos{v}} \]]

\[[ p_t = \frac{2t^3}{\sqrt{t^4+u^2\cos{v}}} \]]

\[[ p_u = \frac{u \cos{v}}{\sqrt{t^4+u^2\cos{v}}} \]]

\[[ p_v = \frac{-u^2 \sin{v}}{2\sqrt{t^4+u^2\cos{v}}} \]]

## Q49

Use implicit differentiation to find $\frac{\partial z}{\partial x}$

\[[ e^z \frac{\partial z}{\partial x} = \frac{\partial z}{\partial x} xy + yz \]]

\[[ \therefore \frac{\partial z}{\partial x} = \frac{yz}{e^z - xy} \]]

## Q52

Find $\frac{\partial z}{\partial x}$.

\[[ (a)\ z = f(x)g(y) \]]

\[[ (b)\ z=f(xy) \]]

\[[ (c)\ z = f(x/y) \]]

For (a),

\[[ \frac{\partial z}{\partial x} = f'(x)g(y) \]]

For (b),

\[[ \frac{\partial z}{\partial x} = f'(xy)y \]]

For (c),

\[[ \frac{\partial z}{\partial x} = \frac{f'(x/y)}{y} \]]

## Q62

Verify that the conclusion of Clairaut's Theorem hold: $u_{xy} = u_{yx}$.

\[[ u = \ln(x+2y) \]]

\[[ u_{xy} = -2(x+2y)^{-2} \]]

\[[ u_{yx} = -2(x+2y)^{-2} \]]

## Q80

If $u = e^{a_1x_1+a_2x_2+ \cdots + a_nx_n}$, where $a_1^2+a_2^2+ \cdots + a_n^2 = 1$, show that

\[[ \frac{\partial^2 u}{\partial x_1^2} + \frac{\partial^2 u}{\partial x_2^2} + \cdots + \frac{\partial^2 u}{\partial x_n^2} = u \]]

Let's find the second derivative of $u$ w.r.t $x_i$.

Also, let $a_1x_1+a_2x_2+ \cdots + a_nx_n = T$.

\[[ \frac{\partial u}{\partial x_i} = e^{T}a_i \]]

\[[ \frac{\partial^2 u}{\partial x_i^2} = e^{T}a_i^2 = ua_i^2 \]]

Hence,

\[[ \frac{\partial^2 u}{\partial x_1^2} + \frac{\partial^2 u}{\partial x_2^2} + \cdots + \frac{\partial^2 u}{\partial x_n^2} = u(a_1^2 + a_2^2 + \cdots + a_n^2) = u \]]

## Q97

You're told that there is a function $f$ whose partial derivatives are $f_x(x,y) = x + 4y$ and $f_y(x,y) = 3x - y$. Should you believe it?

Let's compute $f_{xy}$ and $f_{yx}$

\[[ f_{xy} = 4 \]]

\[[ f_{yx} = 3 \]]

By Clairaut's theorem, since they're different, such a function does not exist.

> # References

[1] Stewart Calculus 8th Edition
