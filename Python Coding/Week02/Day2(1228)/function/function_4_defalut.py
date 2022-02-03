# default 매개변수
# 매개변수의 기본 값을 지정

def greet(name,msg='안녕^^'):
    print(name+': '+msg)

# greet('홍길동','반가워')
# greet('강감찬') #msg에 값을 주지 않는 경우, default
#----------------------------------------------------------------------
def show_info(name,year=1,age=20):
    print(f'{name}/{year}학년/{age}세')

# show_info('홍길동',3,22)
# show_info('홍길동',3)
# show_info('홍길동')
#----------------------------------------------------------------------
# for i in range(5):
#     print('hi',end=" ") #end의 default : \n
# ----------------------------------------------------------------------
# 1. 함수에 리스트 전달

def show_name(list):
    print("   show() :",list)

    for name in list:
        print(name,end="  ")
    print()

def modify_name(list):
    list.append('new')
    print(" modify() :",list)

name_list = ['홍길동','강감찬','이순신']
show_name(name_list)
modify_name(name_list)
print('name_list :',name_list) #기존 리스트도 바뀜
print('------------------------------------------------------------')
# ----------------------------------------------------------------------
# 2. 함수에 딕셔너리 전달

def show_info(dict):
    for info in dict.values():
        print(info,end=' ')
    print()

info_dict = {'name':'홍길동','age':20,'phone':'010-123-123'}
info_dict2 = {'name':'강감찬','age':23,'phone':'010-111-111'}
info_dict3 = {'name':'이순신','age':21,'phone':'010-222-222'}

show_info(info_dict)
show_info(info_dict2)
show_info(info_dict3)
# ----------------------------------------------------------------------





