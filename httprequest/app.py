from flask import Flask,render_template,redirect,url_for,request
app=Flask(__name__)
users={"sai":"sai@2349"}
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if users[username]==password:
            return redirect(url_for('home'))
        else:
            return 'invalid details try again with correct details'
    return render_template('login.html')

@app.route("/logout",methods=['POST','GET'])
def logout():
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)