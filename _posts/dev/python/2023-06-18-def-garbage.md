---
layout: post
title: "del keyword and Garbage Collection"
subtitle: ""
categories: dev
tags: python
comments:
---

1. Variables are not boxes, they are labels
2. `def` keyword and garbage collector
3. `weakref.finalize`

---
In this article, we'll go over what `del` keyword does under the hood and how the garbage collector works in Python.

# Variables are not boxes, they are labels
It's important to note that variables in Python are "labels" with names attached to objects. It would be improper to say that variables are "boxes" containing objects. Let's look at the below example.

```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)
>> [1, 2, 3, 4]
```

We created a list `[1, 2, 3]` and "bind" the variable `a` to it. Then, we bind the variable `b` to the same value that `a` is referencing. After we append an element to the list referenced by `a`, we get the modified list when we print the value referenced by `b`.

This behavior wouldn't make sense if we interpret the variables as boxes. Variables in Python are more like "labels" attached to objects.

## `del` keyword and Garbage Collection

In Python, objects are never explicitly destroyed. Instead, when they become "unreachable", they maybe garbage-collected.

In CPython, the Python interpreter tracks `refcount` referring to the how many times an object is referenced by. As I'll talk about later posts, this is related to the infamous GIL(Global Interpreter Lock). When the `refcount` of an object becomes 0, the object is garbage-collected by the garbage collector and frees up its memory.

An important thing to note about `del` keyword is that <span style="background:#fff88f">it deletes references, not objects</span>. In other words, `del my_obj` statement does not always delete the object out of memory, but it de-references the variable named `my_obj` to the object that it was pointing at. If `my_obj` happened to be the last reference, then the Python's garbage collector would delete the object out of memory.

Also, rebinding a variable also decreases the `refcount`, may leading to the destruction of an object.

```python
a = [1, 2]
b = a
del a
print(b) # out: [1, 2]
b = [3] # Object discarded by the garbage collector
```

In the above example, the list object `[1, 2]` was referenced by two variables `a` and `b`. Then, the reference by `a` is not deleted and `b` rebinds itself to another list object. Consequently, the `refcount` of the original list object reaches `0`, causing the destruction of the object.

## `weakref.finalize`

To demonstrate the destruction of an object, we can use `weakref.finalize` as a callback function to be called when an object is destroyed.

```python
import weakref

def bye():
    print("Goodbye..")

a = {1, 2, 3}
b = a

ender = weakref.finalize(a, bye)
print(ender.alive) # out: True

del a # refcount = 1
b = "hello world!" # out: Goodbye...

print(ender.alive) # out: False
```

We can see that when we rebind the variable `b` to another object, the `refcount` of the original set hits 0, triggering the callback function.