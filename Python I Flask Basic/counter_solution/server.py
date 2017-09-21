from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "ASecretIsThis"
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    print 'counter is {}'.format(session['counter'])
    return render_template('index.html')
@app.route('/plusTwo', methods=['POST'])
def plusTwo():
    session['counter'] += 1
    print 'counter is now {}'.format(session['counter'])
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session.pop('counter')
    print 'counter has been reset'
    return redirect('/')

app.run(debug=True)
