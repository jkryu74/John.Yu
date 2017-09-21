from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():

   name = request.form['name']
   email = request.form['email']
   language = request.form['lang']
   comments = request.form['comments']

   return render_template('users.html', name=name, email=email, language=language, comments=comments)

app.run(debug=True)
