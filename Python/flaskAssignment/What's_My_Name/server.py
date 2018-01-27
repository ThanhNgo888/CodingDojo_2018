from flask import Flask, render_template,request, redirect
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def users_login():
    print 'Got to post'
    name = request.form['name']
    return redirect('/')
@app.route('/process', methods=['POST'])
def show_user():
    name = request.form['name']
    render_template('process.html', name)

if __name__ == '__main__':
    app.run(debug=True) # run our server
