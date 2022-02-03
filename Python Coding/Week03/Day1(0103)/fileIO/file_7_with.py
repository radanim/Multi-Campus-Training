# with 문
# with문이 종료되면 파일객체는 자동으로 close()
# with open(파일명, 열기모드) as 파일객체 :
#   수행코드들

file = 'test3.txt'
data = '\nhello!\nPython Programming\n'
with open(file,'a') as f: # f = open("test3.txt", 'w')
    f.write(data)



