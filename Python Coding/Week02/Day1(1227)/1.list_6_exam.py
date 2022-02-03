# 문제) 각 학생별 점수 리스트 생성
kim = [90,85,70]
choi = [88,92,72]
kang = [100,95,100]
lee = [90,60,70]

avg = 0
name = ['kim','choi','kang','lee']
students = [kim,choi,kang,lee]

# 학생별 총점과 평균점수 출력
for i in range(len(students)):
    sum = 0
    num = len(students[i])
    for j in students[i]:
        sum += j
    avg = sum / num
    print('%s의 총점: %d, 평균: %0.2f' % (name[i],sum,avg))
print('---------------------------------------------')

Arr = ['국어', '영어', '수학']
# 과목별 총점과 평균점수 출력
for i in range(len(students)-1):
    sum = 0
    num = len(students)

    for j in range(num):
        sum += students[j][i]

    avg = sum/ num
    # print('%s) 총점: %d, 평균: %0.2f' % (Arr[i],sum,avg))
    print('{}) 총점: {}, 평균: {}'.format(Arr[i], sum, round(avg,1)))
























