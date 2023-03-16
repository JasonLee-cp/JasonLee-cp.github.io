---

layout: post
title: "Modeling Hierarchical Directory Tree with FastAPI and SQLAlchemy (Visualize with Typer & Rich library)"
subtitle: ""
categories: dev
tags: database
comments:
Code repository: [Github](https://github.com/noisrucer/girok)

---

# Introduction

I've been working on a project recently to build a powerful schedule management app which saves users tremendous amount of time. It will offer a **CLI (Command Line Interface)** as well as **Web app** to quickly perform various schedule management operations.

Below is the CLI calendar view.

![](/assets/img/db/cattree1.png)
As you can see on the left side, one of the features supported is the **infinite category tree**. Users can pre-defined categories such as school work, life, workout that different tasks belong to. Some calendar apps offer the category feature but most of them don't support infinite category tree.

In this article, I'll go through how to model the infinite category tree and how to perform different operations such as <span style="background:#fff88f">show</span>, <span style="background:#fff88f">create</span>, <span style="background:#fff88f">move</span>, and <span style="background:#fff88f">remove</span> categories.

Let's first explore what you can learn after reading this article.

# Show Categories

As you can see from the above, you can recursively create categories. For example, if you type `showtask` command, then it shows you the full category tree.

![](/assets/img/db/cattree2.png)

# Add Categories

You could also add a category by a specifying a full path (`parent path/` + `new category name`).
![](/assets/img/db/cattree3.png)

# Remove Categories

You could also remove a category by specifying a target path. Notice that all subcategories are recursively removed.
![](/assets/img/db/cattree4.png)

# Move Category

Lastly, you can move a category into another category. Notice that all subcategories are also recursively moved.
![](/assets/img/db/cattree5.png)

# Modeling self-referential relationship

Let's first define a category table named `task_category` with SQLAlchemy.

To efficiently model the hierarchical structure, we use a <span style="background:#fff88f">self-referential table</span> which means a table has a foreign key referencing a key of its table itself.

![](/assets/img/db/cattree6.png)

For our case, each category could possibly have the infinite number of children. Hence, this is a one-to-many relationship.

In SQLAlchemy, the representation of this tree structure can be done with `relationship()`.

![](/assets/img/db/cattree7.png)

Here, I named `super_task_category_id` as a foreign key pointing to the parent table.

![](/assets/img/db/cattree8.png)

Then, define `relationship()`. The parameter is the table name (not the actual name but the class). Notice I added `cascade="all,delete"` so that I can remove the whole tree recursively

**[Warning]** In SQLAlchemy, `relationship()`, by default, behaves as the one-to-many relationship whether it's one-to-many or many-to-one.

To build a many-to-one relationship, we need an extra directive `relationship.remote_side`

Both directions can be combined into a bidirectional relationship with `backref()`.

Notice that the entry has `NULL` parent is the **top most category**.

# Visualize tree with Rich library

Now, let's visualize the tree with **Rich** library. Rich offers a powerful tool for building CLI apps.

## Create category

To create a new category, let's accept a full target category path delimited by `/`, with the new category name as the last item. For example, `girok addcat HKU/COMP3230` will create a new category named `COMP3230` under `HKU` category.

To add it under `HKU` category, we need to check two things.

1. There **exists** a category named `HKU`
2. There **does not exist** a category named `COMP3230` under `HKU`

![](/assets/img/db/cattree9.png)

Our create category router accepts a request body named `category`. Here, `category['names']` is a list of category names including the new category name.

![](/assets/img/db/cattree10.png)

![](/assets/img/db/cattree11.png)

![](/assets/img/db/cattree12.png)

To check the first condition, we'll try to obtain the id of the <span style="background:#fff88f">second last category</span> and check if it's possible (If not, then there must be a missing category).

I created a function named `get_last_cat_id` which accepts `cats` which is a list of categories and returns the `id` of the last category.

First initialize the `parent_id = None` since the topmost category has a `NULL` parent. Then, iterate through the list and get the id of each element with `get_category_id_by_name_and_parent_id()` function which returns `None` if there's no match. Hence, if there's no matching category, raise `SubcategoryNotExistException`. If there's a match, then update `parent_id = cat_id`.

In this way, we can check the first condition.

Suppose our target path is `HKU/COMP3230/Assignment`. Then, now we know that the second last item of the category list `COMP3230` is a valid category. However, we have to make sure that there does not already exist a `Assignment` category under `HKU/COMP3230`. This can be easily with `get_category_id_by_name_and_parent_id()` function we used earlier.

![](/assets/img/db/cattree13.png)

We've already obtained the `id` of the `COMP3230` category. Now, extract the last category from the list (which is the new category name). Check if there already exists a category named `Assignment` under the `COMP3230`. If so, raise `CategoryAlreadyExistException`

![](/assets/img/db/cattree14.png)

After successfully passing the two constraints, let's now add a `Assignment` under `HKU/COMP3230`.

![](/assets/img/db/cattree15.png)

![](/assets/img/db/cattree16.png)

All we have to do is create a category whose `super_task_category_id` is equal to the `pid_of_second_last_cat`, constructing a parent-child relationship.

## Remove category

Now, let's also **remove** a category by accepting a full target category path such as `HKU/COMP3230/Assignment`. In this example, we're trying to delete a category named `Assignment` under `HKU/COMP3230`.

![](/assets/img/db/cattree17.png)

It's much simpler than creating a category since we already made athe reusable `get_last_cat_id()` function.

When deleting a category, all we need to check is that there exists a category named `Assignment` under `HKU/COMP3230`. Hence, we pass the category list to `get_last_cat_id()` function to get the id of `COMP3230`. If if throws an exception, then it means there is a missing category along `HKU/COMP3230` path.

After getting the last category id, we can easily delete it.

![](/assets/img/db/cattree18.png)

## Move Category

We also should handle moving a category from one place to another.  
For example,

![](/assets/img/db/cattree19.png)

Suppose we want to move the entire category `HKU` (and its recursive subcategories) into under `Dev/Git` category.

![](/assets/img/db/cattree20.png)

To achive that, we can simply changing the `parent` of `HKU` to `Git`. However, we need to first check a number of constraints.

1. You cannot move a root directory `/`.
2. The source category `HKU` and the target directory `Dev/Git` must exist
3. The target directory `Dev/Git/` must contain the category name `HKU`.

To check the <span style="background:#fff88f">first condition</span>, we can simply check whether the input source category path is an empty list or not.

For the <span style="background:#fff88f">second condition</span>, we can use `get_last_cat_id()` function.

![](/assets/img/db/cattree21.png)

For the last condition, we can use the `get_category_id_by_name_and_parent_id()` function.
![](/assets/img/db/cattree22.png)

![](/assets/img/db/cattree23.png)

# Visualize category tree with Rich

Now, we want to visualize the category tree. I'm going to use `Rich` library which is an amazing tool for building CLI applications.

Let's first look at the server.

![](/assets/img/db/cattree24.png)

Our server will return all the categories as a dictionary like below.

![](/assets/img/db/cattree25.png)

First, let's get all <span style="background:#fff88f">topmost categories</span>.
![](/assets/img/db/cattree26.png)

Then, iterate each category and recursively build a category tree with `build_category_tree()` function.
![](/assets/img/db/cattree27.png)

![](/assets/img/db/cattree28.png)

![](/assets/img/db/cattree29.png)
In `build_category_tree` function, we first get all sub-category ids. Then, iterate each sub-category and recursively attach the subcategory tree.

![](/assets/img/db/cattree30.png)

`build_category_tree` function returns output in the form of the following.

```python
{
  "Category1": {
    "color": "yellow",
    "subcategories": {...}
 },
  "Category2": {
    "color": "yellow",
    "subcategories": {...}
 },
 ...
}
```

Rich offers a **tree** so that you can more easily build a tree structure in terminal.

Below are the basic steps to visualize a tree.

![](/assets/img/db/cattree31.png)

![](/assets/img/db/cattree32.png)

Now, the CLI will receive this response and store into `cats_dict` and pass it to `display_categories` function to nicely visualize tree.

![](/assets/img/db/cattree33.png)

The above is an example of `Typer` library to build CLI apps.

![](/assets/img/db/cattree34.png)

`display_categories` function accepts the `cats_dict` and iterate each key (which is the category name) and call `display_category` function, passing category name `cat`, and the tree object `tree`.

Keep in mind that the `tree.add()` method returns the created sub-tree object.

In `display_category` function, `tree` parameter refers to the <span style="background:#fff88f">parent tree object</span> of the tree object of the current call stack.

Hence, we add the current category to the parent tree object.

![](/assets/img/db/cattree35.png)

Then, we iterate the sub-categories of the current category and recursively build the subtree.

Finally, we print the tree object with `console.print()`

![](/assets/img/db/cattree36.png)

# Conclusion

So far, we've seen how to design a self-referential table to models infinite category tree. Also, we learned how to perform different operations with FastAPI, SQLAlchemy, Typer, and Rich.

In the following posts, I'll explore how to add tasks which are assigned to a specific category like below.
![](/assets/img/db/cattree37.png)

Also, I'll make a post about creating a beautiful CLI app, integrating the category tree we've discussed so far.

![](/assets/img/db/cattree38.png)

Thank you for reading!
