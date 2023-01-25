import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.basename(__name__))
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHELY_TRACK_MODIFICATOIIN']=False

db= SQLAlchemy(app)


class puppy(db.Model):
    __name__='puppies'
    
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Columb(db.Integer)
    
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __repr__(self):
        return f"your {self.name} is {self.age} years old"