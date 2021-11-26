import pymysql

class DAO():

    def create(self, list):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user='root',
                        password='1234',
                        db='cloth',
                        charset='utf8')
        print('1. db연결 성공 >>', conn)

        cur = conn.cursor()
        print('2. db연결 스트림을 접근할수 있는 객체 획득 성공', cur)

        # sql = "insert into member values ('"+list[0]+"', '"+list[1]+"','"+list[2]+"','"+list[3]+"')"
        sql = "insert into member values (%s, %s, %s, %s)"
        result = cur.execute(sql, list)
        # cur.execute(sql)
        print('3. sql문 만들어 mqsql로 보내기 성공', result)

        conn.commit()
        conn.close()

    def update(self, list):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user='root',
                        password='1234',
                        db='cloth',
                        charset='utf8')
        print('1. db연결 성공 >>', conn)

        cur = conn.cursor()
        print('2. db연결 스트림을 접근할수 있는 객체 획득 성공', cur)

        # sql = "insert into member values ('"+list[0]+"', '"+list[1]+"','"+list[2]+"','"+list[3]+"')"
        # id 조건으로 pw, tel 수정
        sql = "update member SET (pw = %s, tel = %s) where id=%s"
        result = cur.execute(sql, list)
        print('3. sql문 만들어 mysql로 보내기 성공', result)

        conn.commit()
        conn.close()

    def read(self, id):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user='root',
                        password='1234',
                        db='cloth',
                        charset='utf8')
        print('1. db연결 성공 >>', conn)

        cur = conn.cursor()
        print('2. db연결 스트림을 접근할수 있는 객체 획득 성공', cur)

        # sql = "insert into member values ('"+list[0]+"', '"+list[1]+"','"+list[2]+"','"+list[3]+"')"
        # id만 받아와서 정보 출력
        sql = "select * from member where id=%s"
        result = cur.execute(sql, id)
        row = cur.fetchone()
        print(row)
        print('3. sql문 만들어 mysql로 보내기 성공', result)

        conn.commit()
        conn.close()
        return row #('apple','apple','apple','apple')

    def all(self):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user='root',
                        password='1234',
                        db='cloth',
                        charset='utf8')
        print('1. db연결 성공 >>', conn)

        cur = conn.cursor()
        print('2. db연결 스트림을 접근할수 있는 객체 획득 성공', cur)

        # sql = "insert into member values ('"+list[0]+"', '"+list[1]+"','"+list[2]+"','"+list[3]+"')"
        # id만 받아와서 정보 출력
        sql = "select * from member"
        result = cur.execute(sql)
        rows = cur.fetchall()
        print(len(rows))
        print('3. sql문 만들어 mysql로 보내기 성공', result)
        print(rows) #(('apple','apple','apple','apple'),('apple','apple','apple','apple'),('apple','apple','apple','apple')) 튜플들의 튜플

        conn.commit()
        conn.close()
        return rows #('apple','apple','apple','apple')


    def delete(self, list):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user='root',
                        password='1234',
                        db='cloth',
                        charset='utf8')
        print('1. db연결 성공 >>', conn)

        cur = conn.cursor()
        print('2. db연결 스트림을 접근할수 있는 객체 획득 성공', cur)

        # sql = "insert into member values ('"+list[0]+"', '"+list[1]+"','"+list[2]+"','"+list[3]+"')"
        sql = "delete from member where id=%s"
        result = cur.execute(sql, list)

        print('3. sql문 만들어 mqsql로 보내기 성공', result)

        conn.commit()
        conn.close()

if __name__ == '__main__':
    dao = DAO()
    dao.create(['apple','apple','apple','apple'])
#해당 모듈이 이 파일 안에서 실행할때만 이하 실행