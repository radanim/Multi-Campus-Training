# 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서 
# 한 줄의 두 숫자를 더한 연산 결과를 파일로 저장하기 

import os.path as pa
file_name = '/Users/chaewon/python/list_num.txt'
file_name2 = '/Users/chaewon/python/save_list_num.txt'
open_file = open(file_name,'r')

if not pa.exists(file_name2):
    new_file = open(file_name2, 'w')
    new_file.close()

def sum(f,file_name2) :
    val_arr = f.readlines()
    f2 = open(file_name2, 'w')
    for val in val_arr:
        if val != '\n':
            sum = 0
            num = val.split(' ')
            sum = float(num[0]) + float(num[1])
            f2.write(num[0] + '+' + num[1].replace("\n","") + '=' + str(sum)+'\n')
    f2.close()

sum(open_file,file_name2)
open_file.close()