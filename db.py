from basic import db ,Puppy


asl=Puppy('ashlin',5)
jak=Puppy('jackie',7)
wol=Puppy('wolverine',4)
pet=Puppy('pettie',5)

db.session.add_all([asl,jak,wol,pet])
db.session.commit()