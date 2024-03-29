# [City Guid](https://github.com/ToluFash/City-Guide) Server (Project: city_guide)
[![Build Status](https://travis-ci.org/project-travel-mate/server.svg?branch=master)](https://travis-ci.org/project-travel-mate/server)
> [Django 2.0](https://docs.djangoproject.com/en/2.0/releases/2.0/) server for Travel Mate

## Local setup instructions
+ Clone the project from source
```shell
git clone https://github.com/project-travel-mate/server && cd server
```
+ Setup virtual environment
```shell
pip install virtualenv
virtualenv venv --python=python3.6
```
Now activate the environment shell with:
```shell
source venv/bin/activate  # On Linux
```
or
```bat
venv\Scripts\activate  & :: On Windows
```
+ Install all dependencies
```shell
pip install -r requirements.txt
```
+ Setup Postgres database and user
*(assuming Postgres is already installed on system; See [postgres setup instructions](http://postgresguide.com/setup/install.html))*

For Linux-
```
$ sudo -u postgres createuser city_guide
$ sudo -u postgres createdb city_guide

$ sudo -u postgres psql
psql=# alter user city_guide with encrypted password 'pass';
psql=# grant all privileges on database city_guide to city_guide ;
psql=# ALTER USER city_guide CREATEDB ;
```
For Windows-
```
The complete path>psql -U postgres -h localhost
Password:The one given during setup of postgres.
postgres=# create database city_guide;
postgres=# create user city_guide;
postgres=# alter user city_guide with encrypted password 'pass';
postgres=# grant all privileges on database city_guide to city_guide ;
postgres=# ALTER USER city_guide CREATEDB ;
```

+ Database migrations
```
python manage.py makemigrations
python manage.py migrate
```

+ Run Tests
```
python manage.py test
```

+ Finally! Run server
```
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000)

+ To access Django Admin
```
python manage.py createsuperuser
```

When prompted, type your username (lowercase, no spaces), email address, and password.
For example, the output should look like this:

```
Username: city_guideadmin
Email address: city_guideadmin@city_guide.com
Password:
Password (again):
Superuser created successfully.
```

+ Re-run the server
```
python manage.py runserver
```

Open [localhost:8000/admin](http://localhost:8000/admin)

## Working with authenticated APIs

> You would need to have a registered user, with which you can generate a authentication token. Follow the following steps to generate a token *(You can download [Postman client](https://www.getpostman.com/) to make the following POST calls)*
Reference: [TokenAuthentication API docs](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

+ Make a POST call to `/api/sign-up` with 4 form-data body objects: `email`, `password`, `firstname`, `lastname`. You should get *"Successfully registered"* response with 201 status code.
+ Make a POST call to `/api/sign-in` with 2 form-data body objects: `username` (which is your email Id you used for sign up), `password`. You will get a token in JSON response, store it somewhere.
+ For making any subsequent request, use the above token by sending it as an "Authorization HTTP Header", eg: `Authorization: Token <your token>`
