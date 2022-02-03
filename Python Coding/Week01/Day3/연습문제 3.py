# for문 이용하여 별 출력하기 문제 (1)
for i in range(5,0,-1):
    print('☆'*i)
print('---------------------------')

# for문 이용하여 별 출력하기 문제 (2)
for i in range(1, 10,2):
    print(' ' * ((10 - i) // 2), end=' ')
    print('☆' * i)
print('---------------------------')

# while문을 이용하여 다음의 결과 화면과 같이 7을 입력할 때까지
# 입력을 반복하고, 7이 입력되면 종료되는 코드를 작성하시오.
while True :
    num = int(input('숫자 입력: '))
    if num == 7 :
        break

print(num, "입력! 종료")
print('---------------------------')

# 1곡에 2,000원하는 노래방 기계에서 현재 잔액이 10000이 소진될 때까지
# 노래방을 이용하는 프로그램을 작성하시오
money = 10000
count = 0

while True :
    count += 1
    money = 10000 - (2000 * count)
    print('노래를 %d곡 불렀습니다.' % count)
    print('현재 %d원 남았습니다. \n' % money)
    if money == 0 :
        print('잔액이 없습니다. 종료합니다.')
        break
