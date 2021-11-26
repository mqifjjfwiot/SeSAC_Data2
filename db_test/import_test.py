from db_test.out_module import call

call(name = '홍길동') # 나이 입력안함. 디폴트값 100
call(name = '저글링', age = 200) # 나이 파라미터까지 지정. 200
call('홍길동', 2000) # 두번째 파라미터=나이=2000