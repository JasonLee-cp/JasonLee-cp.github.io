---
layout: post
title: "Better manage your projects with issue, commit, and PR template"
subtitle: ""
categories: dev
tags: git
comments:
---

Have you struggled before to manage projects using Git, collaborating with team members? Then, you're in the right place!

In this article, we'll go through how to better manage projects using **issue template**, **commit template**, and **pull request** template which will give you a more powerful control of your project management.

## Configure .github directory

![](issue_template1.png)

In `.github` folder in your root project directory, you can find several items.

In this article, we'll see the below three items.

- `/ISSUE_TEMPLATE`: Template for creating issues into distinct categories
- `.gitmessage.txt`: Commit template
- `pull_request_template.md`: PR template

# Issue template

One good way to manage projects is to use **Github issues**.

With issues, you can categorize tasks into distinct categories such as <span style="background:#fff88f">new feature request</span>, <span style="background:#fff88f">bug report</span>, <span style="background:#fff88f">code refactoring</span>, and more to better manage your software development cycle.

![](issue_template2.png)

The above is the issue template that I use for my projects. When initiating a new "**development action**" like creating a new feature or refactoring codes, I prefer to create an **issue** which could summarize the potential action. Then, I <span style="background:#fff88f">link all commits to the related issue</span> so that I can more clearly see the actions(or commits) I've performed to achieve a specific issue.

![](issue_template3.png)

The above example shows the commits I've made for a specific task (development of a new feature). As we will see soon, we can link up each commit to a specific issue when we commit changes. Then, the commits are automatically linked up to that issue on Github.

Now let's create the issue template!

![](issue_template4.png)

Under the `/ISSUE_TEMPALTE` directory, create markdown files laying out the template for each issue category.

I use the above categories when creating an issue. Let's look at the simple template for `feature-request.md`.

![](issue_template5.png)

After creating all issue templates, go back to the repository and click the **Issues** on the top.

![](issue_template6.png)

You can see all the issues created by team members. To create an issue, click the **New issue** button on the top-right corner.

![](issue_template7.png)

You can see the issue templates you defined under `.github/ISSUE_TEMPLATE` folder. Now, let's click on feature request template.

![](issue_template8.png)

The registered markdown file is shown so that you can have a more clear structure to submit your issues.

## Commit template & Link a commit to an issue

Some people tend to write commit messages with `git commit -m "Commit description"`. However, you can write a more detailed commit description plus link that commit to a specific issue.

After linking your local repository to the remote repository, you can see that `.github` directory we defined previously is present.

![](issue_template9.png)

To configure the **commit template**, enter the below command.

![](issue_template10.png)

This will configure the commit template with the `.gitmessage.txt` which is under `.github/` directory.

Now, instead of committing with `-m` option, enter

```shell
git commit
```

Then, it will redirect you to the commit template.

![](issue_template11.png)

In this way, you can write a more detailed and structured commit message so that other members will better comprehend what's going on in this commit.

One useful option is to provide the <span style="background:#fff88f">issue number</span> so that the commit is automatically linked to the issue.

Check which issue number your commit belongs to from github repository and enter `issue #{issue_number}`, with `#{issue_number}` replaced by the issue number.

Or more conveniently, vscode provides autocompletion.

![](issue_template12.png)

After completing your commit message, save it and just close the file, then push it to the remote repository.

As the above commit is related to `issue 11`, let's go to the issue and check the linked commit.

![](issue_template13.png)

Click the `issue #11`, then you'll see the commit is now linked up to the issue.

![](issue_template14.png)

If you click on the `...` button, you can check the commit message you provided.

![](issue_template15.png)

## PR template

![](issue_template16.png)
Similarly, you can set the <span style="background:#fff88f">pull request template</span> by providing a markdown file under `.github` directory.

Then, when you open a pull request, you can see the configured PR template.

![](issue_template17.png)

## Conclusion

So far, we've gone through how to integrate more powerful git features to our projects: <span style="background:#fff88f">issue template</span>, <span style="background:#fff88f">commit template</span>, and <span style="background:#fff88f">PR template</span>. In this way, we can better manage our projects especially working with other team members.
