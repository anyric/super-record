# super-record
[![CircleCI](https://circleci.com/gh/anyric/super-record/tree/develop.svg?style=svg&circle-token=9a8691ee19049daa3538b4168d097e776dd4d0bc)](https://circleci.com/gh/anyric/super-record/tree/develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fdc129400a8240d6b843ef4250be4279)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=anyric/super-record&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/fdc129400a8240d6b843ef4250be4279)](https://www.codacy.com?utm_source=github.com&utm_medium=referral&utm_content=anyric/super-record&utm_campaign=Badge_Coverage)
## Description
Super Record is an information management system which serves the purpose of automating business processes of a supermarket in an effort to improve efficiency, accuracy, performance and accountability.

## Table of Contents
- [Key Features](#key-features)
- [Setup](#setup)
    - [Dependencies](#dependencies)
    - [Getting Started](#getting-started)
- [Running the application](#running-the-application)
- [Testing](#testing)
- [Docker Environment](#docker-environment)

## Key Features
    1. User Accounts Management
    2. Purchase Management 
    3. Stock/Products Management
    4. Sales Management
    5. Expense Management
    6. Report Generation 

## Setup
### Dependencies
* [Python 3.7](https://www.python.org/) - popular general-purpose scripting language suited for web development
* [Django 2.2](https://docs.djangoproject.com/en/2.2/) - A web application framework for Python

### Getting Started
Setting up project in development environment
* Ensure Python 3.7 is installed by running:
```
python --version
```
* Ensure pipenv is installed or you can follow the intallation from [PIPENV](https://docs.pipenv.org/)
* Create a folder for the project by running:
```
mkdir myprojectfoldername
```
* cd in to `myprojectfoldername`
* Create a virtualenv using pipenv by running:
```
pipenv shell
```
* Clone the project repo by running:
```
git clone https://github.com/anyric/super-record.git
```

### Database setup
Create a database locally on your machine named `superrecord` and add the name as a value to the environment variable. Use the `env.sample` template to create a .env file

### Running the application
* Export the .env file by running 
```
. .env
```
* Inside the project root folder i.e src/, run the command below in your console
```
python manage.py migrate

python manage.py runserver
```
* Navigate to `http://127.0.0.1:8000/`
* Login with the default setup credential `username=admin` and `password=1234@admin` and then remember to edit the credentials
* Configure the system to your need.

### Testing
* Export the .env file as describe above if you haven't 
* Run the command below:
```
python manage.py test
```

### Docker Environment
#### Running a Docker development Environment
#### Prerequisites
 - docker
 - docker-compose

#### Setup local docker development environment
* Clone the repository and navigate to the root folder.

#### To build docker images
Run the command below:
```
make build
```

#### To start the local development server
Run the command below:
```
make start
```

#### Running tests
Run the command below:
```
make test
```

#### Stoping the development server
```
make stop
```

#### Cleaning up local docker environment
```
make clean
```

## Developer and Maintainer
* Anyama Richard
