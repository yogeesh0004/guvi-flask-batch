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


app.run(debug=True)