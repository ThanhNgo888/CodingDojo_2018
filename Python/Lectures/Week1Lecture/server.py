from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "ItIsSecret"

@app.route('/')#HomePage
def index():
    name = "Thanh"
    students = [
        {"first_name": "Kyle", "last_name": "Anthony"},
        {"first_name": "Chris", "last_name": "Buh"},
        {"first_name": "Nickolas", "last_name": "jimenez"},
        {"first_name": "Will", "last_name": "Fritz"},
    ]
    return render_template("index.html", x = name, all_students=students)
@app.route('/hello/<name>')
def hello(name):
    return "hello" + name

@app.route('/process', methods=['POST'])
def process():
    if request.form["action"] == 'register':
        pass
        #do some registration

    elif request.form['action'] =='login':
        #do some login
        session["name"] = request.form["first_name"]
        return redirect('/hello/' + session['name'])#/hello/<name>
if __name__ == "__main__":
    app.run(debug=True)
