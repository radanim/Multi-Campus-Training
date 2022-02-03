class Dog :
    def __init__(self,Breed='',Size='Midium',Age = "2 years",Color = "Black"):
        self.__Breed = Breed
        self.Size = Size
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

dog1 = Dog("Neapolitan Mastiff","Large","5 years")
dog2 = Dog("Maltese","Small","2 years","White")
dog3 = Dog("Chow Chow","Large","3 years","Brown")


dog1_arr = dog1.get_Info()
dog2_arr = dog2.get_Info()
dog3_arr = dog3.get_Info()

print(dog1.get_Color())
print(dog2.get_Size())

dog3.set_Age('7 years')
print(dog3.get_Age())
print('-'*80)

dog1.Eat()
dog2.Sit()
dog3.Sleep()
dog1.Run()
print('-'*80)

print('dog2')
print(f'품종 : {dog2.get_Breed()}')
print(f'크기 : {dog2.get_Size()}')
print(f'나이 : {dog2.get_Age()}')
print(f'색상 : {dog2.get_Color()}')
print('-'*80)

dog1.print_Info()