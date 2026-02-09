from flask import Flask ,url_for ,redirect,json
app=Flask(__name__)
@app.route('/')
def home():
    return "this is home"
@app.route('/user/<string:user>')
def user_details(user):
    return f"user name is {user} "
@app.route('/id_details/<int:id>')
def user_id_details(id):
    return f"{id} is interger"
@app.route('/float_details/<float:float>')
def float_details(float):
    return f"{float} is float"
@app.route('/path_details/<path:path>')
def path_details(path):
    return f"subpath is {path}"
@app.route('/uuid_details/<uuid:uuid>')
def uuid_details(uuid):
    return f"uuid:{uuid}"
if __name__=='__main__':
    app.run(debug=True)