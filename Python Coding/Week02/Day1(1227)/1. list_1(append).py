# append() : 리스트에 값 추가
# 학생 n명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하기
# 리스트 내림차순으로 정렬
# score_Arr = []
# score_sum = 0
# score_avg = 0
# count = 0
# n = int(input('학생 수 입력: '))
#
# for i in range(1,n+1):
#     score = int(input(str(i)+'번째 점수 : '))
#     score_Arr.append(score)
#
# for score in score_Arr:
#     if score >= 80:
#         count += 1
#     score_sum += score
#
# score_avg = score_sum / len(score_Arr)
#
# print(f"총점 : {score_sum}, 평균 : {score_avg}, 80점 이상 : {count}명")
# ------------------------------------------------------------------

# 엔터키를 입력 받을때까지 학생 점수 입력 받기
score_Arr = []
score_sum = 0
score_avg = 0
count = 0
no = 1

while True:
    score = input(str(no)+'번째 점수 : ')
    if score == "":
        break
    score_Arr.append(int(score))
    no += 1

for score in score_Arr:
    if score >= 80:
        count += 1
    score_sum += score

score_avg = score_sum / len(score_Arr)

print(f"총점 : {score_sum}, 평균 : {score_avg}, 80점 이상 : {count}명")

# score_Arr.sort(reverse=True)
sort_score = sorted(score_Arr,reverse=True)
print("정렬 전:",score_Arr)
print("정렬 후:",sort_score)

# ------------------------------------------------------------------
