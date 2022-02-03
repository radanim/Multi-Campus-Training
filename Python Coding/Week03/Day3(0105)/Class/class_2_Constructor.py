# 생성자(constructor)
# 목적) 1. 인스턴스 생성
# 목적) 2. 필드값을 초기화하는 함수

# 생성자를 정의할 때 : __init__(self):
# 생성자를 호출(사용)할 때 (인스턴스 생성) : 클래스이름과 같게 사용

# 생성자의 형식
# class class_name:
#     def __init__(self,*args): # *args : 여러개의 인수 받기
        # 이 부분에 필드 초기화 코드 입력

# 1. 기본 생성자 : 생성자에 self만 있고 다른 매개변수는 없는 경우
# class class_name:
#     def __init__(self):
#         pass
# ex)
class Car :
    def __init__(self):
        self.speed = 0
        self.color = 'red'

car1 = Car()
print(f"색상 : {car1.color}")
print(f"속도 : {car1.speed}")
print('-'*80)

# 2. 매개변수가 있는 생성자
# ex)
class Car1:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

mycar = Car1(10,'black') # 인수를 지정하지 않으면 TypeError 발생
print('isinstance(mycar,Car1): ',isinstance(mycar,Car1))
print(f"색상 : {mycar.color}")
print(f"속도 : {mycar.speed}")
print('-'*80)

# 3. defalut 매개변수 생성자 : def __init__(self,arg1=value1,arg2=value2):
class Car2:
    def __init__(self,color='red',speed=50):
        self.speed = speed
        self.color = color
mycar2 = Car2('black',100)
mycar3 = Car2('orange') #__init__(self,speed = 0,color='red')일 때는 속도에 들어감
yourcar = Car2()
print(f"my_car2) 색상 : {mycar2.color} / 속도 : {mycar2.speed}")
print(f"my_car3) 색상 : {mycar3.color} / 속도 : {mycar3.speed}")
print(f"your_car) 색상 : {yourcar.color} / 속도 : {yourcar.speed}")
print('-'*80)


class Car3:
    def __init__(self, color='red', speed=20):
        self.speed = speed
        self.color = color

    def Drive(self):
        self.speed = 50
    def Speed_up(self):
        self.speed += 10

my_car = Car3()
print(f'초기 속도 : {my_car.speed}')
my_car.Drive()
print(f'Drive 후 속도 : {my_car.speed}')
my_car.Speed_up()
print(f'Spped_up 후 속도 : {my_car.speed}')
print('-'*80)


# 1. self : 클래스에서 생성된 인스턴스에 접근 (인스턴스 자신)
#           인스턴스가 생성된 후 해당 인스턴스 이름으로 값을 할당하거나 메서드 호출

# 2. _ : 변수에 특별한 이름을 부여하지 않고 사용할 때
#   ex) for _ in range(10):
#       print('hi')

# 3. __ : 특수한 예약함수(메소드), 변수에 사용
#   ex) if __init == "__main__" :
