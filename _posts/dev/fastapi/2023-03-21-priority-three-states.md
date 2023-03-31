---
layout: post
title: "Contemplation of designing an API consisting of a query parameter with three states"
subtitle: ""
categories: dev
tags: python
comments:
---

**Project repo**: [Girok](https://github.com/noisrucer/girok)

# Problem Statement

![](/assets/img/temp/Pasted%20image%2020230331010547.png)

One of the features offered by Girok is to query tasks with various filtering options such as category, tag, priority, and so on.

When I was working on APIs for retrieving tasks, I encountered a challenge for designing `priority` query for `GET /tasks` route.

Users, although not a must, can assign a task with a `priority` value within `1 ~ 5` so that they could query tasks more effectively.

There're three situations regarding the priority for `GET /tasks` API call.

1. Tasks with a <span style="background:#fff88f">specific priority</span>
2. Tasks with an <span style="background:#fff88f">unassigned priority</span>
3. <span style="background:#fff88f">All tasks regardless of priority</span>

![](/assets/img/temp/Pasted%20image%2020230331014719.png)

As I designed priority as a query whose value ranges from 1 to 5, it was tricky how to incorporate the above three cases as one query.

# Approach #1 - Using a off-boundary value `0` to express "unassigned priority".

The first approach I took was to expand the range `1 ~ 5` to `0 ~ 5` so that the value `0` would indicate that the user wants to query tasks with "unassigned priority". As a result,

1. priority `1 ~ 5` - indicate a specific priority
2. priority `None` - all tasks regardless of priority
3. priority `0` - unassigned priority

However, this approach bought more complications and difficulties for me write codes because I have to "remember" the rule (priority `0`) when sending actual query to the database. Also, following this approach made it unable to directly pass the priority query value to the service logic which communicates with the database. The reason is that if I pass priority `None` to filter queries from the database, `priority = None` refers to "unassigned category" in the database context. However, in the context of "my rule", `priority = None` indicates "all tasks regardless of priority".

Another drawback is that this approach brings further complications to the API caller.

Frontend developers might not feel very complicated with only one or two APIs containing "hand-made rules" like priority `0` referring to "unassigned priority". However, "<span style="background:#fff88f">what if there're thousands of APIs containing their own specific rules</span>"? Then, it'd be nearly impossible for me as well as the API callers to memorize these rules (certainly unncessary waste of effort).

For the above reasons, I came to a conclusion that this is not really a good approach.

# Solution - using "no priority" flag to indicate tasks with unassigned priority

Instead of having a single query, utilizing a "no priority" flag would reduce the complexity of the problem.

Rather than a single `priority` query having 3 different states, the original `priority` query has two states: `None` or `1 ~ 5`.

If the `no_priority` flag is set to `True`, then query the database with `priority=None` referring to tasks with unassigned priority.

On the other hand, if this flag is set to `False`, then query the database with the given `priority` value if it's not `NULL`.

```python
if no_priority:
        tasks_query = tasks_query.filter(models.Task.priority == None)
    else:
        if priority:
            tasks_query = tasks_query.filter(models.Task.priority == priority)
```

In this way, there's no need to follow pre-defined rules for me as well as the API callers.
