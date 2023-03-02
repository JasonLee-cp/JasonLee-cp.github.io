---
layout: post
title: "How to model composite course pre-requisites in database?"
subtitle: ""
categories: project
tags:
comments:
---

## Introduction

As the competitiveness of our service is highly relevant to the objective and detailed information of a course, we wanted to also show the course **prerequisites** to users. A prerequisite course refers to a course that a student must have taken before taking a specific course. For example, `course A` might require candidates to pass in `course B and course C` in prior.

At first, I thought it would be a pretty simple task. However, my school, probably similar for most other schools, has slighly more complicated prerequisites.

Let's look at the Machine Learning course offered by HKU.

![](/assets/img/project/prereq1.png)

As you can see, this course has some pre-requisites but it's a combination of courses connected with **AND** and **OR**.

## Simple prerequisites

If the prequisites were just a list of courses connected with a single AND or OR, we can just model it as a **multi-valued attribute** by creating another table called `CoursePrerequisite`. Then, this table contains two columns: `course_id` and `prereq_course_id`, both referencing `Course` table and are also primary keys.

## Modeling more complicated prerequisites

However, how to deal with composite prerequisites like below examples?

`Prereq(C) = (A and B) or (C and D)`

`Prereq(C) = (A and B) or (C or D)`

`Prereq(C) = (A or B) and (C and D and E)`

The first example means course C requires students to take "both A and B" or "both C and D" in prior.

Consider each parenthesis as a **set** consisting of a number of courses like `(A and B)` or `(C or D or E)`. And let's assume that each parenthesis consists of courses connected with one of **AND** and **OR**.

**Then, each prerequisite is now a combination of sets rather than courses**.

Suppose our goal is to store the following prerequisite.

> Prerequisite of **COMP3314** is `(COMP2119 or ELEC2542 or FITE2010) and (MATH1853 or MATH2014)`.

We can model the above by creating a few more tables called `PrerequisiteSet`, `PrerequisiteSetCourse`, and `PrerequisiteType`.

![](/assets/img/project/prereq2.png)

**Course** table contains `course_id`.

**PrerequisiteSet** table contains `set_id`, `course_id`, and `is_conjunction`. `set_id` column refers to each set in the prerequisite such as `(COMP2119 or ELEC2542 or FITE2010)` and `(MATH1853 or MATH2014)`. Of course, we need to include `course_id` to make sure which course those sets belong to. Also, `is_conjunction` field refers to whether the courses are connected by conjunctions(AND) or disjunctions(OR).

**PrerequisiteSetCourse** table contains `set_id` and `course_id`. This table further specifies actual courses that belong to a specific set. For example,`COMP2119, ELEC2543, and FITE2000` belong to the same set (set_id=1) as we just saw.

Lastly, **PrerequisiteType** table contains `course_id` and `is_conjunction`. This table defines whether the combination of **sets** is connected through conjunctions or disjunctions. In our example, they're connected by **AND**.

Now, when we want to retrieve prerequisite for all the courses, we can join `PrerequisiteSet` and `PrerequisiteSetCourse` on `course_id` and group by course_id, is_conjunction, and set_id.

## Application in the project

In our project, backend API returns the prerequisite in a **string format** like `(COMP2119 or ELEC2542 or FITE2010) and (MATH1853 or MATH2014)`. Let's look at SQL code to implement it.

```sql
SELECT REPLACE(
	GROUP_CONCAT(temp.chunk SEPARATOR '-'),
	'-',
	IF(PT.is_conjunction=true, ' AND ', ' OR ')
) AS 'prerequisite' FROM (
	SELECT PS.course_id,
		concat(
			'(',
			REPLACE(GROUP_CONCAT(PSC.course_id SEPARATOR '-'), '-', If(PS.is_conjunction=true, ' AND ', ' OR ')),
			')'
		) AS chunk
	FROM prerequisite_set_course PSC JOIN prerequisite_set PS ON PSC.set_id = PS.set_id
	WHERE PS.course_id = 'COMP3314'
	GROUP BY PSC.set_id
) AS temp JOIN prerequisite_type PT ON temp.course_id = PT.course_id
GROUP BY temp.course_id;
```

![](/assets/img/project/prereq3.png)

You can see it returns the correct prerequisite for COMP3314.
