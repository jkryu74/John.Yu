from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    session['guessNumber'] = random.randrange(0,101)
    session['typeNumber'] = 'typeNumber'
    print session['guessNumber']

    return render_template('index.html')

@app.route('/indexTwo', methods=['POST'])
def index_two():
    session['typeNumber'] = int(request.form['typeNumber'])
    print session['guessNumber']
    print session['typeNumber']

    if int(request.form['typeNumber']) == session['guessNumber']:
        return render_template('success.html')
    elif int(request.form['typeNumber']) > session['guessNumber']:
        return render_template('tooHigh.html')
    elif int(request.form['typeNumber']) < session['guessNumber']:
        return render_template('tooLow.html')

    return redirect('/')

@app.route('/playagain', methods=['POST'])
def play_again():
    session.pop('guessNumber')
    session.pop('typeNumber')

    return redirect('/')
app.run(debug=True)
