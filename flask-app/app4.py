from flask import Flask,render_template,url_for,redirect
from flask import request
import re

app=Flask(__name__)
#First we imported the Flask class. An instance/object of this class we created 

# we then use the route() decorator to the tell the flask what url should be strigger to call the function

def validate_password(password,confirmpass):
    # Define a regular expression pattern for the password
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:"<>?`\-=[\];\',./]).{,8}$')
    
    # Use the pattern to match the password
    if pattern.match(password):
        if password==confirmpass:             
             return True
        else:            
              return False
    else:
        return False


@app.route("/") # http://127.0.0.1:5000
def index():
       name="Anees"   
       return render_template('index.html',name=name)

@app.route("/contact") # http://127.0.0.1:5000
def contact():   
       return render_template('contact.html')


@app.route("/login",methods=['GET','POST']) 
def Login():
        if request.method=='POST':
                emailaddress=request.form.get("email")
                password=request.form.get("pass1")
                confirmpassword=request.form.get("pass2")
                res=validate_password(password,confirmpassword)
                if res:
                      return redirect(url_for("contact"))
                #       return f"Signup Success"
                else:
                      return f"Something went wrong"

                            
                
        return render_template('login.html')


app.run(debug=True)