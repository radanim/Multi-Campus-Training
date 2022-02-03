# 1. readline() : 한 줄씩 읽어오기
f = open('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/test.txt','r') #'r' : 읽기 용도
line = f.readline() # 첫번째 라인(행) 1개 읽어오기
print(type(line))
print(line)
f.close()

f2 = open('test.txt','r')
while True:
    line2 = f2.readline()
    if not line2:
        break
    print(line2,end="")
f2.close()
print()
print('-'*80)


# 2. readlines
# 리스트로 반환 : 한 행이 리스트의 요소가 됨

# 방법 1
f = open('test.txt','r')
lines = f.readlines()
print('2.readlines: ',lines)
f.close()
print('-'*80)

# 방법 2
f = open('test.txt','r') #'r' : 읽기 용도
for line in f : #readlines() 자동 수행
    print(line,end="")
print()
print('-'*80)
f.close()

# 3. read
f = open('test2.txt','r') #'r' : 읽기 용도
data = f.read() # 모든 라인(행) 읽어오기
print(data)
f. close()
print('-'*80)

for c in data :
    print(c)
print('-'*80)



