from flask import Flask, render_template, session, url_for, redirect,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app=Flask(__name__)

app.config['SECRET_KEY']='mykey'

class myform(FlaskForm):
    name=StringField("what is your name??")
    submit=SubmitField('submit')
    
@app.route('/',methods=['GET','POST'])
def index():
    form=myform()
    
    if form.validate_on_submit():
        session['name']=form.name.data
        flash(f"your text is {session['name']}")
        
        return redirect(url_for('index'))
    return render_template('index.html',form=form)
