# 무한 루프 1
# while True :
#     num = int(input('숫자 입력: '))
#     if num == 7 :
#         break
#
# print(num, "입력! 종료")
# print("-----------------------------------------")
# 무한 루프 2
# 조건 만족 시 끝남
# while 1 :
#     num = int(input('숫자 입력: '))
#     if num == 7 :
#         break
#
# print(num, "입력! 종료")
# print("-----------------------------------------")
# 문제 1 : while & break : 무한루프 이용
# 'q'가 입력되면 종료
# while True :
#     input_msg = input('입력 : ')
#     if input_msg == 'q':
#         print('종료')
#         break
# print("-----------------------------------------")
# 문제 2 : while & continue : 무한루프 이용
# for i in range(10):
#     if i % 2 == 0 :
#         continue
#         # print("%d: 짝수" %i)
#     print(i)
# print("-----------------------------------------")
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         # break
#         continue
#     print(i)
#     i += 1
# print("-----------------------------------------")
# 난수 발생

# import random
# from random import randint
#
# n = randint(1,10)
# print(n)
# print("-----------------------------------------")
# 문제 :
print("%d / %d = %f" % (10, 4, 10 / 4))
print("%d / %d = %5.1f" % (10, 4, 10 / 4))
print("%d / %d = %5.0f" % (10, 4, 10 / 4))
print("%05d" % 543)
print("%10s" % "파이썬")
print("%1.1f" % 123.45)

