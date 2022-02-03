# 문자열 구성 파악
# isalpha() : 문자 여부 결과 반환 (True, False)
# isdigit() : 숫자인지 결과 반환
# isspace() : 하나의 문자에 대해서 공백여부 반환
# isalnum() : 문자 또는 숫자인지 확인
# islower() : 소문자여부
# isupper() : 대문자여분

# String = '내 이름은 kmlee 이고 나이는 12 입니다'
# str_split = String.split(" ")
# for result in str_split:
#     if result.isdigit() :
#         print('%s : 숫자군요! ' % result)

# 입력된 문자열에서 알파벳, 숫자, 스페이스, 기타의 개수를 각각 계산하여 출력하기
# input_msg = input('문장을 입력하세요: ')
# alpha_cnt = digit_cnt = space_cnt = etc_cnt = 0
#
# for str in input_msg:
#     if str.isalpha() :
#         # print('문자: ',str)
#         alpha_cnt += 1
#     elif str.isdigit() :
#         # print('숫자 :',str)
#         digit_cnt += 1
#     elif str.isspace() :
#         # print('공백 : ',str)
#         space_cnt += 1
#     else :
#         # print('기타: ',str)
#         etc_cnt += 1
#
# print(f'문자의 개수: {alpha_cnt}개, 숫자의 개수: {digit_cnt}개, '
#       f'공백의 개수: {space_cnt}개, 기타: {etc_cnt}개')
# print('---------------------------------------------------------------')
#  % 서식문자열 : %s %d %f %c

# string.format()
# 1. '문자열:{위치인덱스}'.format(변수)
# 2. '문자열 {변수명}'.format(변수명=값)
# 3. '문자열 {위치인덱스:포맷코드}'.format(변수)

print('이름은 {name}이고, 폰번호는 {phone}'.format(name='이몽룡',phone='111'))

# print('---------------------------------------------------------------')