from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "NBA"
mysql = MySQLConnector(app, 'fullfriends')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    query = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends=query)

@app.route('/create', methods=['POST'])
def create():
    data = {
        "first_name" : request.form['first_name'],
        "last_name"  : request.form['last_name'],
        "email"      : request.form['email']
    }
    if not EMAIL_REGEX.match(data['email'] or len(data['email']) < 4):
        flash('INVALID EMAIL: Try again.', 'error')

    if '_flashes' in session:
        return redirect('/')

    add_query = "INSERT INTO friends (firstname, lastname, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, now(), now())"
    add_friend = mysql.query_db(add_query, data)
    return redirect('/')

@app.route('/edit')
def go_edit():
    edit_query = "SELECT (id, firstname, lastname, email) FROM friends"
    return render_template('edit.html', friend=edit_query[0])

@app.route('/update', methods=['POST'])
def update():
    update_query = "UPDATE friends SET firstname=:first_name, lastname=:last_name, email=:email, updated_at=now() WHERE id = :id"
    data = {
        "id"         : request.form['id'],
        "first_name" : request.form['first_name'],
        "last_name"  : request.form['last_name'],
        "email"      : request.form['email']
    }
    if not EMAIL_REGEX.match(data['email']) or len(data['email']) < 4:
        flash('INVALID EMAIL: Try again.', 'error')

    if '_flashes' in session:
        return redirect('/')

    update_friends = mysql.query_db(update_query, data)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    del_query = "DELETE FROM friends WHERE id = :id"
    data = {
        "id"         : request.form['id']
    }
    del_friends = mysql.query_db(del_query, data)
    return redirect('/')

app.run(debug=True)
