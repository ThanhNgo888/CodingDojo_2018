from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def basic():
    #request.method and request.form
    if request.method == 'POST':
        if request.form['name'] and request.form['password']:
            return 'Validation successful'
        else:
            return "Validation unsuccessful"
        return "Hi"
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True) # run our server


# GET requests:
# GET requests can be cached
# GET requests remain in the browser history
# GET requests can be bookmarked
# GET requests should never be used when dealing with sensitive data
# GET requests have length restrictions
# GET requests should be used only to retrieve data

# POST requests: Form
# POST requests are never cached
# POST requests do not remain in the browser history
# POST requests cannot be bookmarked
# POST requests have no restrictions on data length
