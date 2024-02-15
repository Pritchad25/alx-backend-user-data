# Project Title: Session authentication

## Table of Contents
1. About
2. Learning Objectives
3. Requirements
4. Getting Started
5. Setup
6. Run
7. Routes
8. License

## About <a name="about"></a>
This project is part of the curriculum of the ALX Software Engineering program. The main objective of this project is to understand and implement Session authentication.

## Learning Objectives <a name="learning-objectives"></a>
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Requirements <a name="requirements"></a>
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README file at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation
- All your classes should have a documentation
- All your functions (inside and outside a class) should have a documentation

## Getting Started <a name="getting-started"></a>
To get started with this project, do the following:

## Files <a name="Files"></a>

## models/ <a name="models/"></a>

- `base.py`: the base of all models of the API - handles the serialization of the file.
- `user.py`: the user model

## api/v1 <a name="api/v1"></a>

- `app.py` : the entry point of the API
- `views/index.py`: the basic endpoints of the API: `/status` and `/stats`
- `views/users.py` : provides all the users endpoints

## SetUp <a name="SetUp"></a>

`$ pip3 install -r requirements.txt`

## Run <a name="Run"></a>

`$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app`

## Routes <a name="Routes"></a>

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users` : returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, last_name` (optional) and `first_name` (optional)
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `first_name` and `last_name` )

## ## License <a name="license"></a>
ALX
