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
    print("%s   %d    %.2f"% (students[i].get('name'),sum,avg))


# 딕셔너리를 이용하여 사용자로부터 영어단어와 뜻을 입력받아 사전을 구성하고,
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램을 작성하시오.

eng_dict = {}

while True:
    input_eng = input('영어 단어 등록 (종료는 quit) : ')

    if input_eng == 'quit':
        print()
        while True:
            search_msg = input('검색할 단어 입력 (종료는 quit) :')

            if(search_msg == 'quit'):
                break
            elif search_msg in eng_dict.keys():
                val = eng_dict[search_msg]
                print(search_msg,'의 뜻은',val,'입니다.\n')
            else:
                print(search_msg,'는 사전에 없는 단어 입니다. \n')
        break

    elif input_eng in eng_dict.keys():
        print(input_eng +'는 이미 등록된 단어 입니다.\n')

    else :
        input_dict = input(input_eng + '의 뜻입력 (종료는 quit) :')
        eng_dict[input_eng] = input_dict
        print()


























