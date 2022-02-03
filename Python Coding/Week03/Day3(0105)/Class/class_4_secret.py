# 비공개 필드/메소드 생성 및 이용

# 비공개 필드 : 필드를 외부에서 직접 사용하지 못하도록 하는 방법
#            클래스 내부에서만 사용가능
# 형식 : __ 필드명

# 비공개 메소드 : 외부에서 직접 사용하지 못하고 클래스 내부에서만 접근
# 형식 : def __메소드명(self,*args)
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

my_car = Car('1234')
# print(car1.color) # __때문에 에러 발생

# 비공개 필드를 접근하려면 필드를 이용하는 메소드를 정의하여 호출해야 함
print('수정 전,',my_car.get_color())
my_car.set_color('black')
print('수정 후,',my_car.get_color())

# 비공개 메소드 접근
my_car.print_ModelNo() #메소드를 호출해서 클래스 안에서 호출하게끔 사용



















