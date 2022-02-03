def input_member(f_in):
    input_f = open(f_in,'w')
    while True:
        input_msg = input('멤버를 입력하세요. (종료는 q) : ')
        if input_msg != 'q':
            input_f.write(input_msg+'\n')
        else :
            break
    input_f.close()
        

def output_member(f_out):
    output_f = open(f_out,'r')
    
    names = output_f.readlines()
    for name in names:
        if name != '\n':
            print(name,end='')
    

while True:
    input_no = input('저장 1, 출력 2, 종료 q : ')
    if input_no == '1':
        input_file = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(input_file)
    elif input_no == '2':
        output_file = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(output_file)
    elif input_no == 'q':
        break
    else :
        print('잘못 입력하셨습니다. 다시 입력해주세요.')

