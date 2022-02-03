# 상속관계와 포함관계

# 1. 상속관계 (is-a)
# 상속 - 부모 클래스
# class person :
#     def __init__(self,name):
#         self.name = name
#
#     def greeting(self):
#         print('hi')
#
# # 상속 = 자식 클래스
# class Student(person):
#     def study(self):
#         print('Studing')


# 2. 포함관계(has-a)
# append를 통해 포함
class person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('hi')

    def __repr__(self):
       return self.name

class Person_list:
    def __init__(self):
        self.person_list = []

    def append_person(self,person):
        self.person_list.append(person)

    def printInfo(self):
        for p in self.person_list:
            print(p)

person_list = Person_list()
name_list = ['kim','lee','choi']

for i in range(3):
    p = person(name_list[i])
    # print(p)
    person_list.append_person(p)

person_list.printInfo()












