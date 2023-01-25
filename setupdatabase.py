from basic import db, detail


db.create_all()



sam=detail('sammy',25)
jak= detail('jacklin',23)

db.session.add_all([sam,jak])
db.session.commit()

print(sam.id)
print(jak.id)




