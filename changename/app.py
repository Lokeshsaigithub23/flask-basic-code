from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/hello/<user>')
def home(user):
    return render_template("index.html",user="lokesh")
if __name__=="__main__":
    app.run(debug=True)