class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greeting(self):
        print("안녕하세요")

class University :
    def __init__(self,department=' ',grade=' '):
        self.department = department
        self.grade = grade

    def manage_score(self):
        print("학점관리")

class undergraduate(Person,University):
    def study(self):
        print("공부하기")

# Kim = undergraduate()
# Kim.name = 'kim'
# Kim.age = 20
# Kim.greeting()
# Kim.manage_score()
# Kim.study()

class A:
    def greeting(self):
        print("안녕하세요. A입니다.")

class B:
    def greeting(self):
        print("안녕하세요. B입니다.")

class C:
    def greeting(self):
        print("안녕하세요. C입니다.")

class D(B,C):
    pass

x = D()
x.greeting()

# 클래스.mro()을 이용하여 메서드 호출 순서 확인
print(D.mro())