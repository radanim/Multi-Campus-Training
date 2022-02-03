# 예외 처리
# 에러 종류와 상관없이 에러가 발생하면 처리하기

# try :
#     에러가 발생할 문장들
# except:
#     에러가 발생하면 처리하는 문장들
# else :
#     에러가 발생하지 않으면 처리하는 문장들
# finally :
#     에러와 상관없이 항상 수행하는 문장들

# 예제) 0으로 나누는 경우
try :
    print(10/0)
except ZeroDivisionError as e: # e = 에러 메세지 변수 (에러 내용 출력)
    print('0으로 나눌 수 없습니다 =>',e)

# 예제) TypeError
try :
    print('나이: '+ 23 + '살')
except:
    print('오류 발생')

# 예제) ValueError
try :
    num = int(input('숫자 : '))
except ValueError as e:
    print('숫자가 아닙니다 =>',e)
else :
    print(f'{num} => 숫자')

# 예제) UnboundLocalError
try :
    def add():
        # a = a+1
        pass
    add()
except UnboundLocalError as e:
    print('에러 발생 =>',e)
    print('-'*30)

# 여러개의 except 처리
# 경우 1) 하나만 출력
try :
    print(10/0)
    print('나이: '+ 23 + '살')
except TypeError as e:
    print('형식이 잘못 지정되었습니다.',e)
except ZeroDivisionError as e:
    print(e)

try :
    print(10/0)
    print('나이: '+ 23 + '살')
except (TypeError,ZeroDivisionError) as e:
    print('형식이 잘못 지정되었습니다.',e)
    print('-'*50)


try :
    f = open('test.txt','r')
except FileNotFoundError :
    print('파일이 발견되지 않았습니다.')
else :
    data = f.read()
    print(data)
    f.close()
finally:
    print('end')
