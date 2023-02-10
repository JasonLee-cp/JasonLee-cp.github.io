---
layout: post
title: "[Python] Variables"
subtitle: "modern javascript, 생성자 new"
categories: dev
tags: python
comments:
---

### Variable Name

- alphabet, number

- no reserved-keywords

## Primitive data types

#### Dynamic Typing: declare data type during execution

```python
# int
x1 = 1
# float
x2 = 3.3
# string
x3 = 'abc'
# bool
x4 = True

print(type(x1))
print(type(x2))
print(type(x3))
print(type(x4))
```

<pre>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
</pre>

## Data Type Conversion

```python
a = 10
print(type(a))

a = float(a)
print(type(a))

a = str(a)
print(type(a))

s = "9.1"
s = float(s)
print(type(s))
```

<pre>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'float'>
</pre>

## List

```python
a = ["1", 1, 2]
b = [2.0, "hello", 4]
```

```python
a.append(b)
a
```

<pre>
['1', 1, 2, [2.0, 'hello', 4]]
</pre>

```python
a.extend(b)
a
```

<pre>
['1', 1, 2, [2.0, 'hello', 4], 2.0, 'hello', 4]
</pre>

```python
a = [1, 2]
b = [2, 3]
a + b
```

<pre>
[1, 2, 2, 3]
</pre>

```python
a * 2
```

<pre>
[1, 2, 1, 2]
</pre>

```python
2 in a
```

<pre>
True
</pre>

```python
print(a)
a[0] = 3
print(a)
```

<pre>
[1, 2]
[3, 2]
</pre>

#### Slicing

```python
a = [1,2,3,4,5,6]
```

```python
print(a[0:3])
print(a[-4:])
```

<pre>
[1, 2, 3]
[3, 4, 5, 6]
</pre>

## List memory space

```python
a = [1,2,3]
b = [3,2,1]

b = a # b is pointing at a
print(a)
print(b)

a[0] = 99
print(a)
print(b)
```

<pre>
[1, 2, 3]
[1, 2, 3]
[99, 2, 3]
[99, 2, 3]
</pre>

### Clone

```python
a = [3, 2, 1]
b = [1, 2, 3]

# clone
b = a[:]
a[0] = 100
print(a)
print(b)
```

<pre>
[100, 2, 1]
[3, 2, 1]
</pre>

### [:] doesn't work for >= 2-D list! Use .copy() instead

```python
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

b = a[:]
a[0][0] = 100
print(a)
print(b)

import copy
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
b = copy.deepcopy(a)
a[0][0] = 100
print(a)
print(b)
```

<pre>
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
[[1, 2], [3, 4]]
</pre>

### unpacking

```python
a = [1,2,3]
e1, e2, e3 = a
print(e1, e2, e3)
```

<pre>
1 2 3
</pre>

```python

```
