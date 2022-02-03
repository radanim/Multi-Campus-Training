# 패키지(package)
# : 모듈들을 모아놓은 디렉터리(폴더)

# 일반적인 디렉터리와 차이점
# 패키지) 디렉터리 안에 __init__.py 존재 (빈 파일)

# 패키지를 사용할 경우 모듈 import
# import 패키지.모듈명
# import 패키지.모듈명 as 별칭
# from 패키지.모듈 import 함수
# from 패키지.모듈 import **

#패키지를 구성하는 방법(파이참)
#1. [파일] - new - python pakage
import My_pakage.pack1.module11 as m11
import My_pakage.pack1.module12 as m12
import My_pakage.pack2.module21 as m21
import My_pakage.pack2.module22 as m22

from My_pakage.pack3.module31 import func31
from My_pakage.pack3.module31 import *

m11.func1()
m11.func2()
m12.func2_1()
m21.func21()
m22.func22()
func31()










