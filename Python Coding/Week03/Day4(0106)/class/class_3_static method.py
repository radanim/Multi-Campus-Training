# 정적 메서드(static method)
# 목적) 인스턴스를 통하지 않고 클래스에 바로 호출하여 사용
# 방법) 메서드 바로 위에 @staticmethod을 사용

class Calc:
    @staticmethod # self 지우기: 인스턴스 변수/메서드가 필요 없기 때문에
    def add(a,b):
        return a+b

    @staticmethod
    def mul(a ,b ):
        return a*b

calc1 = Calc()
calc2 = Calc()

print(calc1.add(3,2))
print(calc2.add(4,2))

# 호출 방식) 클래스이름.정적메서드(*args)
print(Calc.mul(10,30)) # 인스턴스를 생성할 필요가 없음
