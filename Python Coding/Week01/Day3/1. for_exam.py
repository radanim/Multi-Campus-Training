# 문제 0 : 1부터 10까지 더한 후 더한 결과 출력하기
num_sum = 0 #초기화

for num in range(11):
    num_sum += num

print("1에서 10까지 총합:",num_sum)
print("-----------------------------------")

# 문제 1 : 1부터 100까지의 범위에서 홀수만 더한 결과 출력

num_sum = 0
for num in range(1,101,2):
    num_sum += num

print("1부터 100까지 홀수만 더한 총합:",num_sum)
print("-----------------------------------")

# 문제 2 : 1부터 100 사이 정수 중 홀수와 짝수의 합을 각각 구하여 출력하기
even_sum = 0
odd_sum = 0
even_count=0
odd_count = 0
for num in range(1,101):
    if num%2 == 1:
        odd_sum += num
        odd_count += 1
    else :
        even_sum += num
        even_count += 1

even_avg = even_sum/even_count
odd_avg = odd_sum/odd_count

print("홀수 총합: %d" % odd_sum)
print("홀수 평균: %d" % odd_avg)
print("짝수 총합: %d" % even_sum)
print("짝수 평균: %d" % even_avg)

# 예제
# for i in range(1,101,2):
#    print("홀수:",i,", 짝수:",(i+1))
print("-----------------------------------")

# 문제 3 : 1부터 100 사이 정수 중 3의 배수
num_sum = 0
count = 0
for num in range(0,101,3):
    # print(num)
    num_sum += num
print("1부터 100까지 3의 배수의 총합:",num_sum)

# 문제 4 :