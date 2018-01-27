from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)

# our index route will handle rendering our form
@app.route('/',methods=['GET']) # methods= ['Get'] (default)
def index():
  return render_template("index.html")
# this route will handle our form submission

@app.route('/submitForm',methods=['POST'])
def submitForm():
    return render_template("result.html",
        name='Michael Choi',
        location='San Jose',
        language='Python!!!',
        comment='Hi there :)')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) # run our server
