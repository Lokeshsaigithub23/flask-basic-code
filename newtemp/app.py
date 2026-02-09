from flask import Flask,render_template
app=Flask(__name__) 
@app.route('/')
def home():
    user={"username":"lokesh"}
    return render_template('home.html',user=user) 

@app.route('/hello/<users>')
def hello(users):
    return render_template('hello.html',name=users)
      
    
if __name__=='__main__':
    app.run(debug=True)
