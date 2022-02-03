# 가변길이 매개변수 : *args, **kwargs
# 1. 매개변수의 개수가 정해져 있지 않은 경우
# 2. 여러 개의 값을 전달받아 사용할 경우
# *args : arguments의 약자, 인수 값을 받음
# **kwargs : keyword arguments의 약자, key = value의 형태

# 1. *args----------------------------------------------
# 예시 1) 여러 개 인수의 값을 더하는 함수
def sum_num(*args):
    sum = 0
    for num in args:
        sum += num
    # print(f'합계: {sum}')
    return sum

print("합계:",sum_num(1,2,3))
print("합계:",sum_num(1,2,3,4,5))
print("합계:",sum_num(1,2,3,4,1,5,6,7,10))
print('--------------------------------')

# 예시 2) *매개변수 형식을 사용하여 이름 인수
def show_name(*args): # *names
    for name in args:
        print(name,end=" ")
        # result += name + " "
    print()

show_name('홍길동','강감찬')
show_name('홍길동','강감찬','유관순','이순신')
print('--------------------------------')

# ------------------------------------------------------
# 2. **kwargs-------------------------------------------
# 예시
def show_info(**kwargs):
    print('key:', end=' ')
    for key in kwargs.keys():
        print(key, end=" / ")
    print()

    print('val:',end=' ')
    for val in kwargs.values():
        print(val, end = " / ")
    print()

    print('item:', end=' ')
    for item in kwargs.items():
        print(item, end=" / ")
    print()
    print()

show_info(name="홍길동",id="123",phone='010-111-111',address='서울시 서초구 삼성동')
show_info(name="sun",id="moon")
print('--------------------------------')
