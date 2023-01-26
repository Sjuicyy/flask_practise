import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.app_context().push()

basedir=os.path.abspath('')

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)



class Puppy(db.Model):
    
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Text)
    
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __repr__(self):
        return f'your {self.name} is {self.age} years old'