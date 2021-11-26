import db.dao2

title = input('title >> ')
content = input('content >> ')

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list타입으로 파라미터 주고받는거 추천
#list = [id, pw, name, tel]
vo = list()
vo.append(title)
vo.append(content)
print(vo)

db.dao2.DAO.create(vo)
