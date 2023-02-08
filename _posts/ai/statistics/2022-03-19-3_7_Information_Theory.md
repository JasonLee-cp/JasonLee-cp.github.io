---
layout: post
title: "[Information Theory] Shannon Entropy, Cross Entropy, and Kullback-Leibler(KL) Divergence"
subtitle: ""
categories: ai
tags: statistics
comments:
---

> ## Information Theory

**Information theory** is a branch of applied mathematics quantifying how much information is present in a signal. In this post, we'll look at a few key ideas of information theory that are useful in the machine learning context.

The basic intuition of information theory is that learning of an **unlikely** event is more informative than learning of a likely event. For example, a message saying "there're cars in the street" is uninformative and unnecessary to send but "there was a car accident in the street" is informative. We would like to **quantify** information to formalize this intuition:

1. **Likely** events should have **low information** content
2. **Less likely** events should have **higher information** content
3. **Independent** events should have **additive** information

To satify all three properties, we define the **self-information** of an event $$X=x$$ to be

$$ I(x) = -logP(x) $$

I(x) is in units of **nats** where one nat is the **amount of information gaine by observing an event of probability** $$\frac{1}{e}$$. The logarithm here means natural logarithm. When base-2 log is used, then units are called **bits** or **shannons**.

> ## Shannon Entropy

When $$X$$ is a continuous random variable, some properties from the discrete case are lost.

Self-information deals only with a **single outcome**. **Shannon entropy** quantifies the **amount of uncertainty** in an entire probability distribution.

$$ H(X) = \mathbb{E}\_{X \sim P}[ I(x) ] = -\mathbb{E}\_{X \sim P}[ \log P(x) ] $$

and is also denoted $$H(P)$$.

The Shannon entropy of a distribution is the **expected amount of information** in an event drawn from that distribution. Distributions that are very deterministic have low entropy and distributions closer to uniform have high entropy.

When $$X$$ is a continuous random variable, the Shannon entropy is also called as **differential entropy**.

|              ![joint](/assets/img/statistics/images/shannon.png)              |
| :---------------------------------------------------------------------------: |
| _[deeplearningbook.org](https://www.deeplearningbook.org/contents/prob.html)_ |

The above figure illustrates the Shannon entropy of a binary random variable. The x-axis plots the probability of the random variable of being equal to $$1$$. The shannon entropy is at its highest when $$p=0.5$$ since it's closer to uniform , suggesting that it's not leaning towards one outcome. However, when $$p=0$$ or $$p=1.0$$, the shannon entropy goes down to $$0$$ since the expected outcome is "deterministic" or we know for sure that the realization of the random variable will be $$1$$ when $$p=1.0$$.

> ## Kullback-Leibler (KL) divergence

What about the case you want to measure **how different two distributions are**? The Kullback-Leibler (KL) divergence tells us the degree of difference between the two probability distributions $$P(x)$$ and $$Q(x)$$.

$$ D\_{KL}(P\|\|Q) = \mathbb{E}\_{X \sim P} \left[ log\frac{P(x)}{Q(x)} \right] = \mathbb{E}\_{X \sim P}[ \log P(x) - \log Q(x) ] $$

One useful property of KL divergence is that it's **non-negative**. The KL divergence is $$0$$ if and only if the two distributions $$P$$ and $$Q$$ are the same in discrete case and equal "almost everywhere" in continuous case. The KL divergence is often regarded as **distance** between the two distributions although it's not a true distance because it's not symmetric: $$D\_{KL}(P\|\|Q) \neq D\_{KL}(Q\|\|P)$$ for some $$P$$ and $$Q$$.

> ## Cross-Entropy

A very frequently appearing quantity in machine learning context is the **cross-entropy**. The cross-entropy is closely related to the KL divergence. The cross-entropy is formulated by,

$$ H(P,Q) = H(P) + D\_{KL}(P\|\|Q) $$

Since

$$H(X) = -\mathbb{E}_{X \sim P}[\log P(x)]$$

$$D_{KL}(P\|\|Q) = \mathbb{E}_{X \sim P}[\log P(x) - \log Q(x)]$$,

The cross-entropy can be written as,

$$ H(P,Q) = -\mathbb{E}\_{X \sim P}\log Q(x) $$

which is similar to the KL divergence but lacking the left term. Therefore, **minimizing** the cross-entropy w.r.t $$Q$$ is equivalent to minimizing the KL divergence.

> ## Cross-Entropy Loss in Deep Learning

One of the most commonly used loss function in deep learning is the **cross-entropy loss**. As we've learned what cross-entropy is, now we can better understand why we use the cross-entropy loss to train out neural network.

$$ H(p,q) = -\sum\_{x \in classes}p(x)\log q(x) $$

where $$p(x)$$ is the true probability and the $$q(x)$$ is the expected probability. The ultimate purpose of training our neural network is to approximate the (unknown) true probability distribution of the data with our neural network with millions of parameters. Therefore, we're actually trying to **minimize** the difference between our neural network's predicted distribution and the true distribution of the given data. As stated above, minimizing this cross-entropy loss w.r.t $$q$$ (our model) is equal to minimizing the **KL divergence** or the **distance** between the true distribution and the predicted distribution which is essentially what we wish to do when training our model.

[Note] It's common to encounter the expressions of $$0\log0$$. By convention in the information theory context, we treat $$\lim_{x \rightarrow 0}x \log x=0$$.

> ## Personal Notes

In deep learning, data is crucial. We collect various data and frequently perform data augmentation to increase generalization performance. I intuitively understood this importance of diversity of data but the basics of information theory gave me a much better understanding. If there're a lot of duplicates or similar data for training, it becomes more **deterministic** so it doesn't give much informative information and therefore the predicted distribution is unlikely to resemble the true distribution since the true distribution in the real-world data is so much more diverse. We collect as diverse data as possible to mimic the real-world diversity.

> ## References

[1] [deeplearningbook.org](https://www.deeplearningbook.org/)  
[2] _A Modern Introduction to Probability and Statistics by Dekking_
