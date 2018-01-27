from flask import Flask, render_template, redirect
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ItIsSecret"

#localhost:5000/
@app.route("/")#decorator
def index():#root route
    return render_template("index.html")
@app.route("/<color>")
def color(color):
    print color #show color choiced in the consoles
    return redirect('/')
# connect and store the connection in "mysql" note that you pass the database name to the function
# mysql = MySQLConnector(app, 'mydb')
# # an example of running a query
# print mysql.query_db("SELECT * FROM users")
if __name__ == "__main__":
    app.run(debug=True)
