---
layout: post
title: "Upload a Docker container image to ECR private repository"
subtitle: ""
categories: dev
tags: deployment
comments:
---

1. Introduction
2. Create an IAM user
3. Create an ECR repository
4. Upload our image to ECR repository

---

# 1. Introduction

In the [last post](https://noisrucer.github.io/dev/2023/03/25/dockerize/), we dockerized our FastAPI project and ran it locally.

In this article, we'll upload our container to AWS ECR (Elastic Container Registry) which is a registry for container images like Docker Hub. Then, we will deploy our server ECS.

# 2. Create IAM user

In order to publish our container image to private ECR repository, we first need to <span style="background:#fff88f">create a user in IAM</span> (Identity and Access Management).

Open up AWS console and navigate to IAM.

![](/assets/img/temp/Pasted%20image%2020230331040653.png)

Then, select "Users" in the left panel and click "Add Users".

Enter user name and click "Next".

![](/assets/img/temp/Pasted%20image%2020230331041049.png)

Select "Attach policies directly" and add <span style="background:#fff88f">AmazonEC2ContainerRegistryFullAccess</span> policy and <span style="background:#fff88f">AmazonECS_FullAccess policy</span>.
![](/assets/img/temp/Pasted%20image%2020230331041243.png)

![](/assets/img/temp/Pasted%20image%2020230331041358.png)

Click "Next" and create user.

![](/assets/img/temp/Pasted%20image%2020230331042157.png)

Now, select `ecr-demo-user-1` and under "Security Credentials" panel, you will find "Access keys" section.

![](/assets/img/temp/Pasted%20image%2020230331042255.png)

Click "Create access key" and select "CLI".

![](/assets/img/temp/Pasted%20image%2020230331042329.png)

Click "Next" and type some tag value and click "Create access key".

![](/assets/img/temp/Pasted%20image%2020230331042404.png)

Then you'll see `Access Key` and `Secret Access Key`. Store these keys safely somewhere in your local storage.

# 3. Create a ECR repository

Open up console search bar and navigate to <span style="background:#fff88f">ECR (Elastic Container Registry)</span> service.

Click "private" on the top panel and click "create repository".

Then, enter your repository name and select "create".

![](/assets/img/temp/Pasted%20image%2020230331041721.png)

Now if you go to the repositories section, you can see that `simple-demo` private repository has been created.

Select `simple-demo` repository and you'll see that there're no images pushed to the repository yet.

![](/assets/img/temp/Pasted%20image%2020230331041909.png)

To push our own image to the repository, click "View push commands" which contain detailed procedures to uploade our image into the repository.

![](/assets/img/temp/Pasted%20image%2020230331043541.png)

# 4. Upload our image to ECR repository

Go to your project root directory and enter the four procedures shown in
"View push commands" in your terminal.

For the first step, enter the AWS access key and secret key you generated from IAM user.

![](/assets/img/temp/Pasted%20image%2020230331043606.png)

After you go through all the steps, refresh the "Images" page and you'll see that our image has been pushed to the repository.

![](/assets/img/temp/Pasted%20image%2020230331043653.png)
