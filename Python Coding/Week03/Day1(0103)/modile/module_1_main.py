# main 예제

name = ''

def input_name():
    global name
    name = input('이름 입력 : ')

def get_name():
    if name == " ":
        print("이름 없음")
    else :
        return name


if __name__ == '__main__':
    input_name()
    print(get_name())
else :
    print('module_main이 import')