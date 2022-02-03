# 함수(function) 정의

def show_info(name,age):
    print(f'나의 이름은 {name}이고 나이는 {age}입니다.')

# show_info('김채원',23)
# ---------------------------------------------------------
def welcome_msg(n):
    for i in range(n):
        print("welcome!")

# welcome_msg(2)
# ---------------------------------------------------------
# 두 개의 숫자를 입력받아서 합을 구하여 출력하는 함수 작성
# list1 = []
sum = 0
def sum_num():
    num1 = int(input('숫자 1 입력 : '))
    num2 = int(input('숫자 2 입력 : '))
    sum = num1 + num2
    print(f'{num1} + {num2} = {num1 + num2}')
    # list1 = [num1,num2,sum]
    # return list1
    return (sum)

# list1 = sum_num()
# print (list1)
print('합 :',sum_num())