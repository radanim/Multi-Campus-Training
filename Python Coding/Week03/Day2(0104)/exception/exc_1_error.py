# 에러 발생

#0으로 나눈 경우
# 1. ZeroDivisionError : division by zero
# print(10/0)


# 자료형
# 2. TypeError : can only concatenate str (not "int") to str
# print( '나이: ' + 23 + '살')

# 3. NameError : name 'b' is not defined
# print(b)

# 4. ValueError : incomplete format
# ex. b = 10
#     print('%d%' % b)

# 5. SyntaxError : expected ':'
# x = 10
# if x > 10
#     print('합격')

# 6. IndexError: list index out of range
# a= [1,2,3,4]
# print(a[4])

# 7. UnboundLocalError
# def add():
#     a = a+1

# 8. ModuleNotFoundError: No module named 'mymodule'
# 모듈명 잘못되었거나 경로를 알 수 없을 때
# import mymodule

# 9. FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# 열고자하는 파일이 존재하지 않는 경우
# f = open('test.txt','r')
# data = f.read()
# f.close()
