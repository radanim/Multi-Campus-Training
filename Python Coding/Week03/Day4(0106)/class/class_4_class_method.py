# 클래스 메서드 : 인스턴스를 통하지 않고 메서드를 클래스에서 바로 호출

# 방법) 메서드 위에 @classmethod
#       : 메서드 내에 인수로 cls를 지정해야 함 (class)

# 형식)
# class 클래스이름:
#     @classmethod
#     def 메서드명(cls,매개변수들):
#         문장들

# 호출 형식) 클래스이름.메서드명(인수들)

class Person:
    count = 0 # 클래스변수

    def __init__(self,name):
        self.name = name
        Person.count += 1

    @classmethod
    def print_count(cls):
        print(f"{cls.count}명이 태어났습니다.")


man1 = Person('kim')
Person.print_count()
man2 = Person('lee')
Person.print_count()

a = {1,2,3}
b ={3,4,2}

print(a.union(b))
print(set.union(a,b))


