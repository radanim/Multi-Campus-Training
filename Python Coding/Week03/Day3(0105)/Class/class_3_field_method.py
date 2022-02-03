# 필드 이용 메서드

class Car :
    model = ''

    def __init__(self,speed,color,model):
        self.speed = speed
        self.color = color
        self.model = model

    # 필드값을 반환하는 메서드
    def get_model(self):
        return self.model

    # 필드값을 변경하는 메서드
    def set_model(self,model):
        self.model = model

    def get_speed(self):
        return self.speed

    def set_speed(self,speed):
        self.speed = speed

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color=color

my_car = Car(0, 'red','audi')

print(my_car.get_model())
print(my_car.get_color())
print(my_car.get_speed())
print('-'*80)

my_car.set_model('벤츠')
my_car.set_color('black')
my_car.set_speed('40')

print(f"{my_car.get_model()}")
print(f"{my_car.get_color()}")
print(f"{my_car.get_speed()}")