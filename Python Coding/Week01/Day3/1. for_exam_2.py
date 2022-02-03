# 문제 4 : 구구단의 단수를 입력받아서 구구단을 출력하기
# num = int(input('단수 입력 :'))
# for i in range(1,10):
#     # print(num,'*',i,'=',(num * i))
#     print('{} * {} = {:2d}'.format(num, i, num*i))
#     # print('%d * %d = %d'%(num, i, num*i))

# 제곱수 구하기
# for i in range(1,10):
#     print(num,'^',i,'=',(num**i))
# print("--------------------------------------------")

# 문제 5 : 카운트 다운 프로그램
# start_num = int(input('시작 숫자 입력: '))
# for i in range(start_num,0,-1):
#     print(i, end=' ') #end : 줄바꿈 방지, 한 줄로 보일 수 있게 해주는 형식
# print('성공')

# 예제
# for i in range(0,start_num):
#     print(start_num-i , end=' ')
# print("--------------------------------------------")

# 리스트를 이용하는 경우
# score = [70,90,100,50,85]
# count=0
# for i in score:
#     count+=1
#     if i >= 60 :
#         print('%d번 학생, 점수 : %d => 합격' % (count,i))
#     else :
#         print('%d번 학생, 점수 : %d => 불합격' % (count,i))
# print("--------------------------------------------")
#
# 리스트에서 이름 찾기
# search_name = input('이름 입력: ')
# names = ["김채원",'홍길동','변학도','성춘향']
# for name in names:
#     if search_name == name:
#         find = True
#         print(name)
#         break
#     else :
#         find = False
#
# if find :
#     print("명단에 있어요!")
# else :
#     print('명단에 없어요.')
# print("--------------------------------------------")

# 10개의 정수를 받아 양수, 음수, 0 갯수 구하기
# pos, neg, zero = 0,0,0
#
# for i in range(1,11):
#     num = int(input(('숫자') + str(i) +' 입력: '))
#
#     if num > 0 :
#         pos += 1
#     elif num == 0 :
#         zero += 1
#     else :
#         neg += 1
# print("--------------------------------------------")
# print('양수 개수: %d' % pos)
# print('음수 개수: %d' % neg)
# print('0의 개수: %d' % zero)

# print("--------------------------------------------")
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# num = 0
# for y in range(3):
#     for x in range(4):
#         num += 1
#         print(num, end=' ')
#     print()
# print("--------------------------------------------")

# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1
# print("--------------------------------------------")

# i = 1
# sumN = 0;
# while i <= 10:
#     sumN += 1
#     i += 1
# print(sumN)
# print("--------------------------------------------")
# 'stop'문자 입력될 때까지 숫자를 입력하고,
# 입력된 숫자의 갯수를 출력

# num = input('숫자 입력 : ')
# cnt = 0
# while num != 'stop':
#     num = int(num)
#     cnt += 1
#     num = input('숫자 입력 : ')
#     print(num)
# print('숫자 개수',cnt)
# print("--------------------------------------------")
# 7을 입력할 때까지 계속 입력하기
# 7이 입력되면 프로그램 종료
num =int(input('숫자 입력 : '))
while num != 7:
    num = int(input('숫자 입력 : '))

print('7 입력! 종료')
# print("--------------------------------------------")









