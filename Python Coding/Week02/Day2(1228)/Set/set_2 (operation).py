#set의 연산

A = {1,2,3}
B = {3,4,5}

# 1. 교집합
C = A & B
print(C) #3

C = A.intersection(B) #3
print('------------------')

# 2. 합집합
C = A|B
print(C) #{1,2,3,4,5}

C = A.union(B) #{1,2,3,4,5}
print('------------------')

# 3. 차집합
C = A - B
print(C) #{1, 2}
C = A.difference(B) #{1, 2}

D = B - A
print(D) #{4, 5}
D = B.difference(A) #{4, 5}
print('------------------')











