from flask import Flask, request, render_template,session,redirect
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/', methods=['GET','POST'])
def index():
    if 'count' not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template ("index.html")

@app.route('/count', methods=['POST'])
def displayCount():
    if 'count' not in session:
        session["count"] = 0
    session["count"] = 1
    return redirect('/')

@app.route('/ninja', methods=['POST'])
def ninja():
    session['ninja'] = request.form['ninja']
    if 'count' not in session:
        session["count"] = 0
    session["count"] += 1
    return redirect('/')

@app.route('/hackers', methods=['POST'])
def hackers():
    session['hackers'] = request.form['hackers']
    session["count"] = 0
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True) # run our server
