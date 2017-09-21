from flask import Flask, render_template, session, request, url_for, redirect
import random, datetime

app = Flask(__name__)
app.secret_key = "HelloWorld"

@app.route('/')
def index():

    if 'now' not in session:
        session['now'] = datetime.datetime.now()
    if 'message' not in session:
        session['message'] = ''
    if 'activity' not in session:
        session['activity'] = []
    else:
        session['activity'].append(session['message'])
    if 'goldcount' not in session:
        session['goldcount'] = 0
    if 'change' not in session:
        session['change'] = 0
    session['goldcount'] += session['change']
    return render_template('index.html')

@app.route('/process_gold',methods=['POST'])
def process_gold():
    if request.form['action'] == 'house':
        session['change'] = random.randint(5,10)
        session['message'] = "Earned "+str(session['change'])+ " golds from "+request.form['action'] + " "+str(session['now'].strftime("%Y-%m-%d %H:%M"))
    elif request.form['action'] == 'farm':
        session['change'] = random.randint(10,15)
        session['message'] = "Earned "+str(session['change'])+ " golds from "+request.form['action'] + " "+str(session['now'].strftime("%Y-%m-%d %H:%M"))
    elif request.form['action'] == 'cave':
        session['change'] = random.randint(2,5)
        session['message'] = "Earned "+str(session['change'])+ " golds from "+request.form['action'] + " "+str(session['now'].strftime("%Y-%m-%d %H:%M"))
    elif request.form['action'] == 'casino':
        session['change'] = random.randint(-50,50)
        if session['change'] < 0:
            session['message'] = "Lost "+str(abs(session['change']))+ " golds from "+request.form['action'] + " "+str(session['now'].strftime("%Y-%m-%d %H:%M"))
        else:
            session['message'] = "Earned "+str(session['change'])+ " golds from "+request.form['action'] + " "+str(session['now'].strftime("%Y-%m-%d %H:%M"))

    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.pop('goldcount')
    session.pop('message')
    session.pop('change')

    return redirect('/')
app.run(debug=True)
