from flask import Flask

app=Flask(__name__)
#First we imported the Flask class. An instance/object of this class we created 

# we then use the route() decorator to the tell the flask what url should be strigger to call the function
@app.route("/") # http://127.0.0.1:5000
def index():
    return "Welcome to the flask framework...."


@app.route("/contact") # http://127.0.0.1:5000/contact
def contact():
    return "contact page"


@app.route("/about") # http://127.0.0.1:5000/about
def about():
    return "about page"
    

@app.route("/user/<username>/<password>")
def showuser(username,password):
    print(type(username))
    return f'Hello {username} {password}'


@app.route("/posts/<int:id>")
def postuser(id):
    print(type(id))
    return f'Id {id}'


@app.route('/path/<path:subpath>')
def showpath(subpath):
    return f'hey {subpath}'



app.run(debug=True)