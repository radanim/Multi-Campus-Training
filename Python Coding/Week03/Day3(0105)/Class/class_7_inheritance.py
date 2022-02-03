# 상속(inheritance)
# 부모 클래스 (super class) : 상속을 해주는 클래스
# 자식 클래스 (sub class)

# 자동차 클래스

# 부모 클래스
class Car:
    speed = 0
    color = ''
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}의 속도로 주행합니다.')

# 자식 클래스
class Truck(Car):
    def __init__(self,speed,color,load):
        super().__init__(speed,color) # 부모 클래스의 값을 그대로 가져옴
        self.load = load

class Vehicle(Car):
    def __init__(self,speed,color,seat):
        super().__init__(speed,color)
        self.seat = seat

    def drive(self): #메소드 재정의(오버라이딩) # 다시 정의 가능
        print(f'좌석 수 : {self.seat}')

truck1 = Truck(10,'red',1000)
truck1.drive()

Vhc1 = Vehicle(30,'black',5)
Vhc1.drive()

