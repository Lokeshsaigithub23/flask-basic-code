from flask import Flask,url_for ,redirect
app=Flask(__name__)

def guest(guest):
    return f"welcome {guest} as guest"
app.add_url_rule("/guest/<guest>","guest",guest)

def admin():
    return 'this is admin'
app.add_url_rule("/admin","admin",admin)

def user(name):
    if name=='admin':
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("guest",guest=name))
app.add_url_rule("/user/<name>","user",user)    

if __name__=="__main__":
    app.run(debug=True)