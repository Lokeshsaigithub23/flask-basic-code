from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    users=[
        {"id":1,"name":"lokesh","username":"lokesh23","email":"lokesh23@gmail.com"},
        {"id":2,"name":"sai","username":"sai23","email":"sai23gmail.com"},
    ] 
    return render_template('home.html',users=users)
if __name__=='__main__':
    app.run(debug=True)