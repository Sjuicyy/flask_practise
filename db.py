from basic import db, Puppy


data=Puppy.query.all()
print(data)

data= Puppy.query.get(1)
print(data.name)

data = Puppy.query.filter_by(name='jackie')
print(data.all())

data=Puppy.query.get(1)
data.name='asline'
db.session.add(data)
db.session.commit()

data=Puppy.query.get(1)
print(data.name)

data= Puppy.query.all()
print(data)

data=Puppy.query.get(3)
db.session.delete(data)
db.session.commit()