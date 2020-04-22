# Project 3

Web Programming with Python and JavaScript

## Getting Started

To clone and run this application, you'll need [Git](https://git-scm.com), [Pip](https://pip.pypa.io/en/stable/installing/), and [Python](https://www.python.org/) version 3.7 (or higher) installed.

## Installing

To start, clone the repository and set up your environment with the required dependencies from the `requirements.txt` file.

```bash
# Clone this repository
$ git clone https://github.com/danialgagne/project3.git

# Go into the repository
$ cd project3

# Install the dependencies
$ pip install -r requirements.txt
```

You'll need to apply all database migrations and create a superuser if you want to add menu items:

```bash
# set up your database
$ python manage.py migrate

# create a superuser to access django admin
$ python manage.py createsuperuser
```

The app is now ready to run:

```bash
# run your django server
$ python manage.py runserver
```