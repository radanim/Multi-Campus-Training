#딕셔너리(dictionary) : 키와 값의 쌍으로 이루어진 데이터 / ,(콤마)로 구분
# { 키1:값1, 키2:값2, ...}

# 딕셔너리 생성 : {} or dict()
students = {1:'최선',2:'홍길동',3:'강감찬'}
print(students)
print(type(students))
print('------------------------------')

prof = {} #prof=dict()
print(prof)
prof[1]='이순신'
prof[2]='홍길동'
print(prof)
print(type(prof))
print('------------------------------')

print('students[1]:',students[1])
print('students: %s' % students)
print('------------------------------')

# ------------------------------------------------------

member = {'name':'홍길동','phone':'010-1234-1234'}
print(member)
print(member['name'])
print('------------------------------')

member1 = {'name':'홍길동','phone':'010-1234-1234','name':'이순신'}
# member['name']='이순신'
print(member1)
print('------------------------------')

naver = {'name':'naver','url':'www.naver.com','id':'codnjs3575'}
google = {'name':'google','url':'www.google.com','id':'codnjs3575'}
daum = {'name':'daum','url':'www.daum.net','id':'codnjs3575'}

print(naver['id'])
naver['id']='idValue'
print(naver['id'])
print('------------------------------')

# keys(),values(),items()
print('naver.keys():',naver.keys())
# print(type(naver.keys()))
#
# for key in naver.keys():
#     print(key)
to_list = list(naver.keys())
print('to_list:',to_list)
print('------------------------------')

print(naver.values())
# print(type(naver.values()))

# for values in naver.values():
#     print(values)
print('------------------------------')

print(naver.items()) #튜플 형태로 가져옴
# print(type(naver.items()))
#
# for items in naver.items():
#     print(items)

# key로 value 찾기
naver = {'name':'naver','url':'www.naver.com','id':'codnjs3575'}
google = {'name':'google','url':'www.google.com','id':'codnjs3575'}
daum = {'name':'daum','url':'www.daum.net','id':'codnjs3575'}

print('naver.get(name):',naver.get('name'))

# print(naver['passwd'])
print(naver.get('passwd','없음'))

key = 'passwd'

if naver.get(key) is None:
    print(key+'에 대한 값이 없습니다.')
print('---------------------------------------------------------')

# in / not in
print(key in naver)
print(key not in naver)
print('---------------------------------------------------------')

# 문제) 요리에 대한 정보를 딕셔너리에 저장, 음식정보들은 리스트로 구성
data1 = {'name':'버섯불고기','class':'한식','type':'불고기','ingr':['소고기','양파','간장','설탕']}
data2 = {'name':'카레덮밥','class':'양식','type':'덮밥','ingr':['카레','감자','양파','당근']}

datum = [data1,data2]

for data in datum:
    print('values:',data.values())
    print('keys:',data.keys())
    print('items:', data.items())
    print('-------------------------------------------------')
    for d in data:
        print(d)
        # print(datum[d])

































