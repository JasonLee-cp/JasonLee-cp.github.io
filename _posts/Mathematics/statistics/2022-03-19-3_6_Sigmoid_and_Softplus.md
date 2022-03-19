---
layout: null
title: "[Statistics] Sigmoid and Softplus"
categories: ["statistics"]
tag: [math]
---

> ## Logistic Sigmoid

\[[ \sigma(x) = \frac{1}{1+exp(-x)} \]]

|          ![joint](../../assets/images/statistics/images/sigmoid.png)          |
| :---------------------------------------------------------------------------: |
| _[deeplearningbook.org](https://www.deeplearningbook.org/contents/prob.html)_ |

The logistic sigmoid function is commonly used to produce the $\phi$ parameter of a **Bernoulli distribution** since the sigmoid function is bounded to the range $[0,1]$. An important thing to note is that as $x$ gets largs or small, it **saturates** which means it becomes very flat and **insensitive** to small changes for the input.

**Some useful equations of sigmoid**

\[[ \sigma(x) = \frac{exp(x)}{1 + exp(x)} \]]

\[[ \frac{d}{dx}\sigma(x) = \sigma(x)(1-\sigma(x)) \]]

\[[ 1 - \sigma(x) = \sigma(-x) \]]

\[[ \forall x \in (0,1), \sigma^{-1}(x)=log \left( \frac{x}{1-x} \right) \]]

> ## Softplus function

\[[ \zeta(x)=log(1+exp(x)) \]]

|         ![joint](../../assets/images/statistics/images/softplus.png)          |
| :---------------------------------------------------------------------------: |
| _[deeplearningbook.org](https://www.deeplearningbook.org/contents/prob.html)_ |

The softplux function is useful when producing the $\beta$ or $\sigma$ parameter of a **normal distribution** since the softplus has range $(0, \infty)$.

**Some useful equations of softplus**

\[[ log \sigma(x) = -\zeta(-x) \]]

\[[ \frac{d}{dx}\zeta(x)=\sigma(x) \]]

\[[ \forall x>0, \zeta^{-1}(x) = log(exp(x)-1) \]]

\[[ \zeta(x) = \int_{-\infty}^x \sigma(y)dy \]]

\[[ \zeta(x)-\zeta(-x)=x \]]

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/)  
[2] _A Modern Introduction to Probability and Statistics by Dekking_
