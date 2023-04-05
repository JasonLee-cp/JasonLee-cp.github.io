---
layout: post
title: "Implement mutually exclusive command arguments in Typer using Closure"
subtitle: ""
categories: dev
tags: python
comments:
---

1. Introduction
2. Scenario
3. Closure
4. Implement mutually exclusive options

---

# 1. Introduction

When I was developing [Girok](https://github.com/noisrucer/girok), I ran into a challenging task to implement <span style="background:#fff88f">mutually exclusive options</span>.

One of the commands offered was the `addtask` command but with a multitude of different deadline options. For example, users could assign a deadline for a task as `after 7 days`, `next monday`, `2023/5/22`, and so on.

I provided different options such as

1. `--tdy` - today
2. `--tmr` - tomorrow
3. `-d <specific date>` - specific day in `yyyy/mm/dd` format
4. `-a <# days>` - after `n` days from today

![](/assets/img/temp/Pasted%20image%2020230330164751.png)

However, users must provide <span style="background:#fff88f">only one deadline option</span> as it doesn't make sense to have multiple deadlines for a single task.

Typer provides `callback` parameter to be passed in `typer.Option()` so that the provided option value will be passed onto the callback function before jumping into the function body.

It was quite challenging to implement mutual exclusivity to enforce users to provide only one of the deadline options.

I came to solve the problem using <span style="background:#fff88f">closure</span>.

# 2. Scenario

Let's simplify the task and create a simple file.

`main.py`

```python
import typer
from datetime import datetime

app = typer.Typer()

@app.command("greeting")
def greeting(
    name: str = typer.Argument(..., help="Your name"),
    age: int = typer.Option(None, "--age", help="Your age in integer"),
    birthday: str = typer.Option(None, "--birthday", help="Your birthday in yyyy/mm/dd format")
):
    print('hello')
    # We want ONLY ONE of "age" and "birthday" as they're mutually exclusive


@app.command("farewell")
def greeting():
    print("bye")


if __name__ == '__main__':
    app()
```

In this scenario, user would provide his/her `name` and also only one of `age` and `birthday` as we can infer the age from a birthday, we don't need to accept both options.

Our goal is to print the name and the age like "Hello Jason, you're 20 years old!".

# 3. Closure

Before getting into the topic, we need to understand what 'closure' is. Python closure is bascially a nested function that "remembers" the variables of its outer function even when the outer function exits.

Let's a take a look at the code snippet below.

```python
def outer():
    name = "Jason"
    def inner():
        print(f"What's up {name}!")

    return inner

outer_func = outer()
outer_func()
```

```bash
>> What's up Jason!
```

`outer` function has a local variable `name`, a nested function called `inner`. `outer` function, then returns the **object of the inner function**.

In our original knowledge, when we call `outer()` and assign the return value to `outer_func`, the `outer` function must be removed from the call stack as well as its local variables.

However, if we call `outer_func` (`inner` function obj) in the last line, it prints `What's up Jason!`.

# 4. Implement mutually exclusive options

Let's define `mutually_exclusive_age_group` function (outer func) which has a local variable `group` and a nested function `callback` which is to be passed to our option parameter.

```python
def mutually_exclusive_age_group(group_size=1): # maximum number of a group
    group = set() # closure
    def callback(ctx: typer.Context, param: typer.CallbackParam, value: str):
        if value is not None: # option value is provided
            if len(group) + 1 > group_size: # If tge
                raise typer.BadParameter(f"You cannot have {param.name} and {next(iter(group))} at the same time!")
            else:
                group.add(param.name) # Add a member
        return value
    return callback

mutually_exclusive_age_callback = mutually_exclusive_age_group()


@app.command("greeting")
def greeting(
    name: str = typer.Argument(..., help="Your name"),
    age: int = typer.Option(None, "--age", help="Your age in integer", callback=mutually_exclusive_age_callback),
    birthday: str = typer.Option(None, "--birthday", help="Your birthday in yyyy/mm/dd format", callback=mutually_exclusive_age_callback)
):
    print('hello')
```

`mutually_exclusive_age_group` function takes one parameter `group_size` which refers to the maximum number of "members" in a group. In our case, we must have only a single member in our group: one of `age` and `birthday`.

As we just talked about closure, the local variable `group` is a set which will be "remembered" even after we call the outer function.

The inner function `callback` is actually what we will pass into the option parameter in `greeting()`.

So what's going on here?

Notice that `param.name` will give us the name of the entered option like `age` and `birthday`. `value` will give you the actual value you passed for that option.

```python
 if len(group) + 1 > group_size: # If tge
                raise typer.BadParameter(f"You cannot have {param.name} and {next(iter(group))} at the same time!")
            else:
                group.add(param.name) # Add a member
```

In the above code, the condition `len(group) + 1 > group_size` indicates that if you add one more member into the group, then you will overflow the maximum number of members in a group. Hence, we raise the exception.

If the condition is not met, then we're safe to add a new member to a group. Recall that since we're using a <span style="background:#fff88f">closure</span>, the inner function `callback` still "remembers" the local variable `group` of the outer function.

When this callback function is called once more after the group is already filled, then `callback` will remember the previous state of the variable `group` and throw an error.

[Info] Notice that we didn't use `nonlocal group` in the inner function. Python restricts us to perform write operations to the namespace of outer-function but we can only "read" them. In this case, `group` is a set date type which is <span style="background:#fff88f">mutable</span>. That's why we can still mutate this object.

Let's call this function and assign to `mutually_exclusive_age_callback` variable. Then, we pass it to the option parameter in `greeting` function.

Now, when we provide both `age` and `birthday` options, we'll see the following error.

![](/assets/img/temp/Pasted%20image%2020230330175333.png)
