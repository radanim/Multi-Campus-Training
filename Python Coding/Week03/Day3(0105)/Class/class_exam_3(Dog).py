class Dog :
    def __init__(self,Breed='',Size=1,Age = 2,Color = "Black"):
        self.__Breed = Breed
        self.Size = Size #1 = Large, 2 = Midium, 3 = Small
        self.Age = Age
        self.Color = Color

    def Eat(self):
        print('먹다')
    def Sleep(self):
        print('잠자기')
    def Sit(self):
        print('앉다')
    def Run(self):
        print('뛰다')

    def get_Breed(self):
        return self.__Breed
    def set_Breed(self,Breed):
        self.__Breed = Breed

    def get_Size(self):
        return self.Size
    def set_Size(self, Size):
        self.Size = Size

    def get_Age(self):
        return self.Age
    def set_Age(self, Age):
        self.Age = Age

    def get_Color(self):
        return self.Color
    def set_Color(self, Color):
        self.Color = Color

    def get_Info(self):
        return self.__Breed, self.Size, self.Age, self.Color

    def print_Info(self):
        print(f'품종 : {self.__Breed}')
        print(f'크기 : {self.Size}')
        print(f'나이 : {self.Age}')
        print(f'색상 : {self.Color}')

    def __gt__(self, other):
        return self.Size > other.Size

    def __ge__(self, other):
        return self.Size >= other.Size

    def __lt__(self, other):
        return self.Size < other.Size

    def __le__(self, other):
        return self.Size <= other.Size

    def __eq__(self, other):
        return self.Size == other.Size

    def __ne__(self, other):
        return self.Size != other.Size

    def __add__(self, other):
        return self.Age + other.Age

    def __sub__(self, other):
        return self.Age - other.Age

    def __mul__(self, other):
        return self.Age * other.Age

    # def __divmod__(self, other):
    #     return divmod(self.Age,other.Age)

    def __divmod__(self, other):
        return self.get_age() // other.get_age(), self.get_age() % other.get_age()


dog1 = Dog("Neapolitan Mastiff",1,6 )
dog2 = Dog("Maltese",3,2,"White")
dog3 = Dog("Chow Chow",2,3,"Brown")


# 객체 간의 크기를 비교하기
if dog1 > dog2 :
    print('dog1이 크다')
elif dog1 == dog2 :
    print('dog1와 dog2의 크기는 같다')
else :
    print('dog2가 dog1보다 크네요')

print('-'*50)

# 객체 간의 나이를 더하고, 빼고, 곱하고, 나누기
print(f' dog1 + dog2 : {dog1 + dog2}')
print(f' dog3 - dog2 : {dog3 - dog2}')
print(f' dog1 * dog2 : {dog1 * dog2}')
print(f' dog1 / dog3 : {divmod(dog1,dog3)}')