# 파일 압축 및 풀기

import zipfile as z

# 파일 압축
new = z.ZipFile('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/log.zip','w')

new.write('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/test.txt',
        compress_type=z.ZIP_DEFLATED)
new.close()

# 압축 파일 풀기
ext = z.ZipFile('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/log.zip','r')
ext.extractall('/Users/chaewon/Documents/멀티캠퍼스/파이썬/PythonStudy/PythonStudy/Week03 (0103~0107)/Day1(0103)/fileIO/')
ext.close()





