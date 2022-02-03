# gbbGame.py
import random

def gbb_game(you_n):
   com_n = random.randint(1, 3)
   num = com_n - you_n
   if num == -2 or num == 1:
       result = '컴퓨터가 이겼습니다.'
   elif num == 0 :
       result = '비겼습니다.'
   else :
       result = '당신이 이겼습니다.'
   return result,com_n

def input_num():
    input_msg = int(input('YOU 입력 (가위: 1, 바위: 2, 보: 3) : '))
    result,com_n = gbb_game(input_msg)
    print(result)
    print(f'COM : {com_n}')