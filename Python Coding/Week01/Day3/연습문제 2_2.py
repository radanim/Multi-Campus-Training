# 1. 다음의 실행결과와 같이 16진수 글자 하나를 입력하면
#    16진수인지 아닌지를 구분하는 코드를 작성하시오.

input_msg = input('16진수 한 글자 입력 :')
hex_check =['A','B','C','D','E','F','a','b','c','d','e','f']

if input_msg in hex_check:
    trans = int(input_msg,16)
    print("10진수 ==>",trans)
else :
    print('16진수가 아닙니다.')

# 방법 1) '0' <= input_msg <= '9' or 'a' <= input_msg <= 'f' or 'A' <= input_msg <= 'F'
# -------------------------------------------------------------------------------------

# 2. 다음 실행결과와 같이 입력한 금액을 5만원, 1만원, 5천원,
#    1천원, 500원, 100원, 50원, 10원 동전으로 교환하는 프로그램을 작성하시오.
money = int(input('교환할 돈은 얼마? '))
exchange = [50000,10000,5000,1000,500,100,50,10]

for exchange in exchange:
    change_count = money // exchange
    # money &= exchange
    money -= exchange * change_count
    if exchange <= 500 :
        print('%d원 : %d개' % (exchange, change_count), end=" , ")
    elif exchange == 1000:
        print('%d원 : %d장' % (exchange, change_count))
    else :
        print('%d원 : %d장' % (exchange, change_count), end=" , ")

print("\n")
print('바꾸지 못한 돈: %d원' % money)
# -------------------------------------------------------------------------------------

# 3. 두 사람이 주사위를 던져 높은 숫자가 나오면 이기는 게임을 작성해보자.
from random import randint

a_num = randint(1,6)
b_num = randint(1,6)
print('A의 주사위 숫자는 %d 입니다.'% a_num)
print('B의 주사위 숫자는 %d 입니다.'% b_num)

if a_num > b_num :
    print('B가 졌다.')
elif a_num == b_num :
    print('비겼다.')
else :
    print('B가 이겼다.')