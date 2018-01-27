from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

# our index route will handle rendering our form
@app.route('/',methods=['GET']) # methods= ['Get'] (default)
def index():
  return render_template("index.html")
# this route will handle our form submission

@app.route('/process',methods=['POST'])
def processForm():
    if len(request.form['name']) < 1:
      flash("Name cannot be empty!") # just pass a string to the flash function
    elif request.form['comment'] == "":
      flash("Comment box cannot be empty!") # just pass a string to the flash function
    else:
      flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function
      return redirect('/')
    session['comment'] = request.form['comment']
    comment = countLetters(session['comment'])
    print comment
    if comment > 120:
        flash('Comment cannot be more than 120 words. Please try again!')
        return redirect('/')

    #return render_template("result.html",
    #     # name='Michael Choi',
    #     # location='San Jose',
    #     # language='Python!!!',
    #     # comment='Hi there :)')
    #


if __name__ == '__main__':
    app.run(debug=True) # run our server
