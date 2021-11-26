import db.dao

id = input('id >> ')
pw = input('pw >> ')
tel = input('tel >> ')

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list타입으로 파라미터 주고받는거 추천
#list = [id, pw, name, tel]
# id 조건으로 pw, tel 수정
vo = list()
vo.append(id)
vo.append(pw)
vo.append(tel)

db.dao.update(vo)
