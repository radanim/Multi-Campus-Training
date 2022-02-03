# 인스턴스(instance)(변수) : 필드

# 클래스 변수 : 여러 인스턴스가 공유할 수 있는 변수
class Car :
    color = ''
    speed = 10
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1 # 클래스 변수 # 인스턴스가 생성될 때마다 count 1 증가
        print(f'자동차 총 생산량 : {Car.count}')

car1 = Car()
# print(f"car1.count : {car1.count}") #1
# print(f"Car.count : {Car.count}") #1

car2 = Car()
# print(f"car1.count : {car1.count}") #2
# print(f"car2.count : {car2.count}") #2
# print(f"Car.count : {Car.count}") #2










