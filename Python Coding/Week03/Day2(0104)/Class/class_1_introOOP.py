# 객체지향프로그래밍 (Objec Oriented Programming)
# 함수처럼 어떤 기능을 함수 코드에만 묶어두지 않고 객체에 기능을 정의하는 것
# 함수와 변수를 함께 가지고 있도록 구성
# 목적 = 코드의 재사용성

# 객체 : 함수(function) + 데이터(변수)
# 속성 : 객체가 가지고 있는 변수
# 동작 : 객체가 실제로 작동할 수 있는 함수. 메서드
# 예) tv_끄다/켜다/채널변경/기타

# String
str1 = 'I love you'
print(type(str1))
print(str1.split()) # split() : 메서드

# 클래스 : 객체를 만들어내는 틀
# 인스턴스 : 클래스로부터 생성된 객체, 실제로 생성되는 객체
# 클래스 => 메소드(함수) + 필드(변수)

# 계산기
# 1. 함수와 변수로 구성
result = 0

def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(7))
print(adder(10))

# 2. 계산기가 여러개 필요한 경우_ 함수/변수를 여러개 생성
result1 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

result2 = 0

def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(7))

print(adder2(3))
print(adder2(7))
print('-'* 80)
# 2. 계산기가 여러개 필요한 경우_ 클래스로 계산기 정의

class Calculator:
    # 초기값 설정 메소드
    def __init__(self):
            self.result = 0

    def adder_cls(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
print(type(cal1))
print(cal1.adder_cls(3))
print(cal1.adder_cls(5))
print(cal1.adder_cls(10)) # 누적







