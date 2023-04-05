---
layout: post
title: "Inject environment variables into a docker container with AWS Systems Manager Parameter Store"
subtitle: ""
categories: dev
tags: deployment
comments:
---

1. Introduction
2. Modify source code
3. Approach #1 - env var as arguments
4. Approach #2 - env var as a file
5. Approach #3 - AWS SSM Parameter Store
6. IAM access key
7. New task definition
8. Update service

---

# 1. Introduction

In the previous articles, [we created a docker image of a simple FastAPI project](https://noisrucer.github.io/dev/2023/03/25/dockerize/) and [deployed it to AWS ECS Fargate](https://noisrucer.github.io/dev/2023/03/28/deploy-ecs/).

Most of the times, we deal with environment variables such as database connection info or some other 3rd-party API secret keys.
In this article, we'll talk about how we can manage environment variables in AWS server.

# 2. Modify source code

Previously, we made a super simple server with only one endpoint that returns "Welcome back to root!".

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome_root():
    return "Welcome back to root!"
```

Now, let's modify the source code to include an environment variable called `SECRET_NICKNAME`

```python
from fastapi import FastAPI
import os

app = FastAPI()

@app.get('/')
def welcome_root():
    secret_nickname = os.environ.get("SECRET_NICKNAME")
    return f"Welcome back to root. {secret_nickname}!"
```

# 3. Approach #1 - Inject env variables as arguments when running a container image

The first approach is to inject environment variables when we run the container image.

Let's build the container image by running the following command.

![](/assets/img/temp/Pasted%20image%2020230331131018.png)

Now run the following command to pass `SECRET_NICKNAME` env variable.

```bash
docker run -e SECRET_NICKNAME=Jason -p 8000:8000 demo-env
```

![](/assets/img/temp/Pasted%20image%2020230331131910.png)

If you check the `localhost:8000`, you'll see that we successfully passed the env variable.

![](/assets/img/temp/Pasted%20image%2020230331131945.png)

# 4. Approach #2 - Pass the environment variable file when running a container image

Alternatively, we can pass the environment variable file path when running an image.

First create `.env` file under the project root directory.

![](/assets/img/temp/Pasted%20image%2020230331132242.png)

Then, run the container image by passing `--enf-file` option and the target path `.env`.

```bash
docker run --env-file .env -p 8000:8000 demo-env
```

You can see that the env variable has been successfully passed.
![](/assets/img/temp/Pasted%20image%2020230331132343.png)

# 5. Approach #3 - Using AWS Systems Manager Parameter Store

AWS offers a good way to store and manage our environment variables in the Amazon system.

Let's navigate to the AWS console and search for <span style="background:#fff88f">Systems Manager</span>.

![](/assets/img/temp/Pasted%20image%2020230331132516.png)

Click the "<span style="background:#fff88f">Parameter Store</span>" in the left panel.

![](/assets/img/temp/Pasted%20image%2020230331132601.png)

You can register your own environment variables here. To create one, click "<span style="background:#fff88f">Create parameter</span>" on the top right corner.

Enter the environment variable name `SECRET_NICKNAME` and select **SecureString** if you want to store it as a secret information.

![](/assets/img/temp/Pasted%20image%2020230331132708.png)

Then, enter the value in the box and create.

![](/assets/img/temp/Pasted%20image%2020230331132804.png)

![](/assets/img/temp/Pasted%20image%2020230331132837.png)

Now you can see that our env variable is created in the parameter store.

# 6. Grant access to Parameter Store in IAM

To use the AWS Systems Manager Parameter Store in your ECS service, you must have the ECS task execution role and reference it in your task definition.

Notice that in the task definition we created in the [previous article](https://noisrucer.github.io/dev/2023/03/28/deploy-ecs/), you can find that the "<span style="background:#fff88f">Task execution role</span>" is referencing `ecsTaskExecutionRole`.

![](/assets/img/temp/Pasted%20image%2020230331133827.png)

Now let's navigate to IAM service from the console and click "<span style="background:#fff88f">Roles</span>" in the left panel.

![](/assets/img/temp/Pasted%20image%2020230331133909.png)

Click the `ecsTaskExecutionRole`.

Then select "<span style="background:#fff88f">Add permissions</span>" in Permissions policies panel and select "<span style="background:#fff88f">Create inline policy</span>".

Select `JSON` and paste the following.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameters",
        "secretsmanager:GetSecretValue",
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:ssm:<your region>:<your aws account id>:parameter/<parameter name>"
      ]
    }
  ]
}
```

Modify the following three.

1. `<your region>`
2. `<your aws account id>`
3. `<parameter name>` - this would be `SECRET_NICKNAME` that we have defined in the Parameter Store.

After you create a permission policy, you can see that it's not attached to `ecsTaskExecutionRole` (I already had one)

![](/assets/img/temp/Pasted%20image%2020230331134456.png)

# 7. Create a new task definition revision

Now, navigate back to <span style="background:#fff88f">ECS service</span> and select "<span style="background:#fff88f">Task definitions</span>" in the left panel.

![](/assets/img/temp/Pasted%20image%2020230331134628.png)

Click the task definition and select "Create new vision -> Create new revision" in the top-right corner.

![](/assets/img/temp/Pasted%20image%2020230331134706.png)

Scroll little bit and you'll find "Environment variables - optional" section. Enter the key (env variable name), select "ValueFrom", and enter `arn:aws:ssm:<your region>:<your aws account id>:parameter/SECRET_NICKNAME` in the "Value" field.

![](/assets/img/temp/Pasted%20image%2020230331134900.png)

Scroll to the bottom and click "<span style="background:#fff88f">Create</span>"

You can see that the new task definition revision has been created.

![](/assets/img/temp/Pasted%20image%2020230331135044.png)

# 8. Update service

Go to the Clusters and select the cluster you created.

![](/assets/img/temp/Pasted%20image%2020230331135158.png)

Then, click the service in "Services" panel.

![](/assets/img/temp/Pasted%20image%2020230331135235.png)

Now we need to update our service with the newly created task definition which contains the environment variable referencing the Parameter Store.

Click "<span style="background:#fff88f">Update service</span>" in the top-right corner.

Then, select "Force new deployment".

You can see that the new task definition is now available. So click revision `2 (LATEST)`.

![](/assets/img/temp/Pasted%20image%2020230331135406.png)

Now, scroll to the bottom and click "<span style="background:#fff88f">Update</span>".

Select "<span style="background:#fff88f">Deployments and events</span>" panel on the top, and you'll see that the updated service is in progress for a new deployment.

![](/assets/img/temp/Pasted%20image%2020230331135950.png)

After a moment, you can see that the new deployment is successful!

![](/assets/img/temp/Pasted%20image%2020230331140152.png)

Let's open the browser and see if our server is updated. Make sure you enter the DNS name shown in the load balancer.

![](/assets/img/temp/Pasted%20image%2020230331141554.png)

Congratulations! Now you're able to pass any environment variable using the AWS Parameter Store in your own project.
