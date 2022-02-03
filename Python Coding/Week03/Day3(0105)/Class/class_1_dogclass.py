class Dog :
    def __init__(self):
        self.Breed = ""
        self.Size = "Midium"
        self.Age = "2 years"
        self.Color = "Black"

    def Eat(self):
        pass
    def Sleep(self):
        pass
    def Sit(self):
        pass
    def Run(self):
        pass

dog1 = Dog
dog2 = Dog
dog3 = Dog

dog1.Breed = "Neapolitan Mastiff"
dog1.Size = 'Large'
dog1.Age = '5 years'

dog2.Breed = "Maltese"
dog2.Size = "Small"
dog2.Color = "White"

dog3.Breed = "Chow Chow"
dog3.Age = "3 years"
dog3.Color = "Brown"

print(f'{dog1.Breed} / {dog1.Age} / {dog1.Size} / {dog1.Color}')
print(f'{dog2.Breed} / {dog2.Age} / {dog2.Size} / {dog2.Color}')
print(f'{dog3.Breed} / {dog3.Age} / {dog3.Size} / {dog3.Color}')