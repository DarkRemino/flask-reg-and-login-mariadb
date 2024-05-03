import mariadb as db

# If you didn't look through the readme:
# you first need to setup a MariaDB instance
# and then run setup_db.sql to create the schema + tables

# Link to the MariaDB guide for the Python connector: https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/

# This is currently configured to work with the default XAMPP config on Windows
def db_create_connection():
    return db.connect(
        user='root',
        # password='test123', # The default config on XAMPP doesn't have a password
        host='127.0.0.1',
        database='flask_registration_and_login_example',
        port=3306
    )

# Checks whether a user with such an email has already been created
def db_register_check(email, cursor):

    # Important! - The syntax here needs to be exactly like that, you cannot asign a 
    # var to the cursor.execute() function as it is simply not going to work.
    cursor.execute("SELECT id FROM users WHERE email=?", (email,)) # The comma here is not a mistake
    existing_user = cursor.fetchone()

    # Returns False if such a user exists and True if it doesn't
    # (the logic being that you pass the check)
    if existing_user:
        return False
    else:
        return True

# Writes a row into the 'users' table of the DB
def db_register_user(username, password, cursor):
    cursor.execute("INSERT INTO users(email, password) VALUES(?,?)", (username, password))

def db_login_check(email, password, cursor):

    # Works almost exactly the same as register_check, but it returns True when such a user exists instead of False
    cursor.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
    existing_user = cursor.fetchone()

    if not existing_user:
        return False
    else:
        return True