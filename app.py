from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,RadioField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired


app=Flask(__name__)

app.config['SECRET_KEY']='mykey'

class infoform(FlaskForm):
    name=StringField("enter your name", validators=[DataRequired()])
    netured=BooleanField('are you netured??')
    mood = RadioField('please choose your mood', choices=[('mood1','good'),('mood2','better'),('mood3','best')])
    food_choice=SelectField('pick your fav food',choices=[('chi','chicken'),('mtn','mutton'),('bf','beef')])
    feedback=TextAreaField('any additional text')
    submit=SubmitField('Sumbit')
    
    
@app.route('/',methods=['GET','POST'])
def index():
    form=infoform()
    
    
    if form.validate_on_submit():
        session['name']=form.name.data
        session['netured']=form.netured.data
        session['mood']=form.mood.data
        session['food_choice']=form.food_choice.data
        session['feedback']=form.feedback.data
        
        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)


@app.route('/thank')
def thankyou():
    return render_template('thankyou.html')