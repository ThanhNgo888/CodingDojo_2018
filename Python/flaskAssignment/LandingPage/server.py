from flask import Flask, render_template
app = Flask(__name__)

#rendering to index file(GET method)
@app.route('/')
def index():
    return render_template("index.html", greeting="Welcome to Ninjas Land")

#rendering to ninjas file(GET method)
@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

#this route will handle our form submission
@app.route('/dojos')
def create_Ninja():
    print "Got Post Info"
    return render_template("dojos.html")
app.run(debug=True)
