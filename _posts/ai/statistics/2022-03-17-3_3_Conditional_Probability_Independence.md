---
layout: post
title: "[Statistics] Conditional Probability and Independence"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> ## Conditional Probability

The conditional probability of $$A$$ **given** C is,

$$P(A\|C)=\frac{P(A \cap B)}{P(C)},\ P(C)>0$$

> ## Multiplication Rule

From the definition of conditional probability, we can write that

$$P(A \cap C) = P(A\|C)P(C)$$

> ## Chain Rule of Conditional Probability

Any joint probability distribution over multiple random variables can be **decomposed** into conditional probabilities over only one variable:

$$ P(x^{(1)},...,x^{(n)})=P(x^{(1)}) \prod\_{i=2}^n P(x^{(i)} \| x^{(1)},...,x^{(i-1)}) $$

For example, $$P(a,b,c)$$ can be decomposed as either of,

$$P(a,b,c) = P(c)P(b\|c)P(a\|b,c)$$

$$P(a,b,c) = P(a)P(b\|a)P(c\|a,b)$$

> ## Independence and Conditional Independence

Two random variables $$X$$ and $$Y$$ are **independent** if

$$\forall x \in X, y \in Y,\ P(x,y) = P(x)P(y)$$

Two random variables $$X$$ and $$Y$$ are **conditionally independent** given a random variable $$Z$$ if

$$\forall x \in X, y \in Y, z \in Z,\ P(x,y\|z)=P(x\|z)P(y\|z)$$

$$X \perp Y$$ indicates $$X$$ and $$Y$$ are independent.

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/)  
[2] _A Modern Introduction to Probability and Statistics by Dekking_
