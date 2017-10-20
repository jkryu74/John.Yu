from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'secretkey'
mysql = MySQLConnector(app, 'login_reg')

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/useregister', methods=['POST'])
def useregister():
    reg_data = {
        'firstname' :  request.form['firstname'],
        'lastname'  :  request.form['lastname'],
        'email'     :  request.form['email'],
        'username'  :  request.form['username'],
        'password'  :  request.form['password'],
        'confirm'   :  request.form['confirm']
    }

    check_query = "SELECT * FROM login_reg.login WHERE email = :email"
    check_user  = mysql.query_db(check_query, reg_data)

    if reg_data['password'] != reg_data['confirm']:
        flash('Your Passwords do not Match, please try again.')
    elif reg_data['password'] < 8:
        flash('Your Password must be at least 8 characters long.')
    if not EMAIL_REGEX.match(reg_data['email']) and len(reg_data['email']) < 4:
        flash('Your Email is INVALID, please try again.')
    if len(request.form['firstname']) and len(request.form['lastname']) < 2:
        flash('Please enter your Full Name...')
    if len(check_user) != 0:
        flash('Please use a differenet email address.')

    if '_flashes' in session:
        return redirect('/')

    reg_data['password'] = bcrypt.generate_password_hash(reg_data['password'])

    reg_query = "INSERT INTO login_reg.login (first_name, last_name, email, user_name, password, created_at, updated_at) VALUES (:firstname, :lastname, :username, :email, :password, now(), now())"
    reg_add = mysql.query_db(reg_query, reg_data)
    attempt = "Registration"
    return render_template('success.html', attempt=attempt)

@app.route('/login', methods=['POST'])
def login():
    login_data = {
        'email'    : request.form['email'],
        'password' : request.form['password']
    }
    login_query = "SELECT * FROM login_reg.login WHERE email = :email"
    user = mysql.query_db(login_query, login_data)

    if user:
        if not bcrypt.check_password_hash(user[0]['password'], reg_data['password']):
            flash("Processing Error, Please try again.")
        else:
            flash("Error, please try again.")
            return redirect('/')

    attempt = "Login"
    return render_template('success.html', attempt=attempt)

app.run(debug=True)
