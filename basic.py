import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

app.app_context().push()

basedir=os.path.abspath(os.path.basename(__name__))
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False


print(app.config['SQLALCHEMY_DATABASE_URI'])

db=SQLAlchemy(app)




class detail(db.Model):
    __name__='detail'
    
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __repr__(self):
        return f"hello {self.name} your age is {self.age}"











