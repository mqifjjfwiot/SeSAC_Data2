import db.dao as dao

id = input('검색할 id >> ')

row = dao.read(id)#지금 받아온 값은 튜플값 1개. 따로 쓸거면 이걸 row로 객체화 시킨후 쪼개면 된다
#모듈을 만들떄는 각자의 역할의 충실하도록 역할이 섞이면 안된다. 1개당 1개씩만.

print('결과는 '+row[0]+" "+row[1]+" "+row[2]+" "+row[3])