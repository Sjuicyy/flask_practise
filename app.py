from flask import Flask, redirect, render_template, url_for , session, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField



app=Flask(__name__)

app.config['SECRET_KEY']='mykey'

class simpleForm(FlaskForm):
    submit=SubmitField('click me')
    
    
@app.route('/',methods=['GET','POST'])
def index():
    form=simpleForm()
    
    if form.validate_on_submit():
        flash('you just clicked the button')
        
        return redirect(url_for('index'))
    
    return render_template('index.html',form=form)