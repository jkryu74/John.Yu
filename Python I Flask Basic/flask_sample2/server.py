from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "appkey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/re', methods=['POST'])
def request():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    return redirect('/submit')

@app.route('/re', methods=['Get'])
def submit():
    return render_template('submit.html')

app.run(debug=True)
