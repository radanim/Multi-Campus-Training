# 문자열에서 사용되는 연산 함수(메소드)들

email = "codnjs3575@naver.com"
str = 'programming'

# len() : 문자열 길이 반환
len_str = len(str)
print(len_str)
print("------------------------------------------------------")

# count() : 문자열 내에 들어있는 특정 문자(열)의 개수 반환
print('< count() >')
check_str = 'o'
count_str = str.count(check_str)
print('%s은 %d개' % (check_str,count_str))
print("------------------------------------------------------")

# .find(찾을문자[, start [,end] ]) : 문자열 내에서 특정 문자(열)이 존재하면
#                    문자열의 시작 위치를 반환하고, 존재하지 않으면 -1 반환
print('< .find() >')
find_str = email.find('naver')
find_str2 = email.find('naver',15)
find_str3 = email.find('@',5,11)
print(find_str) #찾으면 인덱스를 반환
print(find_str2) #없으면 -1 반환
print(find_str3)
print("------------------------------------------------------")

# .index(찾을문자[, start [,end] ]) : 문자열 내에서 특정 문자(열)의 시작 위치 반환
print('< .index() >')
index_str = email.index('naver')
index_str2 = email.index('3575')
index_str3 = email.index('@')
print(index_str) #찾으면 인덱스를 반환
print(index_str2) #없으면 -1 반환
print(index_str3)
print("------------------------------------------------------")
# 문제 1 : 도시명을 입력하고 해당 도시가 있는지 유무를 출력하기

cities = '인천 대구 대전 부산 울산 청주 춘천'
input_msg = input("도시명 입력: ")

# 방법 1 : in cities 사용
# if input_msg in cities :
#     print('%s, 해당하는 도시가 있습니다.' % input_msg)
# else :
#     print('해당하는 도시가 없습니다.')

# 방법 2 : find() 사용
# find_city = cities.find(input_msg)
# if find_city != -1 :
#     print('%s, 해당하는 도시가 있습니다.' % input_msg)
# else :
#     print('해당하는 도시가 없습니다.')

print("------------------------------------------------------")