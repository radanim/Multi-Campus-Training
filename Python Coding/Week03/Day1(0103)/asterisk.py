# * : 변수 앞에 붙은 경우 (*args, **kwargs) => 언패킹(unpacking)

def asterisk_test(a,*args) :
    print(a,args)
    print(type(args))
    

asterisk_test(1,2,3,4,5)
print('-'*80)

def asterisk_test2(a, *args):
    print(a, *args)
    print(type(args))

asterisk_test2(1,2,3,4,5)
print('-'*80)

def asterisk_test3(a, **args):
    print(a, *args) #키
    print(a, args) #키:값 (딕셔너리 형태)
    print(type(args))

asterisk_test3(1,b=2,c=3,d=4,e=5) #키 = 값
print('-'*80)

data2 = {'b': 2, 'c': 3, 'd': 4, 'e': 5} #딕셔너리
asterisk_test3(1,**data2)
print('-'*80)