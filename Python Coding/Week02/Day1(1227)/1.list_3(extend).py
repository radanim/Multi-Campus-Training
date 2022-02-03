# 리스트.extend() : 리스트 확장

a = [1,2,3]
a.extend([4,5])
print(a)

a.append(9) #하나의 리스트로 들어감 -> [1, 2, 3, 4, 5, 9]
print(a)

a.append([-1,10]) #리스트 안에 리스트로 들어감 -> [1, 2, 3, 4, 5, 9, [-1, 10]]
print(a)

a.insert(3,[1,2]) #[1, 2, 3, [1, 2], 4, 5, 9, [-1, 10]]
print(a)

print('--------------------------------------------------------------')

# 리스트 정렬
# 1. 리스트.sort() : 리스트 정렬
# 2. 리스트.reverse() : 리스트의 순서를 역순으로 변경
# 3. sorted(리스트) : 정렬하여 새로운 리스트를 생성

scores = [90,80,70,81,64,99]
print('정렬 전: ',scores)
scores.sort() #오름차순
print('오름차순 정렬 후: ',scores)
print('--------------------------------------------------------------')

scores = [90,80,70,81,64,99]
print('정렬 전: ',scores)
scores.sort(reverse=True) #내림차순
print('내림차순 정렬 후: ',scores)
print('--------------------------------------------------------------')

scores = [90,80,70,81,64,99]
print('정렬 전: ',scores)
scores.reverse() #역순으로 순서 변경
print('reverse 후: ',scores)
print('--------------------------------------------------------------')

scores = [90,80,70,81,64,99]
print('정렬 전: ',scores)
result = sorted(scores) #오름차순
# result = sorted(scores,reverse=True) #내림차순
print('sotred(scores) 후: ',result)
print('--------------------------------------------------------------')

# .sort(key=정렬하고자 하는 기준점)
chr = ['b','A','e','C']
print('sort 전: ',chr)
chr.sort() #오름차순
print('오름차순 sort 후: ',chr)
print('--------------------------------------------------------------')

chr = ['b','A','e','C']
print('sort 전: ',chr)
chr.sort(reverse=True) #내림차순
print('내림차순 sort 후: ',chr)
print('--------------------------------------------------------------')

# 대소문자 구별없이 알파벳 정렬
chr = ['b','A','e','C']
print('sort 전: ',chr)
chr.sort(key=str.lower) #대소문자 구별 x
print('(lower) sort 후: ',chr)
print('--------------------------------------------------------------')

chr = ['b','A','e','C']
print('sort 전: ',chr)
chr.sort(key=str.lower,reverse=True) #역순
print('(lower)(reverse) sort 후: ',chr)
print('--------------------------------------------------------------')












