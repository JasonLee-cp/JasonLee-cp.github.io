---
layout: post
title: "Deploy our FastAPI server to AWS ECS Fargate"
subtitle: ""
categories: dev
tags: deployment
comments:
---

In the last post --LINK--, we uploaded our simple FastAPI server container image to ECR.

In this article, we'll deploy our server on ECS Fargate so that you can access from anywhere around the world!

# 1. Create an Application Load Balancer (ALB)

Let's navigate to EC2.

![](/assets/img/temp/Pasted%20image%2020230331050446.png)

Then, click "Load Balancers" on the left panel.

![](/assets/img/temp/Pasted%20image%2020230331050517.png)

Click "Create load balancer".

![](/assets/img/temp/Pasted%20image%2020230331050546.png)

Select "Application Load Balancer"

![](/assets/img/temp/Pasted%20image%2020230331050611.png)

We need at least two Availability zones and one subnet per zone.
![](/assets/img/temp/Pasted%20image%2020230331051722.png)

Now, let's go to EC2 and create a security group that allows port 80 for HTTP request.

![](/assets/img/temp/Pasted%20image%2020230331050851.png)

Then, let's continue the Application Load Balancer configuration.

Link the security group we just created in ALB.
![](/assets/img/temp/Pasted%20image%2020230331051003.png)

Scroll down and click "Create target group"

![](/assets/img/temp/Pasted%20image%2020230331051238.png)

## Create a target group

Let's create a target group.

![](/assets/img/temp/Pasted%20image%2020230331051321.png)

![](/assets/img/temp/Pasted%20image%2020230331051443.png)

After creating a target group, go back to ALB configuration, and link the created target group.

![](/assets/img/temp/Pasted%20image%2020230331051544.png)

Finally, click "Create load balancer".
![](/assets/img/temp/Pasted%20image%2020230331050251.png)

# 2. Create a Task Definition

Let's go back to ECS service and create a cluster.

![](/assets/img/temp/Pasted%20image%2020230331051914.png)

Provide a cluster name and scroll down to the bottom and select "Create".

You can see the clutser we just created.

![](/assets/img/temp/Pasted%20image%2020230331052047.png)

# 3. Create a task definition

Select "Task definitions" in the left panel and click "Create new task definition". A task definition is like a `docker-compose` that defines the behaviors and settings of our serivce such as port mapping, which docker image we'll be using, CPU/memory usage, and so on.

Let's go ahead and create a new task definition.

![](/assets/img/temp/Pasted%20image%2020230331052156.png)

Let's add a task definition family name.

Then, grab the image name and image URL of the image we created before from ECR.

![](/assets/img/temp/Pasted%20image%2020230331052622.png)

Then, enter them into `Name` and `Image URI` in the task definition container settings.

Also, since our container is listening on 8000, we define a port mapping indiciating that the container port is 8000.
![](/assets/img/temp/Pasted%20image%2020230331052528.png)

Scroll to the bottom and click "Next".

In the next page, select `AWS Fargate(serverless)` for App environment setting. Also, specify CPU and Memory usage for your need.

![](/assets/img/temp/Pasted%20image%2020230331052801.png)

Next, assign **Task role** and **Task execution role**.
![](/assets/img/temp/Pasted%20image%2020230331052916.png)

Scroll down to the bottom and create a task definition.

In dashboard, you can see our task definition is successfully created.

![](/assets/img/temp/Pasted%20image%2020230331053039.png)

# 4. Create a service

Go to "Clusters" in the left panel and select our cluster.

![](/assets/img/temp/Pasted%20image%2020230331053123.png)

Click our cluster. Then, select "Create" for under Services tab.

![](/assets/img/temp/Pasted%20image%2020230331053152.png)

Select "Launch type" and set it to "Fargate".

![](/assets/img/temp/Pasted%20image%2020230331053303.png)

Now, link the task definition family into our service. Also, provide a service name.

![](/assets/img/temp/Pasted%20image%2020230331053405.png)

Since we mapped PORT `8000` for out container, create a security group that allows TCP 8000 PORT.

![](/assets/img/temp/Pasted%20image%2020230331123408.png)

Link the security group in service configuration.

![](/assets/img/temp/Pasted%20image%2020230331123600.png)

Now let's link the load balancer we created.

![](/assets/img/temp/Pasted%20image%2020230331053746.png)

Also, limk the target group we created.

![](/assets/img/temp/Pasted%20image%2020230331053803.png)

Scroll down to the bottom and click "Create".

Now, we can see that our service has been successfully created.

![](/assets/img/temp/Pasted%20image%2020230331124921.png)

After a moment, we can see that our service is running successfully.

![](/assets/img/temp/Pasted%20image%2020230331053949.png)

Now, to test our server, let's go to the load balancer and copy the DNS name and paste it in a browser.

![](/assets/img/temp/Pasted%20image%2020230331125020.png)

![](/assets/img/temp/Pasted%20image%2020230331125109.png)

Congratulation! You can see that our server is successfully running.

# 5. Conclusion

In the next article, I'll go over how to inject <span style="background:#fff88f">environment variables</span> into the container using <span style="background:#fff88f">AWS Systems Manager Parameter Store</span>.
