# 로그파일 작성

import os
import datetime,random

isdir = os.path.isdir('log')
ext = os.path.exists('log')

print(isdir)
print(ext)

if not os.path.isdir('log'):
    os.mkdir('log')

#로그기록용 텍스트 파일 생성
if not os.path.exists('log/countlog.txt'):
    f = open('log/countlog.txt','w',encoding='utf-8')
    f.write('기록시작\n')
    f.close()

#로그 기록
with open('log/countlog.txt','a',encoding='utf-8') as f :
    for _ in range(10):
        stamp = str(datetime.datetime.now())
        value = random.random() * 100
        log_line = stamp + '\t' +str(value)+'값 생성\n'
        f.write(log_line)



