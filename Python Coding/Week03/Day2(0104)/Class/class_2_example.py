
# A. 클래스 구현 과정
# 1단계 : 클래스 정의(선언)
    # class 클래스명:
    #   def __init__(self):
    #       self.필드명1(변수명) = 초기값
    #       self.필드명2(변수명) = 초기값
    #
    #   def 메소드명1(self,매개변수1,...): #함수정의와 동일
    #       return 필드명(변수명)
    

# 2단계 : 객체 생성(인스턴스 생성)(변수 선언과 비슷)
    # 형식) 객체변수이름 = 클래스명()


# 3단계 : 객체 사용(메소드 사용/필드값 변경/필드값 사용)
    # 변수나 함수와 다르게 구별하기 위해서 
    # 객체이름.변수명 
    # 객체이름.메소드명

# 자동차 클래스 => 메소드 + 필드
# 기능(동작) : speed_up(),speed_down() => 메소드(함수)
# 속성(상태) : color, speed => 필드(변수)

# 1. 클래스 선언
# 클래스이름 : 식별자 규칙에 따라 정의, 대문자로 시작하는 것이 관례
class Car :
    def __init__(self) :
        self.color = 'red'
        self.speed = 0

    def speed_up(self,num) :
        self.speed += num
        return self.speed,self.color

    def speed_down(self,num) :
        self.speed -= num
        return self.speed,self.color

# 2. 객체 생성(인스턴스 생성)
my_car = Car()
your_car = Car()

# 3. 객체 사용(인스턴스 사용)
print(my_car.color)
my_car.color = 'black'
print(my_car.color)

my_car.speed_up(5)
my_car.speed_down(5)

your_car.speed_up(5)
your_car.speed_down(5)

print('-------------------------------------------------------------------')
# # 1. 클래스를 만들어 놓기만 함
# class Car2 :
#     def speed_up(self) :
#         pass
#     def speed_down(self) :
#         pass
#
# # 2. 객체 생성(인스턴스 생성)
# my_car = Car2()
# your_car = Car2()
#
# # 3. 인스턴스 생성 후 값 추가
# print(my_car.color)
# my_car.color = 'black'
# my_car.speed = 0
# print(my_car.color)
#
# print('-------------------------------------------------------------------')
# # 클래스를 만들어 놓기만 함
class Car3 :
    color = ''
    speed = 0

    def speed_up(self) :
        self.speed += 10
    def speed_down(self) :
        self.speed -= 10
# self : 인스턴스가 사용하는 것(자신) / 기존 함수와 구분

# 2. 객체 생성(인스턴스 생성)
my_car = Car3()
your_car = Car3()

# 3. 인스턴스 생성 후 값 추가
my_car.speed_up() # 메서드 호출
print(my_car.speed)

my_car.speed_up()
print(my_car.speed)

my_car.speed_down()
print(my_car.speed)










