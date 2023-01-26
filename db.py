from basic import Puppy, db



jak=Puppy('jackie',7)

db.session.add(jak)
db.session.commit()

all= Puppy.query.all()

print(all)

