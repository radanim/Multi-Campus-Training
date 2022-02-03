# 클래스 상속과 메소드 재정의 연습
# 다형성 (polymorphism) : 같은 이름의 메서드가 다른 기능을 할 수 있도록 한 것

class Animal:
    age = 0
    leg = 4
    color = ''
    breed = ''

    def __init__(self,age,leg,color,breed):
        self.age = age
        self.leg = leg
        self.color = color
        self.breed = breed

    def talk(self):
        print('말한다.')
    def eat(self):
        print('먹는다.')
    def sleep(self):
        print('잔다.')

class Dog(Animal) :
    def __init__(self,name,age,leg,color,breed):
        super().__init__(age,leg,color,breed)
        self.name = name

    def talk(self):
        print(f'{self.name} : 멍멍')

    def eat(self):
        print(f'{self.name}가 간식을 먹는다 냠냠')

class Cat(Animal) :
    def __init__(self, name,age, leg, color, breed):
        super().__init__(age, leg, color, breed)
        self.name = name

    def talk(self):
        print(f'{self.name} : 야옹')

    def sleep(self):
        print(f'{self.name}는 잔다.')

my_dog = Dog('뽀삐',2,4,'white','말티즈')
my_cat = Cat('나비',1,4,'black','페르시안')

my_dog.talk()
my_cat.talk()
my_dog.eat()
my_cat.sleep()