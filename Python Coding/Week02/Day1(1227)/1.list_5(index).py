# 리스트 안에 원소의 위치 값 반환 : index(value)
# 찾는 원소가 없는 경우 에러

x = ['banana','apple','Coconut','Melon']
idx = x.index('apple')
# idx = x.index('Apple')
print(idx)

cnt = x.count('apple')
print(cnt)
print('-----------------------------------------------')
# ---------------------------------------------------------------

# 리스트에서 in / not in 연산
num = [1,2,4,5,7]
result = -10 in num
print(result)
print('-----------------------------------------------')
# ---------------------------------------------------------------

# 리스트가 같은지 다른지 일치 검사 : ==, !=, >, < 등 이용
list1 = [1,2,3]
list2 = [1,2,3]
print('list1 == list2 :',list1 == list2)
print('list1 > list2 :',list1 > list2)
print('list1 < list2 :',list1 < list2)
print('-----------------------------------------------')
# ---------------------------------------------------------------
# 2차원 리스트: 리스트 안에 리스트

data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(data)

for row in data :
    print('배열: ',row)

row = len(data)
col = len(data[0])
print('-----------------------------------------------')

for r in range(row):
    for c in range(col):
        print(data[r][c], end='\t')
    print()







