# 산술 연산자 예제
second = 1000
minutes = second // 60
remainder = 1000 % 60
print("%d분 %d초" % (minutes,remainder))

# 산술 연산자 연습문제 1
myMoney = 5000
candyPrice = 120
numCandies = myMoney // candyPrice
change = myMoney % candyPrice

print('사탕의 개수 : %d개' % numCandies)
print('나머지 돈 : %d원 \n' % change)

# 지수 연산자 예제
x= 3
y = 3 * x**2
print(y,"\n")

# 관계 연산자 예제 : >, <, >=, <=, ==, !=
result = 100 > 10
print(result,"\n") # True

# 논리 연산자 : and, or, not
# a = int(input("a: "))
a = 100
print(a < 10 or a > 20)
print(a==100,"\n")

# 비트연산자 : bit ( &, |, ^, ~, <<, >> )
print("True & True : ",True & True)
print("True & False : ",True & False)
print("True | False : ",True | False)
print("False | False : ",False | False)
print(~a)
print(a>>1)
print(a>>2)
print(a<<1)
