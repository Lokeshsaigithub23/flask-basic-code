from flask import Flask,render_template,redirect,url_for,request,session,flash
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
        user_exists=False
        for user in users:
            if username in user:
                user_exists=True
                if user[username]==password:
                    session.permanent=True
                    session['user']=username
                    flash("login successful",'info')
                    return redirect(url_for('home'))
                else:
                    flash("invalid details try again with correct details","info")
                    return 'invalid details '
        if not user_exists:
            flash("user does not exits","info")
            return 'user does not exits'
    elif 'user' in session:
        return redirect(url_for("home"))
    return render_template("login.html")


@app.route('/logout',methods=['POST'])
def logout():
    session.pop('user',None)
    flash("Logged out successfully", "info")
    return redirect(url_for('login'))
    

@app.route("/update_password_form",methods=['GET','POST'])                               
def update_password_form():
    return render_template("updatepassword.html") 

@app.route("/update_password/<username>", methods=["POST","PUT"])
def update_password(username):
    if request.method=='POST':
        if request.form.get("_method")=="PUT":
            new_password=request.form['new_password']
            user_exits=False
            for user in users:
                user_exits=True
                if username in user:
                    session.pop('user',None)
                    user[username]=new_password
                    flash("password updatesuccessfully","info")
                    return redirect(url_for("login"))
            if not user_exits:
                return "user does not exits"
        else:
            return 'invalid method'
    else:
        return 'invalid method'  

@app.route("/delete_user/<username>",methods=["POST","DELETE"])
def delete_user(username):
    if request.method=='POST':
        if request.form.get("_method")=="DELETE":
            user_exits=False
            for user in users:
                user_exits=True
                if username in user:
                    session.pop("user",None)
                    del user[username]
                    flash("user delete successfully")
                    return redirect(url_for("login"))
        else:
            return "invalid method"         
    else:
        return "invalid method"


if __name__=="__main__":
    app.run(debug=True)