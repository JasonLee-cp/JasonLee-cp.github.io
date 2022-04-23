---
layout: single
title: "[Linear Algbera] Length and Dot Product"
categories: ["linearalgebra"]
tag: []

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Dot Product

The **dot product** or **inner product** of $\vec{v}= \begin{pmatrix} v_1 \\\ v_2 \end{pmatrix}$ and $\vec{w}= \begin{pmatrix} w_1 \\\ w_2 \end{pmatrix}$ is

\[[ \vec{v} \cdot \vec{w} = v_1w_1 + v_2w_2 \]]

## Perpendicular

If $\vec{v} \cdot \vec{w}=0$, $\vec{v}$ and $\vec{w}$ are **perpendicular**.

## Length

The length $\lvert \lvert \vec{v} \rvert \rvert$ of a vector $\vec{v}$ is

\[[ \lvert \lvert \vec{v} \rvert \rvert = \sqrt{\vec{v} \cdot \vec{v}} \]]

> # Unit Vector

A **unit vector** $\vec{u}$ is a vector whose **length** is 1.

\[[ \lvert \lvert \vec{u} \rvert \rvert = 1 \]]

To any non-zero vector $\vec{v}$, **divide by its length** to obtain a unit vector in the same direction as $\vec{v}$

\[[ \vec{u} = \frac{\vec{v}}{\lvert \lvert \vec{v} \rvert \rvert} \]]

## Standard Unit Vector

The standard unit vectors along x-axis and y-axis are $\hat{i}$ and $\hat{j}$.

> # Angle between vectors

The angle betweeen $\vec{v}$ and $\vec{w}$ is,

\[[ \cos \theta = \frac{\vec{v}}{\lvert \lvert \vec{v} \rvert \rvert} \frac{\vec{w}}{\lvert \lvert \vec{w} \rvert \rvert} \]]

\[[ = \vec{u} \cdot \vec{U} \]]

where $\vec{u}$ and $\vec{U}$ are the unit vectors of $\vec{v}$ and $\vec{w}$.

We can see that the two vectors are perpendicular or $\theta = 90$ when $\vec{v} \cdot \vec{w}=0$

> # Schwarz Inquality

\[[ \lvert \vec{v} \cdot \vec{w} \rvert \leq \lvert \lvert \vec{v} \rvert \rvert + \lvert \lvert \vec{w} \rvert \rvert \]]

> # Triangle Inequality

\[[ \lvert \lvert \vec{v} + \vec{w} \rvert \rvert \leq \lvert \lvert \vec{v} \rvert \rvert + \lvert \lvert \vec{w} \rvert \rvert \]]

> # References

[1] Introduction to Linear Algebra, 5th Edition
