from flask import Flask,render_template,redirect,url_for,request,session
from datetime import timedelta
app=Flask(__name__)
app.secret_key="your secret key"
app.permanent_session_lifetime=timedelta(minutes=5)
users=[{"lokesh":"lokesh2349@"},{"sai":"sai@2349"},{'ps230':"ps23@230"}]
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user_exits=False
        for user in users:
            if username in user:
                user_exits=True
                if user[username]==password:
                    session.permanent=True
                    session['user']=username
                    return redirect(url_for('home'))
                else:
                    return 'invalid details try again'
        if not user_exits:
            return 'user does not exists'
    elif 'user' in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route('/logout',methods=['POST'])
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))                                

if __name__=="__main__":
    app.run(debug=True)