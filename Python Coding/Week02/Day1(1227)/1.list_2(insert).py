# insert(위치/인덱스,값) : 리스트의 원하는 위치에 값을 삽입

x = ['apple','banana','coconut','melon']
print(x)

x.insert(1,'watermelon') # ['apple', 'watermelon', 'banana', 'coconut', 'melon']
print(x)
print('-----------------------------------------------------------')
# 리스트의 요소 제거
# 1. remove(값) : 지정한 값을 제거, 동일한 값을 한번에 제거할 수 없음
# 2. pop() : 마지막 요소의 값을 제거
#    pop(index): index 위치 요소 ㄱ밧을 제거

x = ['apple','banana','coconut','melon','banana','apple']
print(x)
x.remove('banana') # 처음으로 만나는 banana만 삭제
print(x)
print('-----------------------------------------------------------')

x = ['apple','banana','coconut','melon','banana','apple']
n = x.count('banana')
for i in range(n):
    x.remove('banana')  # 모든 'banana' 제거

print(x)
print('-----------------------------------------------------------')
y = [1,3,5,1,10]
y_last = y.pop()  # 마지막 값을 지우고, 반환함. 즉, return값 = 마지막 값

print(y)
print('y_last:',y_last)

y.append(-10)
print(y)
rm = y.pop(3)
print(y)
print('rm:',rm)
# y.remove(0) 제거하고자 하는 값이 없음변 VlueError가 생김

y[3]='list' #값을 변경
print(y)
print('-----------------------------------------------------------')

for i in range(len(y)):
    y.pop()
    print(y)

    


