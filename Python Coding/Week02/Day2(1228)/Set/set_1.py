# set : 집합 형태의 자료 구조 (집합 자료형)

# set 생성
s1 = {1,2,3,4,5}
print(s1)
print(type(s1))
print('-----------------------')

s2 = set([3,4,7,8,9])
print(s2)
print(type(s2))
print('-----------------------')

print(dir(s1))
# '__and__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__',
# '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__',
# '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',
# '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__',
# '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
# '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
# 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']
print('-----------------------')

s3 = set()
print(s3)
print('-----------------------')

# set의 특징
# 1. 중복을 허용하지 않음 : unhashable type
# 2. 순서가 없음 (입력순서와 출력순서가 다를 수 있음)------------------------------------------

s4 = {1,3,2,2,5,4,3}
print(s4) #{1, 2, 3, 4, 5}
print('-----------------------')

# 3. 인덱스 사용 불가 : 이미 포함되어 있는 요소를 변경할 수 없음----------------------------------

# print(s4[0]) #에러 발생
# s4[0] = 2 #에러 발생

# 4. 추가, 삭제 가능 : add(), update()--------------------------------------------------
s4.add(10) # 한개 추가
print(s4) #{1, 2, 3, 4, 5, 10}

s4.update([5,6]) # 여러개 추가
print(s4) #{1, 2, 3, 4, 5, 6, 10}
print('-----------------------')

# 5. 집합 안에 (변경 가능한 항목) 포함 불가능------------------------------------------------
#    : 리스트 포함 불가, 튜플 포함 가능
# s5 = {1,2,[3,4]} #TypeError: unhashable type: 'list'
s6 = {1,2, (3,4) } #튜플은 가능
print(s6)
print('-----------------------')

# 6. 요소 삭제 가능---------------------------------------------------------------------
print('삭제 전: %s' % s6)
s6.remove(1) #삭제할 값이 없으면 에러 발생
print('삭제 후: %s' % s6)

s6.discard(10) #삭제할 값이 없어도 에러 발생 x
print('s6.discard(10):',s6.discard(10)) #None

s6.clear()
print('s6.clear():',s6) #요소 전체 삭제 => set() (빈 집합구조)

s6.add(10)
print('s6.add(10)',s6)

del s6 #메모리에서 집합 자체를 삭제
print('-----------------------')



















