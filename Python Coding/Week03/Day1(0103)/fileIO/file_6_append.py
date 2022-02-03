# append() : 파일 끝에 내용 추가
f = open('test2.txt','a')

appendData = '\n\nPython Programming'

f.write(appendData)

f = open('test2.txt','r')
print(f.read())
f.close()









