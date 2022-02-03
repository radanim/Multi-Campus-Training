# 제어문
'''
pw = int(input('비밀번호 입력 : '))

if pw == 1234 :
    print("비밀번호가 일치합니다.")
else :
    # pass # 아무것도 수행하지 않음
    print("비밀번호가 일치하지 않습니다.")
'''


# 문제 : id와 password를 입력받아 모두 맞으면 로그인 성공 출력
#       그렇지 않으면 로그인 실패 출력
'''
id = input('아이디 :')
pw = int(input('비밀번호 : '))

if id == 'multicampus' and pw == 1234 :
    print('로그인 성공')
else :
    print('로그인 실패')
    if id != 'multicampus' :
        print('아이디가 잘못되었습니다.')
    if pw != 1234 :
        print('비밀번호가 잘못되었습니다.')
'''

# 문제 2 : 정수를 입력받아서 홀수인지 짝수인지 판별하여 출력
# num = int(input('정수 입력 : '))

'''
# if문
if num%2==0 :
    print('짝수입니다.')
else :
    print('홀수입니다.')
'''

'''
# 중첩 if문
if num > 0 :
    print('양수')
else :
    if num == 0 :
        print('0')
    else :
        print('음수')
'''

# 다중 if문 (if-elif)
'''
if num > 0 :
    print('양수')
elif num == 0 :
    print('0')
else :
    print('음수')
'''

# 문제 3 : 점수를 입력받아서 학점 출력
score = int(input('점수 : '))

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else :
    grade = 'F'

print('학점 : %s' % grade)
