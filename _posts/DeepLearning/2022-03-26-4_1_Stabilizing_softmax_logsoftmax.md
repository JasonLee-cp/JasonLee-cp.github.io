---
layout: single
title: "[DL] Stabilizing Softmax and Logsoftmax functions to avoid underflow and overflow"
categories: ["deeplearning"]
tag: [machine-learning]

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

Machine learning algorithms inevitably incur a high amount of numerical computations. Typical cases include solving optimization problem by an iterative process such as gradient descent. However, even modern day computers cannot perfectly represent all the real numbers, especially floating-point numbers due to the finite memory space, resulting in **approximation errors**. In many cases, this is just the **rounding errors**. The rounding errors are problematic especially when they get compounded and the optimization algorithm fail to minimize the accumulation of rounding error.

> ## Underflow

One type of rounding errors is **underflow** which is sometimes devastating. Underflow occurs when numbers **near zero** are rounded to zero. This might cause some serious problems.

The first potential problem is that small numbers that are rounded to zero might be essential for optimization. Some algorithms might take great importance on the numbers that are near zero.

Another problem is that functions might behave qualitatively differently when their argument is exactly zero rather than a small positive number.

> ## Overflow

Overflow is another unpromising type of rounding errors where large numbers are approximated as $-\infty$ or $\infty$. Further arithmetic operations might change these infinite values into NaN.

> ## Modified Softmax Function

One example of a function that must be **stabilized** to avoid underflow and overflow is the **softmax function**. Although softmax function is widely used in deep learning literature, it might result in underflow and overflow.

\[[ softmax(\vec{x})\_i = \frac{exp(\vec{x}\_i)}{\sum\_{j=1}^n exp(\vec{x}\_j)} \]]

Consider the case when all the $x_i$ are equal to some constant $c$. Then,

- When $c$ becomes **very large and positive**, **overflow** occurs since $exp(c)$ in the numerator will be infinitely large.
- When $c$ becomes **very small and negative**, **underflow** occurs since the denominator of the softmax function $\sum_{j=1}^n \frac{1}{e^{\infty}}$ will become $0$.

The softmax function can be stabilized by instead evaluating $softmax(z)$ where $\vec{z} = \vec{x} - max(\vec{x}_i)$.

Then, the largest element in the vector will become $0$ it rules out the possibility of overflow. Likewise, since at least one term(maximum element which becomes 0) in the denominator will be 1 ($exp(0)$=1), the possibility of underflow is also ruled out.

It can be simply proved that the value of the softmax function **doesn't change** with addition or subtraction of a scalar $c$ to the input vector.

**[Proof]**
\[[ softmax(\vec{x})\_i = \frac{exp(\vec{x}\_i)}{\sum_{j=1}^n exp(\vec{x}\_j)} \]]

\[[ softmax(\vec{x}+c)\_i = \frac{exp((\vec{x}+c)\_i)}{\sum_{j=1}^n exp((\vec{x}+c)\_j)} = \frac{exp(\vec{x}\_i+c)}{\sum_{j=1}^n exp(\vec{x}\_j+c)} \]]

\[[ = \frac{exp(\vec{x}\_i+c)}{\sum\_{j=1}^n exp(\vec{x}\_j+c)} \cdot \frac{exp(-c)}{exp(-c)} = \frac{exp(\vec{x}\_i)}{\sum_{j=1}^n exp(\vec{x}\_j)} \]]

However, we still have to deal with one problem. The modified softmax function can still cause **underflow** when evaluating $logsoftmax(\vec{x})$. When the numerator of the previously modified softmax function becomes $0$, then $logsoftmax(0)$ will be evaluated as -$\infty$. The logsoftmax function can be stabilized with the same trick we used for the softmax function.

With a similar strategy prove, we can prove that $logsoftmax(\vec{x}) = logsoftmax(\vec{x}+k)$ for a constant $k$. Hence, let's evaluate $logsoftmax(\vec{x}-max(\vec{x}\_i))$ to avoid rounding errors.

\[[ logsoftmax(\vec{x}-max(x_i)) = log \left( \frac{exp(\vec{x}\_i - max(x_i))}{\sum_{j=1}^n exp(\vec{x}\_j - max(x_i))} \right) \]]

\[[ = log \left( exp(\vec{x}\_i - max(x_i)) \right) - log \left( \sum_{j=1}^n exp(\vec{x}\_j - max(x_i)) \right) \]]

\[[ = \vec{x}\_i - max(x_i) - log \left( \sum_{j=1}^n exp(\vec{x}\_j - max(x_i)) \right) \]]

Consequently, evaluating $logsoftmax(\vec{x}_i - max(x_i))$ instead ensures prevention of both the overflow and underflow since the maximum element of $\vec{x}$ now becomes $0$ as it's subracted by $max(x_i)$, making $exp(\vec{x}\_j - max(x_i)) = exp(0) = 1$ so the term inside the log will never become $0$.

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/) Ch.4.
