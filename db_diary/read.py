import db.dao2
id = input("id값을 입력 >> ")
if id:
    print(db.dao2.DAO.read(id))
else:
    rows = db.dao2.DAO.read_all()
    for row in rows:
        print(row)

#db.dao2.read_all()
