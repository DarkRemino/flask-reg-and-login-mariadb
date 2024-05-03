from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import EqualTo, Regexp, InputRequired

# This is truly just meant as an example to prove it works
# If you're considering implementing this in a real project,
# please have proper email validation and use hashing functions for the password

class RegistrationForm(FlaskForm):

    # Is required and has a regex that forces the format to be more or less an email address (something@something.something)
    # WTForms includes an email field as well as a validator for it but it is not implemented in this example.
    email = StringField('Email:',validators=[InputRequired(), Regexp("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message='This is not a valid email address!')])

    # Is required and has a regex for at least one upper- and lower-case English letter, one special character and one digit
    password = PasswordField('Password:', validators=[InputRequired(), Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")])

    # Has to be the same as password
    password_check = PasswordField('Repeat the password:', validators=[])

    # Many implementations prefer to write the submit directly into the html
    # since it isn't special in any way, but here it's done within the form.
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):

    # There's no real need for comment here, the fields are pretty much the same as in registration without the password_check
    email = StringField('Email: ', validators=[InputRequired()])
    password = PasswordField('Password: ', validators=[InputRequired()])
