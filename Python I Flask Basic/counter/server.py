from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    render_template('index.html')

@app.route('/visits', ['POST'])
def times_visited():
    session['x'] = request.form('i')
    return redirect('/Submit')

@app.route('/Submit', ['POST'])
def submit():
    return render_template('submit.html')

@app.route('/back')
def go_back():
    return rediret('/')
