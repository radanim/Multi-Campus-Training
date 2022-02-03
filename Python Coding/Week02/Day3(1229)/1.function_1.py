# 1. 재귀호출 : 자기함수 호출
# 문제) 팩토리얼 계산----------------------------------------------------------------
# 방법 1
# def factorial(n):
#     fact = 1
#     for i in range(n,1,-1):
#         fact *= i
#     return fact
# 
# n = int(input('숫자 입력 :'))
# print(f'{n}!= {factorial(n)}')

# 방법 2
# fac(n) = n * fac(n-1)
# fac(n-1) = (n-1) * fac(n-2)

#--------------------------------------------------------------------------------
def self_call():
    pass

def count(num):
    if num >= 1:
        for i in range(num,0,-1):
            print(i,end=' ')
        print()
    else:
        print('양수를 입력하세요.')

def self_count(num):
    if num == 1:
        return print(1)
    else :
        print(num,end=" ")
        return self_count(num-1)
count(5)

self_count(5)
print('-'*80)
#--------------------------------------------------------------------------------
# 2. 내부 함수 : 함수 안에 있는 함수
# 함수가 정의된 그 범위에서만 사용

def out_func1(x,y):
    def in_func(a,b):
        return a+b
    return in_func(x,y)

print('out_func1(10,20) :',out_func1(10,20))
print()
#--------------------------------------------------------------------------------
# 3. 빌트인 함수/내장 함수 (built-in functions)
# 파이썬에 이미 만들어져 내장되어 있는 함수들
# 별도의 모듈은 import하지 않고 사용가능
# 함수의 형식과 목적에 따라 호출해서 사용
# ex. print(), input(), id(), type(), int(), str(), list(), sum(), len()

# 메소드(method) : 특정 객체를 통해 사용 가능한 함수
# ex. 리스트.index(), append(), insert(), count(), remove(), ... (내장 함수)
# ex. 문자열.index(), find(), sort(), reverse(), ...

# 참고사이트 : https://docs.python.org/ko/3/library/functions.html

# 1. abs() : 절댓값 함수, 양수로 만들어줌
print('01. abs()','-'*70)
print(abs(-10.5))
print()

# 2. all() : 모든 요소가 참이면 True
# False : 0, True: 0이 아닌 값
print('02. all()','-'*70)
print('all([1,2,3]) :',all([1,2,3]))
print('all([0,2,3]) :',all([0,2,3]))
print()
#iterable(반복 가능한 자료형) : 리스트, 튜플, 딕셔너리

# 3. any() : 하나라도 참이면 True
print('03. any()','-'*70)
print('any([1,2,3]) :',any([1,2,3]))
print('any([0,2,3]) :',any([0,2,3]))
print('any([0,0,0]) :',any([0,0,0]))
print('any([0,"",0]) :',any([0,"",0])) #빈 문자열 "" : False
print('any([0,"",[]]) :',any([0,"",[]])) #빈 리스트 [] : False
print()

# 4. bool() : 부울 값으로 변환, 비어있으면 False
print('04. bool()','-'*70)
print("bool("") :",bool(""))
print("bool([]) :",bool([]))
print("bool(1) :",bool(1))
print("bool(10) :",bool(10))
print("bool(-1) :",bool(-1))
print("bool({}) :",bool({}))
print("bool(None) :",bool(None))
print()

# 5. chr(아스키코드) : 아스키코드(ASCII) 값에 해당하는 문자 반환
print('05. chr()','-'*70)
print("chr(95) :",chr(95))
print("chr(97) :",chr(97))
print("chr(65) :",chr(65))
print("chr(55) :",chr(55))
print("chr(50) :",chr(50))
print("chr(48) :",chr(48))
print()

# 6. ord(문자열) : 문자에 대한 아스키코드(ASCII) 값 반환
print('06. ord()','-'*70)
print("ord(\"A\") :",ord("A"))
print("ord(' ') :",ord(' '))
print("ord(\"n\") :",ord('\n'))
print("ord(\"t\") :",ord('\t'))
print("ord(\"0\") :",ord('0'))
print()

# 7. divmod(a,b) : a를 b로 나눈 몫과 나머지 반환
print('07. divmod()','-'*70)
print('divmod(10,3) :',divmod(10,3)) #몫, 나머지
print()

# 8. enumerate() : 시퀀스를 인덱스값을 포함해서 enumerate
# 시퀀스 : range(), 문자열, 리스트, 튜플
print('08. enumerate()','-'*70)
print('enumerate(''hello'') :',enumerate('hello'))
for i,c in enumerate('hello'):
    print(f'{i} : {c}')
print()

for i, season in enumerate(['봄','여름','가을','겨울']):
    print(f'{i} : {season}')
print()

# 9. eval(표현식) : 표현식의 연산 결과 반환
print('09. eval()','-'*70)
print('eval(''1+2'') :',eval('1+2'))
print('eval(''10'') :',eval('10'))
print('type(eval(''10'')) :',type(eval('10')))
print()

# 10. filter(function, iterable) : iterable 자료의 요소들을 function으로 거르다(걸러내다)
print('10. filter()','-'*70)

def positive(x):
    return x > 0

print('filter :',filter(positive,[0,1,-1,10,-3,5])) #객체 생성
print('list(filter) :',list(filter(positive,[0,1,-1,10,-3,5])))
print()

def even(x):
    if x % 2 == 0:
        return x
print('filter :',filter(even,[0,1,-1,10,-3,5,-6])) #객체 생성
print('list(filter) :',list(filter(even,[0,1,-1,10,-3,5,-6])))
print()

# 11. help() : 도움말 보기
print('11. help())','-'*70)
help(print)
# help(filter)

# 12. pow(x,y) : x의 y제곱
print('12. pow()','-'*70)
print('pow(10,3) :',pow(10,3))
print('pow(2,10) :',pow(2,10))
print()

# 13. range([start],stop,[step]) : 지정한 범위의 값을 반복 가능한 객체로 반환
print('13. range()','-'*70)
print('range(0,5) :',range(0,5))
print('list(range(0,5)) :',list(range(0,5)))
print()

# -------------------------------------------------------------------------
# 14. map() : 리스트나 튜플, 문자열 등 반복가능한 구조의 요소별로 지정된 함수를 적용하여 처리
# 원본은 변경하지 않고 처리
# ex. list(map(함수,리스트))
# ex. tuple(map(함수,튜플))
print('14. map()','-'*70)

# -------------------------map() vs for문 ------------------------------
# 방법 1) map 이용
number1 = [3.5,3.4,2.0,4.6]
print('map() 이용 :',list(map(int,number1)))

# 방법 2) for 이용
number1 = [3.5,3.4,2.0,4.6]
for i in range(len(number1)):
    number1[i] = int(number1[i])
print('for 이용 :',number1)
# -----------------------map(),lambda() 사용--------------------------
num_list = [10,20,30]
#방법 1) map() 함수
def add10_var1(num):
    return num + 10

num2 = list(map(add10_var1,num_list))
print('list(map(add10_var1,num_list)) :',num2)

#방법 2) map() 함수 & 람다 함수 이용
num3 = list(map(lambda num : num + 5,num_list))
print('list(map(lambda num : num + 1),num_list) :',num3)
print()
# -------------------------------------------------------------------------

# # 15. zip(*iterable) : iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환
print('15. zip()','-'*70)
print('zip() :',zip([1,2,3],[4,5,6]))
print('list(zip()) :',list(zip([1,2,3],[4,5,6])))
print('list(zip()) :',list(zip([1,2,3],[4,5,6],[7,8,9])))

keys = ['apple','melon','banana']
vals = (250,300,400)

print("list(zip)",list(zip(keys,vals)))
print("dict(zip)",dict(zip(keys,vals)))

print()
#
# # 16.
# print('16. ()','-'*70)
# print()
# print()

print('-'*30,'람다 함수','-'*30)
#--------------------------------------------------------------------------------
# 4. 람다 함수 (lambda functions) : 함수를 한 줄로 간단하게 작성하고 생성

# 1) 람다 표현식을 변수에 할당하지 않고 그 자체로 실행
(lambda x:x+10)(25)

# 2) (lambda x : y=10; x+y)(5) #람다 표현식안에서 변수 생성 불가
# 2-1) 전역변수 사용 가능
y = 10
print('전역변수 사용 lambda :',(lambda x: x+y)(5))

# 3) 활용하기
def add(x,y):
    return x+y

print(f'add(10,20): {add(10,20)}')

add_lambda = lambda x,y : x + y
print(f'add_lambda(10,20): {add_lambda(10,20)}')

add_lambda_default = lambda x=10,y=10 : x + y #default 설정
print(f'add_lambda_default(): {add_lambda_default()}')
print('-'*30)

# 4) 문제_ 리스트의 각 요소에 10을 더하는 함수

num_list = [10,20,30]

# 4) 방법 1_ 함수 안에 for문
def add10(num_list):
    for i in range(len(num_list)):
        num_list[i] += 10

print('add10() 전 :',num_list)
add10(num_list)
print('add10() 후 :',num_list)
print('-'*30)

# 4) 방법 2_ 값 하나만 받는 함수 + for문
def add10_var1(num):
    return num + 10

print('반복문 전 :',num_list)
for i in range(len(num_list)):
    num_list[i] = add10_var1(num_list[i])
print('반복문 후 :',num_list)
print('-'*30)

# 4) 방법 3_ 람다함수
add10_lambda = lambda num : num + 10
print(f'add10_lambda(): {add10_lambda(10)}')

# 5) 문제 2_ 두 리스트의 각 자리수의 값을 합해서 새로운 리스트 생성
list1 = [1,2,3,4]
list2 = [10,20,30,40]

# 방법 1) def 함수 사용
# new_list = []
#
# def sum_lists(list1,list2):
#     for i in range(len(list1)):
#         new_list.append(list1[i] + list2[i])
#
# sum_lists(list1,list2)
# print(new_list)

# 방법 2) lambda 사용
new_list_lam = list(map(lambda x,y : x + y, list1,list2))
print(new_list_lam)




