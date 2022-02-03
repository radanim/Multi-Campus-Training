import os
import shutil

# os.mkdir('log') #폴더 생성, 기존에 생성되어있는 폴더를 또 생성할 때 오류 발생 -> os.path 사용
# shutil.rmtree('log') #폴더 삭제

#기존 디렉터리 확인
import os.path as pa
if not pa.isdir('log'):
    os.mkdir('log')
else :
    print('already exist')


