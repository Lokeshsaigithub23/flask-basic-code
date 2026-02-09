from flask import Flask 
app=Flask(__name__)
@app.route('/')
def home():
    return 'hello'

def about():
    return 'this is about'
app.add_url_rule("/about","hgh",about)

if __name__=='__main__':
    app.run(debug=True)