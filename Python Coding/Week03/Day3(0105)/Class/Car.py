class Car :
    def __init__(self,model_no,speed=0,color='white'):
        self.model_no = model_no
        self.speed = speed
        self.__color = color

    def set_color(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    def __modelNo(self):
        print(self.model_no)

    def print_ModelNo(self):
        self.__modelNo()
        print(self.get_color())

    def Drive(self):
        self.speed = 50

    def Speed_up(self,num=10):
        if (self.speed + num) >= 140:
            print('과속입니다.\n')
            return self.speed
        else: self.speed += num

    def Speed_down(self,num=10):
        if (self.speed - num) > 0 :
            self.speed -= num
        else :
            self.speed = 0
            print('정지했습니다.')

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