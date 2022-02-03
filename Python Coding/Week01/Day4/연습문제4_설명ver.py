# 1. 다음과 같이 이메일주소를 입력받아 이메일 형식인지 아닌지를 판별하여 출력하기

input_msg = input('이메일 입력 : ')

chk_msg = input_msg.find('@') #있으면 시작 위치, 없으면 -1
chk_msg2 = input_msg.find('.') #있으면 시작 위치, 없으면 -1
chk_msg3 = chk_msg2 - chk_msg
count_email = input_msg.count('@')
count_email2 = input_msg.count('.')

#(@가 있고, @ 앞에 문자가 있음) + (.가 있고, .이 @보다 뒤에 있어야 함)
# check_email3 > 1 => @와 . 사이에 문자가 1개 이상 있어야 함
if 0 < chk_msg and 1 < chk_msg3 and count_email <= count_email2 < 2:
    check_msg = input_msg.split("@")
    check_msg2 = check_msg[1].split(".")
    if check_msg2[1] == '': #. 뒤에 문자가 없는 경우 (이메일 형식이 아닌 경우 6)
        print("이메일 형식이 아닙니다.")
        print('입력한 이메일 : %s' % input_msg)
    else :
        print('이메일 형식이 맞습니다.')
else :
    # check_email = -1 : @이 없음 (이메일 형식이 아닌 경우 1)
    # check_email = 0 : @ 앞에 문자가 없음 (이메일 형식이 아닌 경우 5)
    # check_email3 <= 1 : @와 . 사이에 문자가 없음 (이메일 형식이 아닌 경우 4)
    #                   or .와 @ 위치가 바뀐 경우 (이메일 형식이 아닌 경우 3)
    #                   or .이 없는 경우 (이메일 형식이 아닌 경우 2)
    # count_email > 2 or count_email2 > 2 : @이나 .이 두 번 이상 있는 경우
    print("이메일 형식이 아닙니다.")
    print('입력한 이메일 : %s' % input_msg)

# -------------------------------------------------------------------

# 2. 다음 예와 같이 패턴이 있는 문자열에서 숫자만 추출해서 총 합계 구하기
str_data = "{a1:20},{a2:30},{a3:15}, \
           {a4:50},{a5:-14},{a6:15}, \
           {a7:20},{a8:70},{a9:-100}"
str_split = str_data.split(',')
str_Arr = []
num_Arr = []
sum = 0

for i in range(len(str_split)) :
    str_Arr.append(str_split[i].strip())
# 공백제거한 {a1:20}, {a2:30}, ... , {a9:-100}를 str_Arr에 저장

for j in range(len(str_Arr)):
    find_addr = str_Arr[j].find(':')
    num_Arr.append(str_Arr[j][find_addr + 1:-1])
# str_Arr에 저장된 변수를 하나씩 받아서 처리
# 예를 들어 {a1:20} 경우, :의 자리수를 find_addr로 받고
# {a1:20}의 [find_addr+1 : -1] 즉, 숫자부분인 {20}을 num_Arr에 저장

for k in range(len(num_Arr)):
    sum = sum + int(num_Arr[k])
# num_Arr에 저장된 모든 숫자변수를 더함

print(f'총 합계 : {sum}')

# -------------------------------------------------------------------

# 3. 다음과 같이 입력한 숫자만큼의 하트를 출력하도록 작성하시오.
#  for문과 문자열 사용
#  하트 문자 : '\u2665'

input_msg = input('숫자를 여러개 입력하세요. (한자리수) :')

for i in range(len(input_msg)):
    num = int(input_msg[i])
    print('\u2665'*num)



