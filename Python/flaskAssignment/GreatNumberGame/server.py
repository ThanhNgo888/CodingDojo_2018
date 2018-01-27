from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "mySecret"#must use for session

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
#allow the user to make a guess
@app.route('/guess', methods=['POST'])
def guess():
    #set the random Number
    if 'rand' not in session:
        session['rand'] = random.randrange(1,101)
    #print 'The random number is: ', session['rand']
    #print "The guess is: ", request.form['guess']
    guess = int(request.form['guess'])

    #validate the guess
    if guess < session ['rand']:
        session['guess'] = 'too_low'
    elif guess > session['rand']:
        session['guess'] = 'too_high'
    else:
        session['guess'] = 'correct'
    return redirect('/')

#reset/play again
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)#run our server
