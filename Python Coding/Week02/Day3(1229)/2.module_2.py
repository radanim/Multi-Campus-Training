# 1. 모듈 참조
# 방법 1) import 모듈명
# ex. import random

# 방법 2) import 모듈명 as 별칭
# 모듈명이 길거나 모듈명이 동일한 경우 별칭으로 사용
# ex. import pandas as pd

# 2. 모듈 내 함수 참조
# import 모듈
# 모듈.함수명
#
# import random
# random.randint(3,10)
# print(random.randint(3,10))

# 3. 모듈 내 일부만 참조
# 방법 1) from 모듈명 import 변수명/함수명
# ex. from random import randint,randrange

# 방법 2) from 모듈명 import * = import random (단, 매직메서드 제외)
    #매직 메서드/스페셜 변수 : 모듈내에서 __로 시작하는 메서드

# 방법 3) from 모듈명 import 변수명/함수명 as 별칭

# 4. calculator 모듈 사용하기
# 방법 1) import calculator
# 방법 2) from calculator import add,sub
# 방법 3) from calculator import *
# 방법 4) import calculator as cal
import calculator as cal
print(cal.add(10,5))

import sys
sys.path.append('/game/graphic/render.py')

