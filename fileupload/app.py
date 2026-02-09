from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
app=Flask(__name__)
@app.route("/upload")
def file_upload():
    return render_template("upload.html")
@app.route("/uploader",methods=["GET","POST"])
def file_uploaded():
    if request.method=='POST':
        file=request.files["file"]
        file.save(secure_filename(file.filename))
        return "file uploaded successfully"

if __name__=="__main__":
    app.run(debug=True)