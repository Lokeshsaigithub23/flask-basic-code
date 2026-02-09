from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,SearchField,DateField,SubmitField,IntegerField,RadioField,BooleanField,SelectField
app=Flask(__name__)
app.secret_key="your secertkey"
class MyForm(FlaskForm):
    username=StringField("username")
    password=PasswordField("password")
    email=StringField('email')
    bio=TextAreaField("bio")
    phone_number=IntegerField("phone number")
    gender=RadioField("gender",choices=[('male',"male"),('female',"female")])
    course=SelectField("course",choices=[("java","java"),("python","python"),("other","other")])
    birthdate=DateField("brithdate",format='%Y-%m-%d')
    subscribe=BooleanField("subscribe to news letter")
    submit=SubmitField("submit")

@app.route("/",methods=["GET","POST"])
def home():
    form=MyForm()
    if form.validate_on_submit():
        return "registeration successful"
    return render_template("index.html",form=form)

if __name__=="__main__":
    app.run(debug=True)    