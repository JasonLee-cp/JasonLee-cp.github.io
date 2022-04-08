---
layout: single
title: "[DL] Regularization"
categories: ["deeplearning"]
tag: [deeplearning]

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Regualrization

So far, we've only talked about increasing and decreasing the model's representational capacity. However, the behavior of our algorithm is not only affected by the set of functions allowed in its hypothesis space but also by the **specific identity** of those functions. For example, if you use $sin(x)$ for a linear regression problem, it would not perform well.

We can also give a learning algorithm a **preference** for one solution over another in its hypothesis space. In other words, the preferred solution is more likely to minimize our object function or loss function. The unpreferred solution will be chosen only if it fits significantly better than the preferred solution.

## Weight Decay

We can modify the loss function to include **weight decay** term. Instead of just minimizing the MSE loss, we also include $\lambda w^{\top}w$ that expresses a preference for the weights to have **smaller squared** $L^2$ norm.

\[[ J(w) = MSE_{train} + \lambda w^{\top}w \]]

where $\lambda$ is a hyperparameter that determines the **strength** of our preference for smaller weights.

More generally, we can regularize a model that learns a function $f(x; \theta)$ by adding a **penalty** called a **regularizer** to the cost function.

This way of expressing preferences for different solutions are known as **regularization**. Regularization is any modification we make to a learning algorithm that is intended to reduce its genralization error but not its training error.
