# 튜플 : tuple
# 원소 추가, 삭제, 변경 불가

# 튜플 생성 : (), tuple()

tp1 = (1,2,3)
print(tp1)
print(type(tp1)) # <class 'tuple'>
print('--------------------------------')

tp2 = 4,5,6
print(tp2)
print('--------------------------------')

tp3 = tuple([1,2,3])
print(tp3)
print('--------------------------------')

tp4 = [1,2],[3,4]
print(tp4)
print(type(tp4[0]))

# tp4[0] = [-1] #변경 불가능
# print(type(tp4[0]))
print('--------------------------------')

# 튜플의 요소를 변경불가 : 리스트로 변환하여 변경 가능
to_list1 = list(tp4)
print(to_list1)

to_list1[0]=[-1] #변경
to_list1[1]=10
print("to_list1: ",to_list1)

tp5 = tuple(to_list1)
print("tp5: ",tp5)
print('--------------------------------')

# 튜플 다루기 : 요소의 위치 index(), 일치 항목의 개수 count()

print("-1의 위치:",tp5.index([-1]))
print('10의 개수:',tp5.count(10))
print('--------------------------------')

# 튜플 삭제 : del()
# print(tp5)
# del tp5
# del(tp4)
# print('--------------------------------')

# 튜플 요소 접근 : indexing
t1 = (10,30,-10,50,100)
print(t1[0] + t1[3])
print('--------------------------------')

# 튜플 범위에 접근 : slicing
print(t1[1:3])
print(t1[1:])
print(t1[:])
print('--------------------------------')

# 튜플의 덧셈 및 곱셈 연산 : +, *
t2 = ('a','b','c')
print('t1 + t2:',t1+t2)
print('t2 * 3',t2*3)
print('--------------------------------')

# 2차원 튜플
tt = ((1,2,3),(4,5,6),(7,8,9))
print('tt:',tt)
print('tt[0]:',tt[0])
print('--------------------------------')

# 튜플의 원소 추가하는 방법
# 1) 리스트로 변경한 후 값을 추가하고 다시 튜플로 변경
myTuple = (10,20,30)
Tp_list = list(myTuple)
Tp_list.append(40)
myTuple = tuple(Tp_list)
print(myTuple)

# 2) + 연산 수행
myTuple = (10,20,30)
# update = (40,)
# myTuple = myTuple + update
myTuple += 40,
print(myTuple)

print('--------------------------------')






















