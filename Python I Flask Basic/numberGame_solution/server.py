from flask import Flask, redirect, request, render_template, session, flash
import random

app = Flask(__name__)
app.secret_key = "SecretGarden"
@app.route('/')
def index():
    session['number'] = random.randrange(0,101)
    session['guess'] = 'guess'
    print 'the number is '
    print session['number']
    return render_template('index.html')
@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print 'guess: '
    print session['guess']
    print 'the number is '
    print session['number']
    #validate guess
    if session['guess'] < 1:
        flash('Please guess a number higher than 0.')
    elif session['guess'] > 100:
        flash('Please guess a number lower than 100')

    if '_flashes' in session:
        return redirect('/')
    return render_template('index.html')
    #determine whether guess is match, too low, or too high
    # if int(session['guess']) < session['number']:
    #     return render_template('tooLow.html')
    # elif int(session['guess']) > session['number']:
    #     return render_template('tooHigh.html')
    # elif int(session['guess']) == session['number']:
    #     return render_template('right.html')
@app.route('/play', methods=['POST'])
def playAgain():
    session.pop('number')
    session.pop('guess')
    return redirect('/')
app.run(debug=True)
