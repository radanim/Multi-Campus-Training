# 문자열에서 사용되는 연산 함수(메소드)들 (2)

email = "codnjs3575@naver.com"
str = 'programming'
cities = '인천 대구 대전 부산 울산 청주 춘천'
name = '성춘향;변학도;이몽룡;방자'

# 문자열 분리 메소드
# split() : 구분자(공백, 세미콜론, 콜론, 콤마, ...)를 기준으로 문자열 반환

city = cities.split(" ")
for i in range(len(city)):
    print('%d번째 도시 : %s' % (i+1, city[i]))

print('----------------------------------')

name_Array = name.split(";")
print(name_Array)

# 문제) 생년월일은 입력하고 연도, 월, 일 구분
input_msg = input('생년월일(연/월/일) : ')
birth = input_msg.split('/')

year = birth[0]
month = birth[1]
day = birth[2]

# print 방법 1
# print('당신은 %s년에 태어났고, ' % year)
# print('생일은 %s월 %s일이군요.' % (month,day))

# print 방법 2
# print('당신은 %s년에 태어났고, \n생일은 %s월 %s일이군요' % (year,month,day))

# print 방법 3
print(f'당신은 {year}년에 태어났고, \n생일은 {month}월 {day}일이군요.')
print('----------------------------------')

