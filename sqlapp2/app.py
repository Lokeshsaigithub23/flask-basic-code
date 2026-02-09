from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mssql+pyodbc://sa:lokeshsai2349@DESKTOP-GPJC32R\\SQLEXPRESS/sqlapp?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
app.app_context().push()
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(100))
    date_joined=db.Column(db.Date,default=datetime.utcnow)
    
if __name__=="__main__":   # help in runing code#
    app.run(debug=True)
    