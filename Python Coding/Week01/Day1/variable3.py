# 포맷 코드 사용
# 방법 1. print("문자열", 변수)
# 방법 2. 포맷 코드
#       형식) print("서식" % 값)
#       형식) print("문자열 %d 문자열" % 변수)
#
#  %d : 정수
#  %f : 실수
#  %s : 문자열
#  %c : 문자 1개
#  %o : 8진수
#  %x : 16진수
#  %% : % 표현

name , age = "김채원", 23
avg = 93.5
rate = 80.5

print('나이: %d살' % age)
print('이름: %s' % name)
print('평균: %.2f' % avg)
print('출석률 : %.1f%% \n' %rate )

# 화씨 온도 구하기
fTemp = 90
cTemp = (fTemp - 32) * 5 / 9
print('섭씨 온도: %d' % fTemp)
print('화씨 온도: %.2f \n' % cTemp)
