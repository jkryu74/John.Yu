from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/data', methods=['POST'])
def create_user():
   name = request.form['name']
   email = request.form['email']
   return redirect('user.html', name='name', email='email')

app.run(debug=True)
