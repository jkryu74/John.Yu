from flask import Flask, render_template, request, redirect, session
import random, datetime
# import time
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'data' not in session:
        session['data'] = ['']
    if 'pot' not in session:
        session['pot'] = 0
    else:
        print "idx.error"

    return render_template('index.html')
@app.route('/next', methods=['POST'])
def next():
    session['open'] = request.form['open']
    if session['open'] == 'house':
        house = random.randint(2, 6)
        session['pot'] += house
        session['data'].append('You have earned {} gold. ({:%Y-%m-%d %H:%M})'.format(house, datetime.datetime.now()))
    elif session['open'] == 'cave':
        cave = random.randint(10, 26)
        session['pot'] += cave
        session['data'].append("You have earned {} gold. ({:%Y-%m-%d %H:%M})".format(cave, datetime.datetime.now()))
    elif session['open'] == 'farm':
        farm = random.randint(5, 11)
        session['pot'] += farm
        session['data'].append("You have earned {} gold. ({:%Y-%m-%d %H:%M})".format(farm, datetime.datetime.now()))
    elif session['open'] == 'casino':
        flip = random.randint(0,2)
        casino = random.randint(-50, 51)
        if casino < 0: #lose
            session['pot'] += casino
            session['data'].append("Entered a Casino and lost {} gold. Ouch... ({:%Y-%m-%d %H:%M})".format(casino, datetime.datetime.now()))
        else: #win
            session['pot'] += casino
            session['data'].append("Entered a Casino and earned {} gold. ({:%Y-%m-%d %H:%M})".format(casino, datetime.datetime.now()))


    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session.pop('data')
    session.pop('pot')

    return redirect('/')
app.run(debug=True)
