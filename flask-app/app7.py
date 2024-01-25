from flask import Flask,render_template,redirect,url_for,session,request

app=Flask(__name__)
app.secret_key=b'%$^$^%^*&&**%$Anees234'



@app.route("/") 
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return "Welcome to the flask framework please login...."

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="POST":
        session['username']=request.form['username']
        return redirect(url_for('index'))
        
    return '''
     <form method="post">
      <p> <input type="text" name="username">
      <p> <input type="submit" value="login">
     </form>
'''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))



app.run(debug=True)