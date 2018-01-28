from flask import Flask, render_template, request, redirect, session, flash
#initialize the Flask application
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

# our index route will handle rendering our form
@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    if len(request.form['name']) < 1:
       flash("Name cannot be empty. Please try again!")
       return redirect('/')

    elif len(request.form['comment']) < 10:
       flash("Comment cannot be empty or less than 120 characters. Please try again!")
       return redirect('/')
    else:
        flash("Success! Your name is {}".format(request.form['name']))

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')
@app.route('/show')
def show():
    return render_template('result.html')
    return redirect('/')
@app.route("/back", methods=['POST'])
def goBack():
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True) # run our server
