from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms import StringField,PasswordField,TextAreaField,SearchField,DateField,SubmitField,IntegerField,RadioField,BooleanField,SelectField
app=Flask(__name__)
app.secret_key="your secertkey"
class MyForm(FlaskForm):
    username=StringField("username",validators=[DataRequired(message="please enter name")])
    password=PasswordField("password",validators=[DataRequired(message="please enter password")])
    email=StringField('email',validators=[DataRequired(message="please enter email"),Email(message="invlaid email")])
    bio=TextAreaField("bio")
    phone_number=StringField("phone number")
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