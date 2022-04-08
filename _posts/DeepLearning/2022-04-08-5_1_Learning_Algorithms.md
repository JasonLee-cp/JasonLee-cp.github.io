---
layout: single
title: "[DL] What is Machine Learning?"
categories: ["deeplearning"]
tag: [deeplearning]

toc: true
toc_label: "Table of Contents"
toc_icon: "align-justify" # corresponding Font Awesome icon name (without fa prefix)
toc_sticky: true
---

> # Learning Algorithms

A machine learning algorithm is able to **learn** from the data. Here, what does "learning" mean? Mitchell (1997) provided a simple definition:

> A computer program is said to learn from **experience** $E$ with respect to some class of **tasks** $T$ and **performance measure** $P$, if its performance at tasks in $T$, as measured by $P$, improves with **experiences** $E$.

> # The Task, T

The process of learning itself is not a task. Learning is **attaining the ability** to perform the task. For example, if we want a build a model that classifies between dog and cat, classification is the task.

Machine learning tasks are usually described in terms of how the machine learning system process an **example** which is a collection of **features**. We typically represent an example in a vector form $x \in \mathbb{R}^n$ where each entry $x_i$ is another feature. For example, the features of an image are typically the pixel values.

## Classification

For the classification task, our model is asked to provide which of $k$ categories some input belongs to. In other words, the model is asked to produce a mapping function $f: \mathbb{R}^n \rightarrow \{1,...,k\}$ so that when $y=f(x)$, the model maps the input vector $x$ to the scalar ouput $y$.

## Classification with missing inputs

Classification task becomes more challenging when some of the inputs are missing. In this scenario, instead of providing a single classification function, the learning algorithm must learn a **set** of functions. For example, with $n$ input variables, we can now obtain all $2^n$ different classification functions needed for each possible set of missing inputs.

## Regression

A regression task is asked to predict a **numerical value**. The learning algorithm is learned for a function $f: \mathbb{R}^m \rightarrow \mathbb{R}$. This task is similar to classification except the output format. An example of regression task is to predict housing price given some features such as location, house size, etc.

## Transcription

For transcription task, the algorithm is asked to observe a relatively **unstructured representation** of some kind of data and transcribe into **discrete textual form**. For example, in optical character recognition, the program is given a photograph containing an image of text and is asked to return this text in the form of a sequence of characters.

## Machine Translation

This task is translating a sequence of symbols in a language and translating into another language

## Structured output

Structured output tasks involve cases where the output is a vector (or other data structure containing multiple values) with important relationships between the different elements. One example is mapping a natural language sentence into a tree that describes its grammatical structure.

> # The Performance Measure, P

We must have some sort of quantitative evaluation measurement of a learning algorith. There is not only one measure but might be different for tasks $T$.

For classification tasks, one popular metric is **accuracy** which tells how many examples the model predicted correctly out of all examples. The equivalent measure is **error rate** which is the proportion of examples for which the model produces an incorrect output.

For most of the times, we mostly care about a model's performance on **unseen** data since this determines how well it will work when deployed in the **real world**. Therefore, we separate dataset into non-overlapping train/test set so that we can train our model on the train set and test our model on the test set for which the model has never been trained for.

> # The Experience, E

Machine learning algorithms can be categorized as **supervised** or **unsupervised** by what kind of experience they're allowed to have during the learning process.

In many cases, machine learning algorithms are allowed to experience an entire **dataset** which consists of many examples, also known as **data points**.

> # Linear Regression

The goal of linear regression is to take a vector $x \in \mathbb{R}^n$ as input and predict the scalar value $y \in \mathbb{R}$ as its output which is a linear function of the input. To formalize this, we can define $\hat{y}$ as the value the model predicts and $y$ is the ground-truth value.

\[[ \hat{y} = w^{\top}x \]]

where $w \in \mathbb{R}^n$ is a vector of **parameters**.

The parameters are values that control the behavior of the system. We can also think of $w$ as a set of weights that determine how each feature affects the prediction.

For linear regression, the definition of our task $T$ is to predict $y$ from $x$ by outputting $\hat{y}=w^{\top}x$.

Now one popular performance measure $P$ of linear regression is the **Mean Squared Error (MSE)** of the model on the test set. If $\hat{y}$ gives the predictions of the models, then MSE is given by

\[[ MSE = \frac{1}{m} \sum_i (\hat{y} - y)_i^2 \]]

or

\[[ MSE = \frac{1}{m} \lvert \lvert \hat{y} - y \rvert \rvert_2^2 \]]

Intuitively, we can see that the error becomes $0$ when $\hat{y}=y$. In other words, the error increases whenever the **Euclidean distance** between the predictions and the targets increases.

Now we have the task $T$ and the performance measure $P$. Then, we need to design an algorithm that will improve the weights $w$ in a way that reduces MSE when the algorithm experiences a training set $(X, y)$.

Some of the ways of achieving this are **gradient descent** and **normal equation**.

- **Gradient Descent**: [see this post for details](https://jasonlee-cp.github.io/deeplearning/4_2_gradient_descent/)
- **Normal equation**: This is a one-shot way of finding the optimal solution by just solving the equation:

\[[ \frac{1}{m} \nabla_w \lvert \lvert Xw-y \rvert \rvert = 0 \]]

\[[ \nabla_w (Xw-y)^{\top}(Xw-y)=0 \]]

\[[ \nabla_w ((Xw)^{\top}-y^{\top})(Xw-y)=0 \]]

\[[ \nabla_w (Xw)^{\top}(Xw)-y^{\top}(Xw)-y(Xw)^{\top}+y^{\top}y=0 \]]

\[[ \nabla_w w^{\top}X^{\top}Xw - y(Xw)^{\top}-y(Xw)^{\top}+y^{\top}y=0 \]]

\[[ \nabla_w w^{\top}X^{\top}Xw -2y(Xw)^{\top} + y^{\top}y=0 \]]

\[[ 2X^{\top}Xw-2X^{\top}y=0 \]]

\[[ X^{\top}Xw-X^{\top}y=0 \]]

\[[ w = (X^{\top}X)^{-1}X^{\top}y \]]

Also, it's common to include an **intercept term** $b$ also known as **bias** so that the model now becomes

\[[ \hat{y}=w^{\top}x+b \]]

So, the mapping from parameters to predictions is still linear but the mapping from features to predictions is now an **affine function**.
