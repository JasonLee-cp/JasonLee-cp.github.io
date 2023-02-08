---
layout: post
title: "[Statistics] 4.2 Inequalities for Expectations"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> # Inequalities for Expectations

> # Cauchy-Schwartz Inequality

If $$X$$ and $$Y$$ have finite variances, then

$$ \mathbb{E}\lvert XY \rvert \leq \sqrt{\mathbb{E}[X^2]\mathbb{E}[Y^2]} $$

> # Jensen's Inequality

If $$g$$ is **convex**, then

$$ \mathbb{E}[g(X)] \geq g(\mathbb{E}[X]) $$

If $$g$$ is **concave**, then

$$ \mathbb{E}[g(X)] \leq g(\mathbb{E}[X]) $$

## Convex and Concave

A function $$g$$ is **convex** if for each $$x,y$$ and each $$\alpha \in [0,1]$$,

$$ g(\alpha x + (1 - \alpha)y) \leq \alpha g(x) + (1-\alpha)g(y) $$

If $$g$$ is twice differentiable and $$g''(x) \geq 0$$ for all $$x$$, then $$g$$ ix **convex**.

A function $$g$$ is **concave** if $$-g$$ is convex.

> # References

[1] All of Statistics by Larry A. Wasserman
