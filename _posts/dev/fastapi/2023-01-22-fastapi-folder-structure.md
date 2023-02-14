---
layout: post
title: "FastAPI Directory Structure"
subtitle: "Good practices for FastAPI structure besides the official documentation's"
categories: dev
tags: fastapi
comments:
---

# Introduction

When I work on projects, one of the things I spent time the most is **project code structure**. The structure dramatically impacts the readability, modularization, and redundancy of codes. In this article, I'll go over the recommended folder structure by the official FastAPI documentation and its limitations. Then, I'll introduce a more scalable and evolvable structure.

FastAPI provides the general guideline of structuring files in [FastAPI folder structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/) in the official documentation.

# FastAPI Recommended Structure

```text
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

This structure is <span style="background:#fff88f">categorized by its type</span> (`api, crud, router, schemas, etc`). I first followed this structure but encountered difficulties while working on the project [VIZTA](https://noisrucer.github.io/project/2023/02/08/vizta/).

Suppose the router `/routers/visualization.py`. In VIZTA, the visualization APIs not only include visualization-only logics but also include users, courses, and email. However, if we have only one router handling the visualization, <span style="background:#fff88f">different business logics for different services could get entangled</span>, making it more difficult to scale up. Also, business logics for each service are spread across different routers so it's difficult to clearly locate specific codes as the project gets bigger.

Hence, I needed a more <span style="background:#fff88f">scalable, modularized, and better readable</span> code structure. After googling for a while, I found this wonderful [repository](https://github.com/zhanymkanov/fastapi-best-practices#1-project-structure-consistent--predictable) which suggests a more scalable and organized structure which is inspired by Netflix's [Dispatch](https://github.com/Netflix/dispatch).

# New Structure

A good project structure must be consistent, scalable, and straightforward. Below are the three principles when organizing the project structure, referenced from [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices#1-project-structure-consistent--predictable).

- If looking at the project structure doesn't give you an idea of what the project is about, then the structure might be unclear.
- If you have to open packages to understand what modules are located in them, then your structure is unclear.
- If the frequency and location of the files feels random, then your project structure is bad.
- If looking at the module's location and its name doesn't give you an idea of what's inside it, then your structure is very bad.

The new suggested structure separates files into <span style="background:#fff88f">services</span> rather than types.

```
fastapi-project
├── alembic/
├── src
│ ├── auth
│ │ ├── router.py
│ │ ├── schemas.py # pydantic models
│ │ ├── models.py # db models
│ │ ├── dependencies.py
│ │ ├── config.py # local configs
│ │ ├── constants.py
│ │ ├── enums.py
│ │ ├── exceptions.py
│ │ ├── service.py
│ │ └── utils.py
│ ├── course
│ │ ├── router.py
│ │ ├── schemas.py
│ │ ├── models.py
│ │ ├── dependencies.py
│ │ ├── config.py
│ │ ├── constants.py
│ │ ├── enums.py
│ │ ├── exceptions.py
│ │ ├── service.py
│ │ └── utils.py
│ ├── config.py # global configs
│ ├── models.py # global models
│ ├── exceptions.py # global exceptions
│ ├── pagination.py # global module e.g. pagination
│ ├── database.py # db connection related stuff
│ └── main.py
├── requirements
│ ├── base.txt
│ ├── dev.txt
│ └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
```

## All source codes in `/src`

`/src` is the root directory holding all the source files.

## Each service owns a directory

### 1. Each service such as `/src/auth` and `/src/course`.

### 2. `router.py`: all endpoints for each service reside.

### 3. `schemas.py`: pydantic models

`/src/course/schemas.py`
![d](/assets/img/project/fastapistructure2.png)

### 4. `models.py`: db models

`/src/course/models.py`
![d](/assets/img/project/fastapistructure3.png)

### 5. `dependencies.py`: service-specific dependencies are here. One example could be verifying JWT credentials.

`src/dependencies.py` global dependencies

![d](/assets/img/project/fastapistructure4.png)

### 6. `constants.py`: service specific constants are here. One example could be `JWTSettings` for `auth` service.

`/src/course/constants.py`
![d](/assets/img/project/fastapistructure5.png)

### 7. `enums.py`: service specific enums are here.

`/src/course/enums.py`
![d](/assets/img/project/fastapistructure6.png)

### 8. `exceptions.py`: service specific exceptions are here.

`/src/course/exceptions.py`
![d](/assets/img/project/fastapistructure7.png)

### 9. `service.py`: service specific business logics go here. This will interact with database.

`/src/course/service.py`
![d](/assets/img/project/fastapistructure8.png)

### 10. `utils.py`: non-business logic functions such as hashing password.

`/src/auth/utils.py`

![d](/assets/img/project/fastapistructure9.png)

Also, when importing other packages from a package, <span style="background:#fff88f">explicitly state the module name</span> like

![d](/assets/img/project/fastapistructure1.png)

In this way, adding a new service into the existing project does not destroy the structure of the project so it's more scalable than separating them into types.
