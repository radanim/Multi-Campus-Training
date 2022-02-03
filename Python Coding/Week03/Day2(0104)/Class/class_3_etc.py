
# B.isinstance(인스턴스명, 클래스명) : 특정한 클래스의 인스턴스인지 확인
print(isinstance(my_car,Car))
# print(isinstance(my_car1,Car)) # NameError: name 'my_car1' is not defined

print('-------------------------------------------------------------------')

# C. 파이썬의 기본 클래스 : int, float, str, bool, list, dict, set, tuple, ...
a = int(10)
print(type(a))

b = list(range(10))
print(type(b))

c = dict(x=10,y=20)
print(type(c))
print(c.keys())
print(c.values())
print('-------------------------------------------------------------------')

#--------------------------------------------------------------
# D. 객체와 인스턴스
# 객체 : 객체만 지칭할 때는 객체(object)라고 하고
# 인스턴스 : 클래스와 함께 묶어서 부름
