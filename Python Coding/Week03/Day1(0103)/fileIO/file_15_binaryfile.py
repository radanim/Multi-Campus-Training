# 이진 파일 : 글자가 아닌 비트 단위로 의미가 있는 파일
# - 그림/음악/동영상/엑셀/한글/실행(exe) 파일
# 텍스트파일: 메모장으로 열고 내용이 보이는 파일

# 이진파일 읽고 쓰기 (복사)
# 읽기 : open('이진파일이름','rb')
# 쓰기 : open('이진파일이름','wb') # write()
# read(1) : 1바이트씩 읽기

b_in = open('/Users/chaewon/Desktop/스크린샷 2022-01-03 오전 9.32.36.png','rb')
b_out = open('/Users/chaewon/Desktop/tmp/스크린샷 2022-01-03 오전 9.32.36.png','wb')

while True:
    str_in = b_in.read(1)
    if not str_in : #파일의 끝: 더이상 읽을 데이터가 없음
        break
    b_out.write(str_in)
b_in.close()
b_out.close()










