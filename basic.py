import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.app_context().push()

basedir=os.path.abspath('')

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

db=SQLAlchemy(app)

class Students(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    address=db.Column(db.Text)
    
    
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        
        
    def __repr__(self):
        return f" Hello {self.name} your age is {self.age} and your address is  {self.address} "
    
    