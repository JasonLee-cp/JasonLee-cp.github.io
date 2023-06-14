---
layout: post
title: "Deploy FastAPI on AWS Lambda"
subtitle: ""
categories: dev
tags: deployment
comments:
---

1. Serverless Computing
2. Pros/Cons of Serverless
3. Deploy FastAPI on AWS Lambda

---


## What is Serverless Computing?
Serverless is a cloud computing model where developers can run applications without worrying about the provisioning and managing the servers and the infrastructure. Consequently, serverless computing enables developers to mainly focus on writing applications and business logics. Despite the name "serverless" suggests, it doesn't mean there's no server. There are servers running but they're invisible to the developers. The leading serverless cloud providers are AWS Lambda, Azure Functions, Google Cloud Functions and IBM Cloud Code Engine.

## Pros and Cons of Serverless

Serverless architecture offers a number of advantages to developers but it can also incur some drawbacks.

**Advantages**
1. <span style="background:#fff88f">No server management</span>
	* The management of the server and the infrastructure is all handled by the provider so developers can focus on writing business logics.
2. <span style="background:#fff88f">Only charge for what you use</span>
	* Developers pay only for what they use. Some providers even break down charges into 100ms frames. You don't have pay anything when there's no resources being used.
3. <span style="background:#fff88f">Highly scalable</span>
* As the user traffic goes up, the server capacity automatically increases and the vice versa. If a function needs to be run in multiple instances, the provider starts up new servers and end them when done. Consequently, developers don't have to worry about the time when there's an unusual amount of user traffic comes in unexpectedly.

**Disadvantages**
1. <span style="background:#fff88f">More challenging testing and debugging</span>
	* As we have less control on the server managements, it's hard to replicate the server environment on the local development environment.
2. <span style="background:#fff88f">Performance may be affected</span>
	* As the server is not constantly running (some functions are invoked rarely), the cold start-up time might degrade performance.
3. <span style="background:#fff88f">Vendor lock-in</span>
	* As the server management and the infrastructure relies on a single vendor, it might be difficult to migrate to another vendor as each vendor offers different features and workflows.

## Deploy FastAPI service to AWS Lambda

AWS Lambda is a major serverless computing provider offered by Amazon.

### 1. Install Poetry

Poetry is a great tool for package and dependency management.

To install, 

```bash
brew install pipx
```

```bash
pipx install poetry
```

After installation, create a project directory by

```bash
poetry new serverless_demo
cd serverless_demo
```

Then, you will see the project structure as below.

```bash
serverless_demo/
├── README.md
├── poetry.lock
├── pyproject.toml
├── serverless_demo
│   ├── __init__.py
└── tests
    └── __init__.py
```

## 2. Dummy FastAPI Project

First, install FastAPI with Poetry.

```bash
poetry add "fastapi" "uvicorn[standard]"
```

Then, create `main.py` under `serverless_demo/serverless_demo/main.py` and give a simple router.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main_route():
	return {"Message": "Hello world!"}
```

Let's test our app.

```bash
uvicorn serverless_demo.main:app
```

## 3. Serverless Framework
Serverless Framework is a popular open-source web framework built with Node.js for building applications on AWS Lambda.

Install by

```bash
curl -o- -L https://slss.io/install
```

Now create `serverless.yml` file under the project root directory and copy and paste the following code.

```yml
service: serverless-demo
frameworkVersion: '3'

provider:
	name: aws
	runtime: python3.9
	region: ap-northeast-2

functions:
	api:
		handler: serverless_demo.main.handler
		events:
			- httpApi: '*'

package:
	exclude:
		- node_modules/**
		- venv/**

plugins:
	- serverless-python-requirements
```

(Make sure to configure your AWS credentials first before deployment, for example by using `aws-cli`).

We have one plugin `serverless-python-requirements` which is a Python packaging plugin with `requirements.txt` or `pyproject.toml` file.

Notice that under `function/api`, we have `handler`. We need to wrap our ASGI app to adapt AWS Lambda and API Gateway and we use `Mangum` for this.

```bash
poetry add mangum
```

Then, add the handler in `main.py`.

```python
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def main_route():
	return {"Message": "Hello world!"}

handler = Mangum(app)
```

Since serverless is a `Node` package, we have to initialize an npm project and install the plugin.

```bash
npm init -y
npm install serverless-python-requirements
```

## 4. Deployment

Finally, let's deploy our project to AWS Lambda. Move to the project root directory and

```bash
serverless deploy
```

You can see we have successfully deployed our app to AWS Lambda. You can test our app with the `endpoint` URL.
![](/assets/img/temp/serverless1.png)

![](/assets/img/temp/serverless2.png)

To test our app on AWS Lambda, go to AWS console and select Lambda. On the left panel, click `Functions` and select the project name. Then you will see the following.

![](/assets/img/temp/serverless3.png)