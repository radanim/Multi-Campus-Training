# 1. write : 파일에 쓰기

# data = 'H1'
# data = '안녕하세요'
# f = open('file2.txt','w')
# f = open('file3.txt','w',encoding='utf-8')
# f.write(data) # 파일에 data 쓰기
# f.close()

f = open('file4.txt','w',encoding='utf-8')

for i in range(1,11):
    data ='%d행\n' % i
    # data ='%d행' % i
    f.write(data)

f.close()

