from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
from db import db_create_connection, db_register_user, db_register_check, db_login_check

# Warning: make yourself a venv to install all the needed packages
# 1. make venv command: python3 -m venv venv
# 2. activate venv: Windows[.\venv\Scripts\activate] / Linux[source ./venv/bin/activate]
# 3. install requirements: pip install -r requirements.txt

app = Flask(__name__, template_folder='', static_folder='')

# The secret key is needed for CSRF protection on wtforms (make sure it's something random if using it)
app.config["SECRET_KEY"]="very_secret_key_definitely_change"

@app.route("/", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
def index():

    form = RegistrationForm()

    conn = db_create_connection()
    cursor = conn.cursor()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        if db_register_check(email, cursor):
            db_register_user(email, password, cursor)
            conn.commit()  
  
    cursor.close()
    conn.close()

    return render_template("register.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()

    conn = db_create_connection()
    cursor = conn.cursor()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        if db_login_check(email, password, cursor):
            pass # There is no further logic implemented here, maybe in another project

    return render_template('login.html', form=form)