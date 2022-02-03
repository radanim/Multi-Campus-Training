#  함수 : 함수이름()
#        함수이름()으로만 호출
#        input(), print(), len(), del() : 내장 함수
#        사용자 정의 함수

#  메소드 : 메소드이름()
#  클래스의 멤버인 객체를 통해서 사용
#  string객체이름.find()

# 리스트에서 사용되는 함수 : len() => 리스트의 길이 반환(원소의 개수)
# a = [1,2,3,4,5]
# print(len(a))

score_Array = []
for i in range(1,6):
    score = int(input(f'학생{i} 점수 입력 : '))
    score_Array.append(score)

score_sum = sum(score_Array)
score_avg = score_sum / len(score_Array)

print(f'총점 : {score_sum}\n평균 : {score_avg:.2f}')