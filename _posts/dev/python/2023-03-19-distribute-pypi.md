---
layout: post
title: "Distribute your own PyPI library using Typer"
subtitle: ""
categories: dev
tags: python
comments:
---

## 1. Introduction

`Typer` is an amazing library that helps you build an amazing CLI app with python.

In the development process, you usually test your python command by executing the file directly `python -m my_command.py -p 5`. However, how do you actually **distribute it to PyPI repository so that other people can download your library and use it with only the package name?**

In this article, we'll create a simple CLI app called **goat_calc** which has two commands named `calc` and `hello`.

`calc` takes two arguments. If the user provides `--add` option, print the sum. If the user provides `--sub` option, then print the subtraction.

`hello` simply prints "hello".

# 2. Install Poetry

We'll be using [poetry](https://python-poetry.org/docs/#installing-with-pipx) to distribute our package to `PyPI`. We have a couple of options to install poetry.

In this post, we'll use `pipx` to install it. For other installation options, please visit [install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

First, install `pipx`.

```bash
pip install pipx
```

Then, install poetry.

```bash
pipx install poetry
```

# 3. Create a new project

Go to any directory like `~/Desktop` and initiate our first project by

```bash
poetry new goat_calc
```

![](/assets/img/temp/Pasted%20image%2020230329211104.png)

Then, you'll see that the folder named `goat_calc/` is created. Under `goat_calc/` directory, there's another folder named `goat_calc/` also. The outer `goat_calc/` directory is our project root folder and you can actually change its name to your preference.

Let's now go to the outer `goat_calc/` folder and open up vscode.

```bash
cd goat_calc
code .
```

# 4. Install packages

Let's install `typer` by

```bash
poetry add "typer[all]"
```

![](/assets/img/temp/Pasted%20image%2020230329222123.png)

Then, activate the poetry virtual environment by

```bash
poetry shell
```

![](/assets/img/temp/Pasted%20image%2020230329222135.png)

Then, your `pyproject.toml` will look as follows

![](/assets/img/temp/Pasted%20image%2020230329222226.png)

In case you already have `requirements.txt` ready, I wrote a script for you to generate poetry-compatible dependencies.

Create a python file and paste the below code and execute it. Then, `new_requirements.txt` will be generated. Copy them and paste under `[tool.poetry.dependencies]` in `pyproject.toml` file.

```python
file_path = "requirements.txt"
poetry_requirements_path = "new_requirements.txt"

new_requirements = ''
with open(file_path, 'r') as f:
    while True:
        line = f.readline()[:-1]
        if not line:
            break
        name, version = line.split('==')
        new_line = name + f"=\"{version}\""
        with open(poetry_requirements_path, "a") as ft:
            ft.write(new_line + "\n")

```

# 5. Build a Typer app

Create `main.py` under `goat_calc/` directory.

![](/assets/img/temp/Pasted%20image%2020230329223357.png)

Let's make a simple Typer app with two commands: `calc` and `hello`

`/goat_calc/main.py`

```python
import typer

app = typer.Typer()

@app.command()
def calc(
    x: int = typer.Argument(..., help="first number"),
    y: int = typer.Argument(..., help="second number"),
    is_add: bool = typer.Option(..., "--is-add", help="Set this flag to add. Otherwise, subtract.")
):
    print(x + y if is_add else x - y)

@app.command()
def hello():
    print("hello")

if __name__ == "__main__":
	app()
```

Let's now try if it works.

To see all the commands, enter `python3 goat_calc/main.py --help`

![](/assets/img/temp/Pasted%20image%2020230329223611.png)

Let's execute `calc` command with `--add` option,

```bash
python3 goat_calc/main.py calc 2 3 --add
```

![](/assets/img/temp/Pasted%20image%2020230329224017.png)

Now with `--sub` option.

```bash
python3 goat_calc/main.py calc 2 3 --sub
```

![](/assets/img/temp/Pasted%20image%2020230329224055.png)

`hello` command

![](/assets/img/temp/Pasted%20image%2020230329224114.png)

It seems work pretty well!

# 6. README.md

It's better to provide the documentation of features of the library to users.

![](/assets/img/temp/Pasted%20image%2020230329224310.png)

# 7. Fill out your package info

By default, the version is set to `0.1.0`.

Write a brief description summarizing the current release.

![](/assets/img/temp/Pasted%20image%2020230329224402.png)

Now, we don't want to make users to execute our package typing `python3 main.py calc 2 3 --add`. Let's add a <span style="background:#fff88f">script</span> that would define the command to run our package in `pyproject.toml` file.

![](/assets/img/temp/Pasted%20image%2020230329224918.png)

The `goatcalc` on the left-hand side is actually the command users type to run our package like `git`. The right-hand side defines the path to our `app` which we defined earlier in `main.py`. However, we need to remove `__name__ == "__main__"` in `main.py` since the script will call `app()` instead for us.

```python
import typer

app = typer.Typer()

@app.command()
def calc(
    x: int = typer.Argument(..., help="first number"),
    y: int = typer.Argument(..., help="second number"),
    is_add: bool = typer.Option(..., "--is-add", help="Set this flag to add. Otherwise, subtract.")
):
    print(x + y if is_add else x - y)

@app.command()
def hello():
    print("hello")

# REMOVED __name__ == "__main__"

```

# 8. Install our package to test it locally

Let's install our package to run it locally by

```bash
poetry install
```

![](/assets/img/temp/Pasted%20image%2020230329225254.png)

Now, let's test if our package works fine. You can now use `goatcalc` command without providing python interpreter.

![](/assets/img/temp/Pasted%20image%2020230329225354.png)

It seems working well!

# 9. Distribute our package to PyPI

It's time to distribute our package to PyPI so that other people can download it!

Let's first create a wheel package by

```bash
poetry build
```

Then you'll see the following `dist/` folder created in the project directory.
![](/assets/img/temp/Pasted%20image%2020230329225517.png)

The next step is to go to [PyPI](https://pypi.org/) website and create an account. After you log in, go to [Register API Token](https://pypi.org/manage/account/token/) to register a new API token.

For the scope field, select `Entire account (all projects)`. Later you can change it to be restricted to specific packages.

After creating an API token, go back to the terminal and enter

```bash
poetry config pypi-token.pypi <your APi token>
```

Now, you're ready to publish your package!

```bash
poetry publish --build
```

![](/assets/img/temp/Pasted%20image%2020230329225938.png)

Yay! You have successfully published your pakcage to PyPI. Let's go to [PyPI](https://pypi.org/) to check our package.

![](/assets/img/temp/Pasted%20image%2020230329230047.png)

Search for `goat-calc` and you see our package has been successfully published.

![](/assets/img/temp/Pasted%20image%2020230329230113.png)

Congratulations! Now you have your own amazing package.

# 10. Test our package with pip

Finally, let's go back to our terminal and install our package by

```bash
pip install goat-calc
```

![](/assets/img/temp/Pasted%20image%2020230329230326.png)

After installing some dependencies you'll see that our package with version `0.1.0` has been installed!

Let's test our commands.

![](/assets/img/temp/Pasted%20image%2020230329230350.png)

Yay! It works great!

# 11. Update our package

You'll obviously want to update our packages with new features.

Let's modify our `main.py`

```python
import typer

app = typer.Typer()

@app.command()
def calc(
    x: int = typer.Argument(..., help="first number"),
    y: int = typer.Argument(..., help="second number"),
    is_add: bool = typer.Option(..., "--add/--sub", help="Set this flag to add. Otherwise, subtract.")
):
    print(x + y if is_add else x - y)
    print("Updated") # THIS IS UPDATED

@app.command()
def hello():
    print("hello")
```

Also, modify the next release version and description in `pyproject.toml`.

![](/assets/img/temp/Pasted%20image%2020230329230650.png)

Finally, modify `goat_calc/__init__.py` file as below

![](/assets/img/temp/Pasted%20image%2020230329230745.png)

Let's publish our next release by

```bash
poetry publish --build
```

![](/assets/img/temp/Pasted%20image%2020230329230912.png)

Let's upgrade our package by

```bash
pip install goat-calc --upgrade
```

![](/assets/img/temp/Pasted%20image%2020230329231010.png)

Let's test it out!

![](/assets/img/temp/Pasted%20image%2020230329231026.png)

You can see our change has been successfully updated.
