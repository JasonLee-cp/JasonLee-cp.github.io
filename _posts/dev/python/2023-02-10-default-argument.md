---
layout: post
title: "[Python] Default arguments - mutable/immutable"
subtitle: "modern javascript, 생성자 new"
categories: dev
tags: python
comments:
---

In this chapter, I'll go over how the default argument works in Python.

Before getting into that, we need to understand the difference between **mutable** and **immutable**.

## Immutable object

In python, an immutable object is an object that cannot be changed or modified once it has been created. `int`, `string`, and `tuple` are some examples of an immutable object.

## Mutable object

As you might have guessed, a mutable object can be changed and modified. `list` and `dict` are some examples.

## Default argument

You can specify default values for a function's arguments like below,

```py
def func(a=1, b=None):
    ...
```

In this way, you can either not pass an argument for the parameter having the default value or you can still pass a specific value upon a function call.

So, what's the problem? Consider this example.

```py
def func(a, b=[]):
    b.append(a)
    return b


print(func(1))
print(func(2))
print(func(3))
```

What would be the output? You might think it will be `[1]`, `[2]`, `[3]`. However, when you execute it, you'll see the output is

```py
[1]
[1, 2]
[1, 2, 3]
```

This is because the **default value is evaluated ONLY ONCE when the function was first compiled**. In this case, that initial evaluation happened to be the list object which contains nothing. Then, when you actually call the function by `func(1)`, if you didn't provide a specific value, that initially evaluated default value `[]` will be used for `b`. However, as you saw above, list is a **mutable object** which you can modify or change its internal state. This is why the list gets accumulated as you call multiple functions.

To make it clearer, you may think the initially evaluated default value is an object **pointing to the memory address xyz**. Then, the default will **always** be this object. Thus, when you call the first `func1(1)`, the list object stored in memory address xyz will be appended by an int object `1`. The next call `func(2)` will append to the same list object stored in memory address xyz, and so on.

To see a function's defaults, you can check with `func.__defaults__`. For example,

```py
def func_immutable(x, a=0):
     a += 1
     return a

def func_mutable(x, a=[]):
    a.append(x)
    return a

print(func_immutable.__defaults__)
print(func_mutable.__defaults__)
```

```py
(0,)
([],)
```

As you can see, the default values are stored **before** you make the first function call. So it's **wrong** that the default value is evaluated upon the first functionc all.

## How to modify its behavior to make it work normally?

To make this function work like you expected(maybe you expected a weird way), you can change the default argument to `None` and initialize the list object inside the function. This approach works because `None` is an **immutable** object and no matter how many times you call the function, the default value will always be `None`.

```py
def good_func(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b

print(func(1))
print(func(2))
print(func(3))
```

When you execute this, you'll see

```py
[1]
[2]
[3]
```

as you expected.
