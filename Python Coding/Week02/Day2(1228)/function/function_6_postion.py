# 위치 인수와 키워드 인수


def sum_num(a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print()
    return a+b+c


# 1. 위치 인수 (기본) : 위치에 의해 인수를 구별하는 방식
print('합계: ',sum_num(10,20,30))
print('---------------')

# 2. 키워드 인수 : 매개변수 이름(키워드)에 값을 할당

print('합계: ',sum_num(a=10 ,c=30, b=20))
print('---------------')
print('합계: ',sum_num(a=10, c=50, b=-10))
print('---------------')