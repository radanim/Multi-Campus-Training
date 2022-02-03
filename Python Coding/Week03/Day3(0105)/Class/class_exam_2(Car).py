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


my_car = Car('123',10)
print(f'초기 속도 : {my_car.speed}')

my_car.Drive()
print(f'Drive 후 속도 : {my_car.speed}')

my_car.Speed_up(30)
print(f'Speed_up 후 속도 : {my_car.speed}')

my_car.Speed_down(20)
print(f'Speed_up 후 속도 : {my_car.speed}')

my_car.Speed_up(130)
print(f'Speed_up 후 속도 : {my_car.speed}')

my_car.Speed_up(130)
print(f'Speed_up 후 속도 : {my_car.speed}')

my_car.Speed_down(60)
print(f'Speed_up 후 속도 : {my_car.speed}')

print('-'*80)