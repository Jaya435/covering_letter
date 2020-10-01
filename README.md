# About Me

This Repository contains a Flask project that uses an API to save different sections of information about me to a database. These are then served up to a webpage for the user. It is meant to be reusable and scalable for different purposes.

## Getting Started

These instructions will let you get a copy of the project up and running on your local machine for viewing the information See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to run this programme using Python3. You can follow a guide here to install Python3 on your local machine https://installpython3.com/. Once Python3 is installed, you can run this programme from within a virtual environment. You can do this by creating a virtual environment as below:

```
python3 -m venv /path/to/new/virtual/environment
```
to activate the venv use:
```
source /path/to/new/virtual/environment/bin/activate
```
to install the required modules in said venv:
```
pip install -r /path/to/requirements.txt
```
You will need a suitable database running in the background, in my case I used Postgresql 13. You will then need to create an inital database, first log into your terminal entry for your db:
```
CREATE DATABASE blog_api_db;
```
There are then a few environment variables that need to be created:
```
export DATABASE_URL=postgres://user:password@host:port/db_name
export FLASK_ENV=development
```
### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository onto your local machine
```
https://github.com/Jaya435/covering_letter.git
```
Then run
```
cd api
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python run.py
```

The web application should now be running successfully, and you should be able to browse some information about me and my background.

## Authors

* **Tom Richmond** - *Initial work* - [Jaya435](https://github.com/Jaya435/)
