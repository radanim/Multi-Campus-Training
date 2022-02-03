# in / not in
# 문자열 내에 특정한 문자열이 포함되어 있는지 확인
# 결과 : True / False
String = "Python programming"
result = 'on' in String

if 'on' in String:
    print("yes")
else :
    print("no")

print('----------------------------------------')
# 예제 1. in 활용
ID = input('ID 입력 : ')
id_Array = ['sun','kim','moon','sky']

if ID in id_Array:
    print('로그인 성공')
else :
    print('로그인 실패')