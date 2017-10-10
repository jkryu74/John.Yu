from flask import Flask, flash, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
import datetime
import re
app = Flask(__name__)
app.secret_key = "slimshady"
mysql = MySQLConnector(app, 'email_wdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    show_query = mysql.query_db("SELECT * FROM emails")
    return render_template('index.html', all_emails=show_query)
@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'email':request.form['email']
    }
    if not EMAIL_REGEX.match(data['email']) or len(data['email']) < 5:
        flash("NOT VALID EMAIL", 'error')
        return redirect('/')
    else:
        add_query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, now(), now())"
        add_email = mysql.query_db(add_query, data)
        return redirect('/')
@app.route('/delete', methods=['POST'])
def delete():
    del_query = "DELETE FROM emails WHERE id = :id"
    data = {
        "id" : request.form['id']
    }
    email = mysql.query_db(del_query, data)
    return redirect('/')
app.run(debug=True)
