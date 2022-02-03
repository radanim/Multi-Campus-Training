# 학생들의 이름과 성적을 딕셔너리로 저장하고 있다
# 이 딕셔너리를 사용하여 각 학생의 성적에 대한 총점과 평균을 계산하여 출력하는 코드를 작성하시오.

students = [
    {"name":"홍길동","korean":87,"math":98,"english":88,"science":95},
    {"name":"이몽룡","korean":92,"math":98,"english":96,"science":98},
    {"name":"성춘향","korean":76,"math":96,"english":94,"science":90},
    {"name":"변학도","korean":98,"math":92,"english":96,"science":92},
    {"name":"박지성","korean":95,"math":98,"english":98,"science":98},
    {"name":"류현진","korean":64,"math":88,"english":92,"science":92},
]

len = len(students)
print("이름    총점    평균")

for i in range(len):
    sum = 0
    cnt = 0

    for val in students[i].values():
        val = str(val)
        if val.isdigit() :
            sum += int(val)
            cnt += 1
    avg = sum / cnt
    print(students[i].get('name'),' ',sum,'  ',avg)



