from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'secretkey'
mysql = MySQLConnector(app, 'the_wall')

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    reg_data = {
        'firstname' :  request.form['firstname'],
        'lastname'  :  request.form['lastname'],
        'email'     :  request.form['email'],
        'password'  :  request.form['password'],
        'confirm'   :  request.form['confirm']
    }

    query = "SELECT first_name, last_name, email FROM users where email = :email"
    user = mysql.query_db(query, reg_data)

    if reg_data['password'] != reg_data['confirm']:
        flash('Your Passwords do not Match, please try again.')
    elif reg_data['password'] < 8:
        flash('Your Password must be at least 8 characters long.')
    if not EMAIL_REGEX.match(reg_data['email']):
        flash('Your Email is INVALID, please try again.')
    if len(request.form['firstname']) and len(request.form['lastname']) < 2:
        flash('Please enter your Full Name...')

    if '_flashes' in session:
        return redirect('/')

    reg_data['password'] = bcrypt.generate_password_hash(reg_data['password'])

    reg_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
    VALUES (:firstname, :lastname, :email, :password, now(), now())"
    reg_add = mysql.query_db(reg_query, reg_data)
    return render_template('success.html', user=user[0])

@app.route('/wall', methods=['POST'])
def login():
    login_data = {
        'email' : request.form['email'],
        'password' : request.form['password']
    }
    query = "SELECT * FROM users WHERE email = :email"
    user = mysql.query_db(query, login_data)

    if user:
        if bcrypt.check_password_hash(user[0]['password'], login_data['password']):
            session['email'] = request.form['email']
            return render_template('login.html')
        else:
            flash("Error, please try again.")
            return redirect('/')
    return render_template('login.html')

@app.route('/messages', methods=['POST'])
def wall():
    if 'email' in session:
        data = { 'email' : session['email'] }
        query = "SELECT id FROM users WHERE email = :email"
        messages = mysql.query_db(query, data)
        session['id'] = user.id

        query = "SELECT * FROM comments"
        comments = mysql.query_db(query)
        return render_template('login.html', messages=messages, comments=comments)

@app.route('/messages')
def messages():
    if 'email' in session:
        data = {
            'email' : session['email']
            'id' : session['id']
        }
        query = "SELECT * FROM messages WHERE id = :id"
        id = mysql.query_db(query, data)

        input_data = {
            'message' : request.form['message'],
            'id'      : id[0]['id']
        }
        input_query = "INSERT INTO messages (id, message, created_at, updated_at) \
        VALUES (:id, :message, now(), now())"
        message = mysql.query_db(input_query, input_data)
        return redirect('/wall')

@app.route('/comments', methods=['POST'])
def comments():
    if 'email' in session:
        data = { 'email' : session['email'] }
        query = "SELECT id FROM users WHERE email = :email"
        user_id = mysql.query_db(query, data)

        input_data = {
            'id'          : id[0]['id'],
            'messages_id' : messages_id[0]['id'],
            'comment'     : request.form['comment']
        }
        input_query = "INSERT INTO messages (id, user_id created_at, updated_at) \
        VALUES (:comment, now(), now())"
        comment = mysql.query_db(input_query, input_data)
        return redirect('/wall')

app.run(debug=True)
