# 변수 이름(명명 규칙)
# 1. 대소문자 구분 : C언어 기반 (X와 x는 다름)
# 2. 영문자,숫자 혼용 가능하지만 숫자 먼저 사용 불가능
# 3. 공백 사용 불가능
#   snake 형태) std_name
#   camel 형태) stdName
# 4. 예약어 사용 불가능
#   import keyword
#   keyword.kwlist

# 변수에 값 저장
# 변수 = 값
a = 100
print("a:",a)
print("")

# 변수1, 변수2, 변수3 = 값1, 값2, 값3
A,B,C=11,22,33
print("A:",A)
print("B:",B)
print("C:",C)
print("")

# 변수1 = 변수2 = 변수3 = 값
x = y = z = 112233
print("x:",x)
print("y:",y)
print("z:",z)
print("")

# 두 변수의 값 교환
a,b=10,20
print("바뀌기 전, a:",a,"b:",b)
a,b = b,a
print("바뀌기 후, a:",a,"b:",b)
print("")

del a # 변수 제거

name = "김채원"
age = 23
addr = "서울시 노원구"

print("이름:",name,"나이:",age)
print(name + "은 " +addr + "에 살고 있습니다.")
print(name + "은 " +str(age) + "살입니다.") # 형변환
print("")

# ---------------------------------------------------------------
#문제 1. 자신의 이름과 나이를 변수에 저장한 후 print()을 이용하여 한 줄에 출력하시오.
name = "김채원"
age = 23
print("이름:",name,"나이:",age)
print("이름은 "+name+"이고, 나이는 "+str(age)+"살입니다.")
print("|n")
# 예시 1. print(f'{name} {age}')
# 예시 2. print("저의 이름은 {0}이고 저의 나이는 {1}입니다".format(name,age))
# 예시 3. print("이름: {}, 나이: {}".format(name,age))
# ---------------------------------------------------------------
#문제 2. 변수 선언 후 값 저장하고 출력하시오.
name = "김채원"
code = 2018100
year = 4
grade = "A"
avg = 93.5

# name, no, year, grade, avg = "김채원", 2018100, 4, "A", 93.5
print("성명 : ", name)
print("학번 : ", code)
print("학년 : ", year)
print("학점 : ", grade)
print("평균 : ", avg)
print("")
# 예시 1. for i, e in zip(["성명", "학번", "학년", "학점", "평균"], ["kim", "1", "1", "1", "1"]):
#     print(":".join([i, e]))
# 예시 2. print("성명 : " + name + "\n학번 : " + str(code) + "\n학년 : "  +str(year) + "\n학점 : " + grade+"\n펑균 : " + str(avg))
# 예시 3. print('성명 : %s' % name)
# ---------------------------------------------------------------

