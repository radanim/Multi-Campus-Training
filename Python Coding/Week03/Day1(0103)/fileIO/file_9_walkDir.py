# 디렉터리 목록 보기

import os

print(os.walk('/Users/chaewon/python'))

for dir_name, sub_dir, fnames in os.walk('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO'):
    print(dir_name)

    # for fname in fnames :
    #     print(fname)
        # print(os.path.join(dir_name,fname))





