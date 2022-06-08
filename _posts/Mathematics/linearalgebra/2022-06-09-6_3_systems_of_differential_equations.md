---
layout: single
title: "[Linear Algbera] 6.3 Systems of Differential Equations"
categories: ["linearalgebra"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Keywords

**[1]** If $Ax=\lambda x$ then $u(t) = e^{\lambda t}x$ will solve $\frac{du}{dt}=Au$. Each $\lambda$ and $x$ give a solution $e^{\lambda t}x$

**[2]** If $A = X \Lambda X^{-1}$ then $u(t)=e^{At}u(0)=Xe^{\Lambda t}X^{-1}u(0)=c_1 e^{\lambda_1t}x_1 + \cdots + c_n e^{\lambda_n t}x_n$

**[3]** $A$ is **stable** and $u(t) \rightarrow 0$ and $e^{At}\rightarrow 0$ when all eigenvalues of $A$ have real part $<0$.

**[4]** **Matrix exponential** $e^{At}=I + At + \cdots + (At)^n / n! + \cdots = X e^{\Lambda t}X^{-1}$ if $A$ is diagonalizable

**[5]** **Second order equation First order system**: $u'' + Bu' + Cu = 0$ is quivalent to $\begin{bmatrix} u \\\ u' \end{bmatrix}' = \begin{bmatrix} 0 & 1 \\\ -C & -B \end{bmatrix} \begin{bmatrix} u \\\ u' \end{bmatrix}$

> # Differential Equations

Eigenvalues and eigenvectors are perfect for $\frac{du}{dt}=Au$. As a prior knowledge, the derivative of $e^{\lambda t}$ is $\lambda e^{\lambda t}$.

The main point is to **convert constant-coefficient differential equations into linear algebra**.

The ordinary equations $\frac{du}{dt}=u$ and $\frac{du}{dt}=\lambda u$ are solved by exponentials:

$\frac{du}{dt}=u$ products $u(t)=Ce^t$

$\frac{du}{dt}=\lambda u$ produces $u(t)=Ce^{\lambda t}$.

When $t=0$, we have $u(0)=C$. The solutions that start from $u(0)$ at $t=0$ are

\[[ u(t) = u(0)e^t \]]

\[[ u(t)=u(0)e^{\lambda t} \]]

This is the 1 by 1 case. Let's generalize to n by n. The unknown is a vector $u$. We start from the initial vector $u(0)$ and the $n$ equations contain a square matrix $A$. We expect $n$ exponents $e^{\lambda t}$ in $u(t)$, from $n$ $\lambda's$

\[[ \frac{du}{dt}=Au,\ \ u(0)=\begin{bmatrix} u_1(0) \\\ \cdots \\\ u_n(0) \end{bmatrix}\ \text{at}\ t=0 \]]

These differential equations are **linear** which means if $u(t)$ and $v(t)$ are solutions, so is $Cu(t)+Dv(t)$. Thus, the first job is to **find n "pure exponential solutions"** $u=e^{\lambda t}x$ by using $Ax=\lambda x$.

Notice that $A$ is a **constant matrix**. So $\frac{du}{dt}=Au$ is "linear with constant coefficients".

> Solve linear constant coefficient equations by exponentials $e^{\lambda t}x$, when $Ax=\lambda x$

> # Solution of $\frac{du}{dt}=Au$

## Pure exponential solution

The **pure exponential solution** is $e^{\lambda x}$ times a fixed vector $x$. $\lambda$ is an **eigenvalue** of $A$ and $x$ is the **eigenvector**.

> Choose $u=e^{\lambda t}x$ when $Ax=\lambda x$. Then, $\frac{du}{dt}=\lambda e^{\lambda t}x$ agrees with $Au = A e^{\lambda t} x$

After we fine the pure exponential solutions, the **complete solution** is the **linear combination** of those pure solutions

## Complete solution

\[[ u(t) = Cu_1(t) + Du_2(t) \]]

> # Summary: Three steps

**[1]** Write $u(0)$ as a **combination** $c_1x_1 + \cdots + c_n x_n$ **of the eigenvectors of A**

**[2]** Multiply each eigenvector $x_i$ by its **growth factor** $e^{\lambda_i t}$.

**[3]** The solution is the same combination of those pure solutions $e^{\lambda t}x$

\[[ \frac{du}{dt}=Au \]]

\[[ u(t) = c_1 e^{\lambda_1 t}x_1 + \cdots + c_n e^{\lambda_n t}x_n \]]

> # References

[1] Introduction to Linear Algebra, 5th edition
