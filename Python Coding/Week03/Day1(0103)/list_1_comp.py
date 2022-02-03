# list comprehension (리스트 컴프리헨션)
# 리스트를 빠르게, 간결하게 처리 : 파이썬 코드 스타일

# 예시) 정수 0~9 값을 갖는 리스트를 생성하시오
# 방법 1.
num = list(range(10))

print(num)

# 방법 2.
num_arr = []
for i in range(10):
    num_arr.append(i)
print(num_arr)

# 방법 3.list comprehension
num_arr2 = [i for i in range(10)]
print(num_arr2)


# 예시) 짝수만 리스트로 생성 : 필터링
# 방법 1.
num_arr = []
for i in range(10):
    if i % 2 == 0:
        num_arr.append(i)
print(num_arr)

# 방법 2. list comprehension
num_arr = [i for i in range(10) if i % 2 == 0 ]
print(num_arr)
print('-'*80)

num_arr = [i if i % 2 ==0 else -1 for i in range(10)]
print(num_arr)
print('-'*80)

# 방법 3. list comprehension : 중첩 반복문
list1 = ['a','b','c']
list2 = ['D','E',"F"]
result = [i+j for i in list1 for j in list2]
print(result)
result = [i+j for i in list1 for j in list2 if not(i==j)]
print(result)
print('-'*80)

words = 'Remember to let her into your heart'.split()
print(words)
print('-'*80)

result = [[w.upper(),w.lower(),len(w)] for w in words]


for i in range(len(result)):
    print(result[i])



