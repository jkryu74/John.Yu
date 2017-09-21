from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def first_pythonEmb():
    return render_template('/index.html', phrase="Hello", Times=5)

app.run(debug=True)
