from flask import Flask, request, render_template,session,redirect
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/', methods=['GET','POST'])
def index():
    return render_template ("index.html")
@app.route('/users', methods=['POST'])
def create_user():
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!
@app.route('/show')
def show_user():
    return render_template('counter.html')

  counter = 1
  counter +=1
  return str(counter)


if __name__ == '__main__':
    app.run(debug=True) # run our server
