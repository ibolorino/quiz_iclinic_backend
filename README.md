# Quiz Iclinic

Quiz Iclinic is a challenge for fullstack job made with Django and React Native


## Installation

### Django and requirements

Go to your workspace folder and create a Virtual Environment:

```
python3 -m venv venv
```

Clone repository:

```
git clone https://github.com/ibolorino/quiz_iclinic_backend.git
```
Install requirements:

```
cd quiz_iclinic_backend
pip install -r requirements/local.txt
```

If you have any `Failed building wheel for 'module name'` error, you need to install wheel and reinstal requirements:

```
pip install wheel
pip install -r requirements/local.txt
```

### PostgreSQL

Quiz Iclinic requires PostgreSQL 12.  Go to [PostgreSQL](https://www.postgresql.org/) and follow documentation to install it.

Create postgresql database:

```
CREATE DATABASE quiz_iclinic OWNER username;
GRANT ALL PRIVILEGES ON DATABASE quiz_iclinic TO username;
```
Replace 'username' for postgres user

### Running Backend

Create '.env' file on quiz_iclinic_backend folder with the following content:

```
DJANGO_DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/quiz_iclinic
CORS_ORIGIN_ALLOW_ALL=True
ALLOWED_HOSTS=localhost:3000
```

Database Migration:
```
./manage.py makemigrations
./manage.py migrate
```

You will need a superuser to access django admin to create questions and answers:
```
./manage.py createsuperuser
```

Run server:
```
./manage.py runserver
```

To access Django Admin, go to http://localhost:8000/admin and login with superuser created.

## Don't forget to install and run frontend:

[Frontend Quiz Iclinic](https://github.com/ibolorino/quiz_iclinic_frontend)