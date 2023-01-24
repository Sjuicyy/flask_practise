from flask import Flask, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


app=Flask(__name__)

app.config['SECRET_KEY']='mykey'

class myform(FlaskForm):
    name=StringField('Enter your name:')
    submit=SubmitField('Click Me!!')


@app.route('/',methods=['GET','POST'])
def index():
    form=myform()
    
    
    if form.validate_on_submit():
        session['name']=form.name.data
        flash(' Your name is ')
        return redirect(url_for('index'))
    
    return render_template('index.html',form=form)







































# from flask import Flask, redirect, render_template, url_for , session, flash
# from flask_wtf import FlaskForm
# from wtforms import SubmitField, StringField



# app=Flask(__name__)

# app.config['SECRET_KEY']='mykey'

# class simpleForm(FlaskForm):
#     submit=SubmitField('click me')
    
    
# @app.route('/',methods=['GET','POST'])
# def index():
#     form=simpleForm()
    
#     if form.validate_on_submit():
#         flash('you just clicked the button')
        
#         return redirect(url_for('index'))
    
#     return render_template('index.html',form=form)