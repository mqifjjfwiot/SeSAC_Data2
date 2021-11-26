import db.dao2

id = input('수정할 id 검색 >> ')
title = input('수정할 title 입력 >> ')
content = input('수정할 content 입력 >> ')

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list타입으로 파라미터 주고받는거 추천
#list = [id, pw, name, tel]
vo = list()
vo.append(title)
vo.append(content)
vo.append(id)
print(vo)

db.dao2.DAO.update(vo)
