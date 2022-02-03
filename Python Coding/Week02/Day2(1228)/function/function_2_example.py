# 반환값

# 문제) 사각형의 넓이 계산 함수 getArea()
# 매개변수(parameter): 가로(width), 세로(height)
def getArea(width,height):
    return (width * height)

# width = int(input('가로: '))
# height = int(input('세로: '))
# area = getArea(width,height)
# print(f'넓이 : {area}')
# ----------------------------------------------------------------------------

#반환값이 여러 개인 경우
def multi_return():
    return 1,2,3

# 1. 반환된 여러 개의 값을 하나의 변수에 받기
# result = multi_return()
# print(f'result: {result}')
# print(f'result[0]: {result[0]}')
# print(f'type: {type(result)}')
# print('----------------------')

# 2. 반환된 여러 개의 값을 여러 변수로 각각 받기
# a,b,c = multi_return()
# print('a: %s' % a)
# print('b: %s' % b)
# print('c: %s' % c)
# print('----------------------')

# return문이 여러개 사용할 경우
def multi_return():
    return 1 #첫번째 값만 반환
    return 2
    return 3

# result = multi_return()
# print(result) #
# print('----------------------')
# ----------------------------------------------------------------------------
# 문제) 상품 가격, 주문 수량을 입력받아서 주문액을 계산하여 반환하는 함수 출력
# 주문액이 10만원 이상이면 10%할인
# 주문액이 5만원 이상 10만원 미만이면 5%할인
# 주문액이 5만원 미만이면 할인 없음

price = int(input('상품 가격 입력: '))
qt = int(input('주문 수량 입력: '))

def order(price, qt=100):
    amount = price * qt
    if amount >= 100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    else :
        discount = 0
    result = amount - discount
    return amount,discount,result


amount,discount,result = order(price,qt)
# amount,discount,result = order(price)
print(f'주문액: {amount}원')
print(f'할인액: {discount}원')
print(f'지불액: {result}원')

# result = order()
# print(f'상품 가격: {result[0]}원 \n주문 수량: {result[1]}개 \n주문액: {result[2]}원')
# ----------------------------------------------------------------------------
# 리스트 반환
# 문제) 3명 이름을 입력 받아서 리스트에 저장하고 리스트를 반환하는 함수

def get_names():
    names = []
    for i in range(3):
        name = input('이름 입력: ')
        names.append(name)

    return names

# name_list = get_names()
# print(name_list)
# ----------------------------------------------------------------------------
# 이름과 나이를 입력받고 그 정보를 딕셔너리 형태로 반환

def info():
    name = input('이름: ')
    age = int(input('나이: '))
    return {'name':name,'age':age}

# info_dict = info()
# print(info_dict)
# print(type(info_dict))
# ----------------------------------------------------------------------------
# 함수 호출 시 반환값이 없는 경우
def hello():
    print('hello')

# result = hello()
# print(result) # None
# ----------------------------------------------------------------------------








