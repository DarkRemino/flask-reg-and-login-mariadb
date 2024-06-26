# This is an example of a login/registration system in FLask

It was designed to take away the abstraction of Flask-Login and SQLAlchemy
as I found them to hamper me when I needed to modify the way a registration/login
actually worked under the hood (add organizations, roles (beyond admin) and so on)

## What does this example do?

The idea of the example is a simple Flask application, connected to a MariaDB instance,
that does user registration and login using simple SQL statements inside functions. The
point of the repo is to avoid any abstraction on top of SQL, be that Data Models to define
what is already available in the DB or complex query functions that are literally just
5-word quries.

The example consists of 2 pages - registration and login, with the barest of necessary validation:
 - the email needs to be an email
 - the 2 passwords on registering have to match
 - and some other minor things

The end result are 2 incredibly simple pages that let you register yourself and then login.
The login doesn't do anything as it is only meant as an example, but the code is made in such
a way that implementing further actions after login should be trivial.

I have tried to add as many comments wherever I deemed it necessary to explain a part of the code,
so that even a person seeing this type of code should be able to orient themselves in it.

## How to get it running

In order for this example to work, you need 2 main things:
1. A venv with all the needed packages installed
2. A MariaDB/MySQL instance running on your local machine with the proper schema+tables

### For the venv:
 - make sure you have Python installed on your PC
 - open the directory of the example
 - in terminal, type "python3 -m venv venv" (depending on OS, it might ask you to install a package)
 - once created, activate the venv by running either ".\venv\Scripts\activate"(Windows) or "source ./venv/bin/activate"(Linux)
 - install the required packages by running "pip install -r requirements.txt"

### For the db:
 - get MariaDB for your OS by: Installing XAMPP (Windows) / Installing the service mariadb or mariadb-server depending on distro (Linux)
 - Windows users are done here as db.py is currently made to use root without a password
 - Linux users will need to first run mysql_secure_installation. It is highly recommended that you set a password (and even a new user) and rewrite the connection in db.py
 - Once you have a configured MariaDB instance (MySQL should also work), you can execute the db_setup.sql file or, alternatively, make the schema and tables yourself.

### After all is set up:
Just activate the venv (if you haven't already) and type in "flask run --debug" to start the site. This will run the dev server Flask provides on localhost:5000
The registration form can be accessed on / and /register, and the login form - on /login.

### I hope this little example helps you!
