from flask import Flask, redirect, render_template, session, request
import random
import datetime
app = Flask(__name__)
app.secret_key = "WhisperingSecrets"
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'log' not in session:
        session['log'] = []
    length = len(session['log'])
    if length > 5:
        height = 40*length
    else:
        height = 200
    return render_template('index.html', height=height)
@app.route('/process_money', methods=['POST'])
def processMoney():
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        farm = random.randrange(10,21)
        session['gold'] += farm
        session['log'].append('Earned {} golds from the farm! ({:%m-%d-%Y %H:%M:%S})\n'.format(farm, datetime.datetime.now()))
    elif session['building'] == 'cave':
        cave = random.randrange(5,11)
        session['gold'] += cave
        session['log'].append('Earned {} golds from the cave! ({:%m-%d-%Y %H:%M:%S})\n'.format(cave, datetime.datetime.now()))
    elif session['building'] == 'house':
        house = random.randrange(2,6)
        session['gold'] += house
        session['log'].append('Earned {} golds from the house! ({:%m-%d-%Y %H:%M:%S})\n'.format(house, datetime.datetime.now()))
    elif session['building'] == 'casino':
        toss = random.randrange(0,2)
        casino = random.randrange(0,51)
        if casino == 0:
            session['log'].append('Entered a casino and did not lose or win anything. Phew! ({:%m-%d-%Y %H:%M:%S})\n'.format(casino, datetime.datetime.now()))
        if toss == 0: #loss
            session['gold'] -= casino
            session['log'].append('Ouch...Entered a casino and lost {} golds. ({:%m-%d-%Y %H:%M:%S})\n'.format(casino, datetime.datetime.now()))
        if toss == 1: #win
            session['gold'] += casino
            session['log'].append('Entered a casino and won {} golds! ({:%m-%d-%Y %H:%M:%S})\n'.format(casino, datetime.datetime.now()))

    return redirect('/')
@app.route('/restart', methods=['POST'])
def restart():
    session.pop('gold') #remove session['gold']
    session.pop('log') #remove session['log']
    session.pop('building') #remove session['building']
    return redirect('/')
app.run(debug=True)
