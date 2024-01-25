from flask import Flask,make_response,url_for,redirect,render_template,request,abort

app=Flask(__name__)

@app.route("/") 
def index():  
    response=make_response(render_template("cookie.html"))
    response.set_cookie('Username',"rohan")
    response.set_cookie('Password',"abc1345")
    uname=request.cookies.get('Username')
    password=request.cookies.get('Password')
    print(uname,password)
    return response



@app.route("/login")  
def login():
    abort(400)
    return render_template("login.html")



@app.route("/test/")  
def test():
    return redirect(url_for('login'))




@app.errorhandler(400)
def bad_page(error):
    return render_template('error-400.html'),400


@app.errorhandler(401)
def unauthorised_page(error):
    return render_template('error-401.html'),401


@app.errorhandler(404)
def not_found_page(error):
    return render_template('error-404.html'),404


app.run(debug=True)