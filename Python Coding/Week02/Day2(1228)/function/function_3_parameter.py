# 함수의 매개변수

def getArea(width,height): #width -> 매개변수(parameter) : 함수로 전달되는 값을 받는 변수
    return width*height

# result= getArea(10,5) # (10,5) -> 인수(argument) : 함수 호출 시 함수에게 전달되는 값 (실제 인수)
# ----------------------------------------------------------------------------------
def get_avg(kor,eng,mat):
    return (kor+eng+mat)/3

# kor = int(input('국어점수 입력: '))
# eng = int(input('영어점수 입력: '))
# mat = int(input('수학점수 입력: '))
#
# avg = get_avg(kor,eng,mat)
# print(f'평균: {avg}')
# ----------------------------------------------------------------------------------
# 문제) 사칙연산 함수

def add(n1,n2):
    return (n1 + n2)
def sub(n1,n2):
    return (n1 - n2)
def mul(n1,n2):
    return (n1 * n2)
def div(n1,n2):
    return (n1 / n2)
def mod(n1,n2):
    return (n1 % n2)

add_num = add(9,3)
sub_num = sub(9,3)
mul_num = mul(9,3)
div_num = div(9,3)
mod_num = mod(9,3)

# print(f' 9 + 3 = {add_num}')
# print(f' 9 - 3 = {sub_num}')
# print(f' 9 * 3 = {mul_num}')
# print(f' 9 / 3 = {div_num}')
# print(f' 9 % 3 = {mod_num}')

print(f' 9 + 3 = {add(9,3)}')
print(f' 9 - 3 = {sub(9,3)}')
print(f' 9 * 3 = {mul(9,3)}')
print(f' 9 / 3 = {div(9,3)}')
print(f' 9 % 3 = {mod(9,3)}')


























