# 리스트 연산
# 1. 리스트 합치기 : +
# 2. 리스트 곱하기 : * (반복)
# 3. 리스트 내용 변경


fruits = ['apple','banana','melon']
a = [1, 'apple', 3.5, [10,20,30], True]

# 1. 리스트 합치기 : +
b = fruits + a
print("fruits + a")
print(b)
print('-----------------------------')

# 2. 리스트 곱하기 : * (반복)
c = fruits * 3
print("fruits * 3")
print(c)
print('-----------------------------')

# 3. 리스트 내용 변경
a[3]='melon'
print("a[3]='melon' => ",a)
print('-----------------------------')
a[1:3] = [10,11,12]
print("(a[1:3] = [10,11,12]) => ",a)
print('-----------------------------')
a[0] = [-1,-4]
print("(a[0] = [-1,-4]) => ",a)
print('-----------------------------')

# 리스트 복사
# 1. 얕은 복사 : 실제 리스트가 복사되지 않고 참조값(주소)만 복사
a = [1,2,3,4]
b = a
print('a:',a)
print('b:',b)

a[-1] = 100
b[0] = 0.5
print('a: %s \nb: %s'%(a,b))
print('-----------------------------')

# 2. 깊은 복사 (deep cody) : 리스트 복사본을 새로 생성하여 반환
# list() 함수 또는 copy모듈의 deepcopy() 함수 사용
# 2-1. list() 함수
a = [1,2,3,4]
c=list(a)
d=a
print(c)
print(d)
print(id(a[0]),id(c[0]))
print('바뀌기 전 c :',c)
a[0] = 'apple'
c[-1] = '!!'

print('바뀐 뒤 a :',a)
print('바뀐 뒤 c :',c)
print('-----------------------------')
# 2-2. copy모듈의 deepcopy() 함수
import copy

d=['a','b','c']
e = copy.deepcopy(d)
print('',e)

e[0] = 1
print('',d)
print('',e)