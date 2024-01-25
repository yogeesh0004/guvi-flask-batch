from flask import Flask,render_template

app=Flask(__name__)
#First we imported the Flask class. An instance/object of this class we created 

# we then use the route() decorator to the tell the flask what url should be strigger to call the function
@app.route("/") # http://127.0.0.1:5000
def index():
    return render_template('index.html')


@app.route("/contact") # http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')


@app.route("/about") # http://127.0.0.1:5000/contact
def about():
    return render_template('about.html')

@app.route("/login") # http://127.0.0.1:5000/contact
def login():
    return render_template('login.html')


app.run(debug=True)