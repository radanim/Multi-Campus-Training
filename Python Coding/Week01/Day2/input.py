# 입력 함수 : Input()
# 키보드로부터 값을 입력받아 처리하고 싶을 때

# name = input('이름: ') # input()은 str로 저장
# age = int(input('나이: '))

# print('이름은 %s이고, 나이는 %d입니다.' % (name,age))

'''
# 연습 문제 1. 두 정수를 입력받아 사칙연산 수행
print("두 정수를 입력받아 사칙연산 수행")
num1 = int(input('첫번째 숫자: '))
num2 = int(input('두번째 숫자: '))

print("")
print("두 숫자의 합 : " , num1 + num2)
print("두 숫자의 차 : " , num1 - num2)
print("두 숫자의 곱 : " , num1 * num2)
print("두 숫자의 나누기 : " , int(num1 / num2))
'''


'''
# 연습 문제 2.
kor = int(input('국어점수 입력 :'))
eng = int(input('영어점수 입력 :'))
math = int(input('수학점수 입력 :'))

sum = kor+eng+math
avg = sum/3

print("총점 : ", sum)
print("평균: ", avg)
print("평균 {:.2f}".format(avg))
'''

# 연습 문제 3. BMI 지수 계산
weight = float(input('몸무게(kg): '))
height = float(input('키(미터): '))
BMI = weight / (height * height)
# print("당신의 BMI는 %f 입니다." %BMI)
print("당신의 BMI는 {:.3f}입니다.".format(BMI))
print("당신의 BMI는", format(BMI,'.2f') , "입니다")