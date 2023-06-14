---
layout: post
title: "Grouping of Python Sequences"
subtitle: ""
categories: dev
tags: python
comments:
---

1. Container vs Flat
2. Every Python object has a header with metadata
3. Mutable vs Immutable


The Python stand library offers different sequence types implemented in C.

## Container vs Flat
![](/assets/img/python/seq1.png)
Sequence can be categorized into two types depending on the type of element it holds.

<span style="background:#fff88f">Container sequences</span> hold items of different types. It's important to note that a container sequence hold references to the object it contains. `list`, `tuple`, `collections.deque` are the examples of container sequences.

On the other hand, a <span style="background:#fff88f">flat sequence</span> stores the value of its contents in its own memory space not as Python objects. Hence, flat sequences take up much less memory space. `str`, `bytes`, and `array.array` are some examples of flat sequence. 

## Every Python object has a header with metadata
Every Python object in memory has a header with metadata.

For example, a `float` has a value field and two metadata fields.

* `ob_refcnt`: obj's reference count
* `ob_type`: a pointer to the obj's type
* `ob_fval`: a C double holding the float value

Each of the above fields takes `8 bytes` and this is why a tuple of floats takes up more memory space than an array of floats. A tuple of 5 float objects has a tuple object itself plus the five float objects while an array of 5 floats has only a single array object and raw float values.

## Mutable vs Immutable
Mutable sequences are the ones whose state can be changed after initialization. Examples of mutable sequences include `list`, `bytearray`, `array.array`, `collections.deque`.

Immutable sequences' state cannot be changed once they have been initialized. Some examples are `tuple`, `str`, `bytes`.

![](/assets/img/python/seq2.png)
(arrows pointing from subclass to superclass)

Mutable sequences inherit all methods from immutable sequences with additional methods.

The built-in "concrete" sequence types do not actually inherit(subclass) the `Sequence` and `MutableSequence` abstract base classes (ABCs) but they're virtual subclasses registered with those ABCs.






