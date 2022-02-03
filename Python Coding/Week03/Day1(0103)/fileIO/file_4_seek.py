# 파일 내에서 검색
# seek(offset,whence)
#   1) offset : 상대 위치 (시작 위치로부터 열의 위치)
#   2) whence : 위치 (0: 시작위치, 1: 현재위치, 2: 파일의 끝위치)

# ex. seek(0,0) : 시작위치로부터 0열의 위치 => 0행 0열
# ex. seek(10,0) : 시작위치로부터 10열의 위치 => 0행 10열
# ex. seek(0,1) : 현재위치
# ex. seek(0,2) : 끝위치로부터 0열의 위치 => 마지막행 0열

f = open('test2.txt','r')
# f.seek(0,0) #0행 0열
# f.seek(3,0) #0행 3열
f.seek(6,0) #0행 6열
# f.seek(10,0) #0행 10열
# f.seek(0,2) #파일의 마지막 위치
# f.seek(14,0) #한글은 못 읽어옴 (2바이트씩 끊어서 입력해야함)
# f.seek(15,0) #한글은 못 읽어옴 (2바이트씩 끊어서 입력해야함)
# lines = f.readlines()
# print(lines)
line = f.readline()
print(line)
f.close()













