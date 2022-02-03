# 수치형, 문자열 : 변경 불가능(immutable)
x = '123'
y = x
y += '4'

print('수치형, 문자열 : 변경 불가능(immutable)')
print(x) #123
print(y) #1234
print('id(x):',id(x))
print('id(y): %s 불일치' % id(y))
print('-------------------------------------------------')

# 튜플 : 변경 불가능(immutable)
x = (1,2)
y = x
y += (3,)

print('튜플 : 변경 불가능(immutable)')
print(x) #(1, 2)
print(y) #(1, 2, 3)
print('id(x):',id(x))
print('id(y): %s 불일치' % id(y))
print('-------------------------------------------------')

# 리스트 : 변경 가능(mutable)
x = [1,2]
y = x
y.append(3)

print('리스트 : 변경 가능(mutable)')
print(x) #[1, 2, 3]
print(y) #[1, 2, 3]
print('id(x):',id(x))
print('id(y): %s 일치' % id(y))
print('-------------------------------------------------')

# 딕셔너리 : 변경 가능(mutable)
x = {1:2}
y = x
y[2] = 3

print('딕셔너리 : 변경 가능(mutable)')
print(x) #{1: 2, 2: 3}
print(y) #{1: 2, 2: 3}
print('id(x):',id(x))
print('id(y): %s 일치' % id(y))
print('-------------------------------------------------')