# 연습문제 1. 정수 3개를 입력받아서 제일 큰 수를 출력하기
'''
num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))

if num1 > num2 :
    if num1 > num3 :
        max_num = num1
    else :
        max_num = num3
else :
    if num2 > num3 :
        max_num = num2
    else :
        max_num = num3

print('제일 큰 수 : %d' % max_num)
'''

# 예제
'''
if num1 > num2 and num1 > num3:
    print('제일 큰 수: %d' %num1)
elif num2 > num3:
    print('제일 큰 수: %d' %num2)
else:
    print('제일 큰 수: %d' %num3)
'''


# 연습문제 2. 도형을 선택해서 면적 구하기
choice = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : '))
if choice == 1 : #if choice == '1' 문자열로 비교하기
    width = int(input('가로 입력: '))
    height = int(input('세로 입력: '))
    area = width * height
    print('사각형의 면적 = %.2f' % area)
elif choice == 2 :
    width = int(input('밑변 입력: '))
    height = int(input('높이 입력: '))
    area = width * height / 2
    print('삼각형의 면적 = %.2f' % area)
elif choice == 3 :
    radius = int(input('반지름 입력: '))
    area = (radius**2) * 3.1416
    print('원의 면적 = %.2f' % area)
else :
    print('숫자를 잘못 입력하였습니다.')