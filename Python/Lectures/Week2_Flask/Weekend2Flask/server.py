from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")
def index():
    if 'users' not in session:
        session['users'] = []
    return render_template("index.html")
@app.route("/users/create", methods=['POST'])
def create():
    if 'users' not in session:
        session['users'] = []
    if request.form['name'] == "":
        return redirect("/")
    #print session['users']
    temp = session['users']
    temp.append({"name":request.form['name'], "email":request.form['email']})
    session['users'] = temp
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
