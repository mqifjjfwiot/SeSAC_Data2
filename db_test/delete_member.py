import db.dao

id = input('id >> ')


# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list타입으로 파라미터 주고받는거 추천
# list = [id, pw, name, tel]
# id 기준으로 데이터 삭제
vo = list()
vo.append(id)


db.dao.DAO.delete(vo)
