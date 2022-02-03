#!/usr/bin/env python
# coding: utf-8

# # pandas 데이터 합치기

# - pandas는 두 개 이상의 데이터 프레임을 하나로 합치는
# - **병합(merge)**이나 **연결(concate)**을 지원
# - merge(), join(), concat()

# In[1]:


# 필요 모듈
import pandas as pd
import numpy as np
import random


# In[2]:


# 여러 변수 출력 코드
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# ## 1. 데이터 병합

# ### 1) merge() 명령을 이용한 데이터 프레임 병합
# 
# - **merge** : 
#     - 두 데이터 프레임의 공통 열(column)이나 인덱스(index)를 기준으로 합침
#     - **key** : 기준이 되는 열 데이터

# #### 형식
# - df.merge(df1) : 두 df를 병합시켜 준다.
# - 기본은 inner join : 양쪽에 동일하게 존재하는 키만 표시
# - key : 기준열을 의미
#     -  실제 데이터 필드거나 행 인덱스 일 수 있다.
# - 병합방식
#     - inner join :  양쪽 df에서 모두 키가 존재하는 data만표시
#     - outer join :  한쪽에만 키가 존재하면 data를 표시
#     - 병합방식을 설정 : how=inner(생략가능), how=outer 
# 

# ![](./img/join_all.PNG)

# ![](./img/join_inout.PNG)

# **예제1. 데이터프레임 생성**
# 
# - 고객 정보를 담고 있는 데이터 프레임

# In[3]:


# 예시 df 생성 - 고객 정보를 담고 있는 df
df1 = pd.DataFrame({'고객번호':[1001,1002,1003,1004,1005,1006,1007],
                   '이름':['둘리','도우너','또치','길동','희동','마이콜','영희']},
                  columns=['고객번호','이름'])
df1


# - 예금 정보 데이터 프레임

# In[5]:


# 예제 df 생성 - 예금 정보 df
df2 = pd.DataFrame({'고객번호':[1001,1001,1005,1006,1008,1001],
                   '금액':[10000, 20000,15000, 5000, 100000, 30000]},
                  columns=['고객번호','금액'])
df2


# **merge 명령으로 두 df를 병합하는 문법**

# merge(df1, df2, how, on, left_on, right_on, left_index, right_index)

# - 모든 인수 생략(병합 df를 제외한) 공통 이름을 갖고 있는 열
# - '고객번호'가 키가 됨
# - 양쪽에 모두 존재하는 키의 data만 보여주는 **`inner join`** 방식을 사용
#     - pandas.merge(df1, df2)
#     - df1.merge(df2)

# In[7]:


df1.head(2)
df2.tail(2)


# **데이터프레임1.merge(데이터프레임2)**
# - 기준 데이터프레임은 df1

# In[9]:


df1.merge(df2)


# In[11]:


# df2가 기준 데이터프레임인 경우
df2.merge(df1)


# **pandas.merge(데이터프레임1, 데이터프레임2)**
# - 기준데이터 프레임은 왼쪽에

# In[8]:


# 기준 데이터 프레임  : 왼쪽에 나타남
pd.merge(df1,df2)


# ### how 인수를 사용한 다양한 병합

# **merge( , how = 'outer')**
# - how = inner/outer/left/right
#     - how=left : 왼쪽 df에 있는 모든 키의 데이터는 표시
#     - how=right : 오른쪽 df 에 있는 모든 키의 데이터는 표시

# - outer join
#     - 키 값이 한쪽에만 있어도 데이터를 보여 줌
#     - 어느 한 df에 데이터가 존재하지 않으면 NaN으로 표시됨

# In[12]:


pd.merge(df1,df2, how='outer')


# - left join

# In[13]:


pd.merge(df1,df2, how='left')


# - right join

# In[14]:


pd.merge(df1,df2, how='right')


# ### 동일한 키 값이 있는 경우
# 
# - 키값이 같은 데이터가 여러개 있는 경우에는 있을 수 있는 모든 경우의 수를 따져서 조합을 만들어 낸다.

# **예제2. 데이터프레임 생성**

# - 데이터프레임1 

# In[15]:


# 예제 df 생성 
# 열: 품종, 꽃잎길이
df1 = pd.DataFrame({
    '품종':['setosa','setosa','virginica','virginica'],
    '꽃잎길이':[1.4, 1.3, 1.5, 1.3]},
    columns=['품종','꽃잎길이'])
df1


# - 데이터프레임2

# In[17]:


# 열 : 품종, 꽃잎너비
df2 = pd.DataFrame({
    '품종': ['setosa','virginica','virginica','versicolor'],
    '꽃잎너비':[0.4,0.3,0.5,0.3]},
    columns=['품종','꽃잎너비'])
df2


# - df1과 df2 를 병합
# 
# 
#     - 위 데이터에서 키 값 setosa에 대해
#         - df1에는 1.4와 1.3 2개의 데이터가 있고
#         - df2에는 0.4라는 1개의 데이터가 있으므로
#         - 병합 데이터에는 setosa가 (1.4,0.4)(1.3,0.4)의 2 경우가 표현된다.
#         
# 
#     - 키값 virginica의 경우에는 df1에 2개 df2에 2개의 데이터가 있으므로
#         - 2개와 2개의 조합에 의해 4개의 데이터가 표현된다.

# In[20]:


#양쪽 데이터프레임에서 공통된 키만 표현

df1.head(1)
df2.head(1)
pd.merge(df1,df2)
pd.merge(df1,df2, how='left')
pd.merge(df1,df2, how='right')
pd.merge(df1,df2, how='outer')


# ### merge()의 on 인수를 사용하여 기준열 명시하여 병합

# **key**
# - 두 데이터 프레임에서 이름이 같은 열은 모두 키가 될 수 있다.
# - 열이름이 같아도 키로 사용할 수 없는 열이 있으면 **on 인수로 기준열을 명시**해야 한다.

# **예제3.**

# In[24]:


# 예제 df
df1 = pd.DataFrame({
    '고객명':['춘향','춘향','몽룡'],
    '날짜' : ['2018-01-01','2018-01-02','2018-01-01'],
    '데이터':[20000, 30000, 100000]
})
df1


# In[25]:


df2 = pd.DataFrame({
    '고객명':['춘향','몽룡'],
    '데이터':['여자','남자']
})
df2


# **기준열을 직접 지정 : on=기준열 이름**
# - 반환 결과에 동일 필드명이 있을 경우에는 필드명_x, 필드명_y로 필드명을 변경해서 표현

# In[28]:


pd.merge(df1, df2, on='고객명')


# **키가 되는 기준열 이름이 두 데이터 프레임에서 다르게 나타나는 경우**
# - **left_on, right_on 인수**를 사용해서 기준열을 명시해야 함

# **예제4.**

# In[31]:


df1=pd.DataFrame({
    '이름' :['영희','철수','철수'],
    '성적' :[90,80,80]
})
df2 = pd.DataFrame({
    '성명' :['영희','영희','철수'],
    '성적2':[100,80,90]
})
df1
df2


# In[30]:


pd.merge(df1, df2, left_on='이름', right_on='성명')
# 양쪽에서 기준이되는 열의 이름이 다르기 때문에 on인수를 두번사용
# 출력결과는 양쪽 필드 명이 다르기 때문에 기준열이 모두나타난다.


# ### 인덱스 기준으로 병합
# 
# : 일반 데이터 열이 아닌 인덱스를 기준으로 merge 할수도 있음
# 
# 
# - 인덱스를 기준열로 사용하려면
#     - left_index = True 또는
#     - right_index = True 설정을 하게 됨

# **예제5. 데이터프레임의 인덱스를 기준열로 사용하는 경우**

# In[32]:


df1 = pd.DataFrame({
    '도시': ['서울','서울','서울','부산','부산'],
    '연도': [2000, 2005, 2010, 2000, 2005],
    '인구': [9853972, 9762546, 9631482, 3655437, 3512547]    
})

df2=pd.DataFrame(
    np.arange(12).reshape((6,2)),
    index=[['부산','부산','서울','서울','서울','서울'],
          [2000, 2005, 2000, 2005, 2010, 2015]],
    columns=['데이터1','데이터2']
)

df1
df2


# In[33]:


pd.merge(df1, df2, left_on=['도시','연도'], right_index=True)


# **예제6. 두 데이터프레임의 key가 모두 인덱스인 경우**

# In[34]:


df1 = pd.DataFrame([[1.,2.],[3.,4.],[5.,6.]],
                   index=['a','c','e'],
                   columns=['서울','부산'])
df1

df2=pd.DataFrame([[7.,8.],[9.,10.],
                  [11.,12.],[13.,14.]],
                 index=['b','c','d','e'],
                 columns=['대구','광주'])
df2


# **두 데이터프레임의 인덱스가 키로 사용될 경우**

# In[35]:


# 두 데이터프레임의 key가 모두 인덱스인 경우
pd.merge(df1,df2, how='outer',left_index=True, right_index=True)


# ## 2) join()을 이용한 병합

# **Dataframe1.join(Dataframe2. how='left/right/inner/outer', on=keys)**

# - 사용 방법은 merge()와 동일
# - 행 인덱스를 기준으로 결합
# 
# - Dataframe1.join(Dataframe2. how='left')가 default값

# In[36]:


df1.join(df2, how='outer')


# ### 연습문제1.
# - 두 개의 데이터프레임을 만들고 merge 명령을 병합한다.
# - 단, 데이터 프레임은 다음 조건을 만족해야 한다.
#     1. 각각 5X5 이상의 크기를 가진다.
#     2. 공통열을 하나이상 갖는다. 
#         - 다만 공통열의 이름은 서로 다르게 할 것
#     3. merge의 경우를 inner, outer, left, right 4개의 형태로 출력할 것
#     4. 지정된 인덱스와 컬럼명을 갖는다. 

# In[23]:


data = [[22, 60.1, 170.5, '남', '서울'], 
        [45, 51.3, 157.3, '여', '부산'], 
        [22, 68.3,180.1,  '남', '대구'],
        [33, 88.3, 190.2, '남', '제주'], 
        [27, 48.3, 160.1, '여', '강릉']]

df1 = pd.DataFrame(data, 
                   index=['홍길동', '이몽룡', '성춘향','변학도','김연아'], 
                   columns=["나이", "몸무게", "키", "성별" ,"주소"])
df1


# In[24]:


data = [[22, 60.1, 170.5, '남', '서울'], 
        [45, 51.3, 157.3, '여', '부산'], 
        [22, 68.3,180.1,  '남', '울산'],
        [33, 88.3, 190.2, '남', '제주'], 
        [27, 48.3, 160.1, '여', '광주']]
df2 = pd.DataFrame(data,
                   index=[1,2,3,4,5],
                   columns=["나이", "몸무게", "키", "성별" ,"지역"])
df2


# In[25]:





# ------------------------------

# ## 2. 데이터 연결
# 
# ### concat() 명령을 사용한 데이터 연결

# **pd.concat([left, right], axis=0, join='outer', ignore_index=False, keys=None)**
# 
# - left, right :  Series, DataFrame, Panel object 리스트
# - axis :  0은 위+아래로 합치기, 1은 왼쪽+오른쪽으로 합치기
# - join :  'outer': 합집합(union), 'inner': 교집합(intersection)
# - ignore_index :  False: 기존 index 유지, True: 기존 index 무시
# - keys :  계층적 index 사용하려면 keys 튜플 입력

# - 기준열 없이 데이터를 합친다
# - 위 아래로 데이터를 결합하는 **행 결합(row bind)**이 기본
# - axis 속성을 1로 설정하면 열 결합(column bind)을 수행
# - 단순히 두 시리즈나 데이터프레임을 연결하기 때문에 **인덱스 값이 중복**될 수 있다.

# #### 행결합 : pd.concat([df1,df2], axis=0)

# ![](./img/join_inout_row.PNG)

# #### 열결합 :  pd.concat([df1,df2],axis=1)

# ![](./img/concat_column.png)

# ### 두 시리즈 데이터 연결

# **예제1.**

# - 두 시리즈 데이터 생성

# In[37]:


s1=pd.Series([0,1], index=['A','B'])
s2=pd.Series([2,3,4], index=['A','B','C'])
s1
s2


# - 두 시리즈 데이터 연결

# In[38]:


# 두 시리즈 연결 : 행방향으로 합침
pd.concat([s1,s2])


# In[39]:


# 두 시리즈 연결 : 열방향으로 합침
pd.concat([s1,s2], axis=1)


# ### 두 데이터프레임 연결

# **예제2.**
# - 데이터프레임 생성

# In[40]:


# concat 연결
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'E': ['C4', 'C5', 'C6', 'C7'],
                    'F': ['D4', 'D5', 'D6', 'D7']},
                   index=[0, 1, 2, 3])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[1,2,3,4])
df1
df2
df3


# **데이터 프레임 행 결합**

# - 행을 모두 표현
# - join 인수 생략 : 기본값이 'outer'로 지정되어 있음 (모든 열 표현)

# In[44]:


result = pd.concat([df1,df2])
result


# In[42]:


pd.concat([df1,df2], join='outer')


# **인덱스가 중복된 경우 : 인덱싱을 수행하면?**

# In[50]:


# 인덱스가 중복 된 경우 인덱싱을 수행 하면 ?
result
result.loc[0]


# **인덱스가 중복되므로 기본 인덱스로 재설정**
# - 인덱스 열 제거 : drop=True

# In[52]:


# 인덱스가 중복 되므로 기본 인덱스로 재 설정
# 인덱스 열은 제거

result.reset_index(drop=True)


# **concat( , join = 'inner')**
# 
# : 공통된 열만 표현

# In[53]:


# concat() : 행결합 - 행은 모두 표현
# join='inner' 이므로 열은 공통열만 표현

pd.concat([df1,df2], join='inner')


# **concat( , ignore_index = True)**
# 
# : 기존 인덱스 제거 후 제로베이스 인덱스 설정

# In[54]:


# ignore_index = True : 기존 인덱스 제거 후 제로베이스 인덱스 설정

pd.concat([df1,df2], join='inner', ignore_index = True)


# **concat( , keys=[])**
# 
# : 상위 레벨 인덱스 설정

# In[59]:


# keys 파라미터를 통해 상위레벨 인덱스 설정 가능

result= pd.concat([df1,df2,df3], keys=['x','y','z'])
# 3개의 df이므로 각 df에 대응되는 상위 레벨 인덱스를 정의

result


# - 다중 인덱스인 경우 데이터 접근 : .연산자를 이용한 체인 인덱싱
# 

# In[61]:


# 다중 인덱싱 : . 연산자를 이용한 접근
result.loc['z'].loc[1:2]


# ### concat() 를 이용한 열 결합
# 
# **pd.concat([df1,df2], axis=1, join='inner/outer')**
# 
# - axis=1
#     - 데이터프레임들의 열을 결합
# 
# 
# - join='outer' : 기본 설정
#     - 모든 행을 표시하고 해당 행의 데이터가 없는 열의 원소는 NaN으로 표시
# 
# 
# - join='inner'
#     - 병합하는 데이터프레임에 중복되는 인덱스의 행만 표시

# <img src='./img/concat_column.png' width=300, height=250>

# **예제3.**

# In[62]:


# 예제 df 생성
df1=pd.DataFrame(
    np.arange(6).reshape(3,2),
    index=['a','b','c'],
    columns=['데이터1','데이터2']
)
df1

df2=pd.DataFrame(
    5+np.arange(4).reshape(2,2),
    index=['a','c'],
    columns=['데이터2','데이터4']
)
df2


# - concat( , axis=1, )을 이용한 열 결합 : outer join이 기본으로 적용

# In[64]:


pd.concat([df1,df2], axis=1, join='outer')
# join ='outer'가 기본이므로 생략 가능


# - concat( , axis=0, )을 이용한 행 결합

# In[65]:


# 행 결합
pd.concat([df1,df2], axis=0, join='outer')


# - inner join이 적용된 열 결합

# In[66]:


pd.concat([df1,df2], axis=1, join='inner')


# ### 연습문제2. 
# - 어느회사의 전반기(1월-6월)실적을 나타내는 데이터프레임과
# 후반기(7월-12월)실적을 나타내는 데이터 프레임을 작성한 후
# 합친다(단순병합)
# - 실적 정보는 "매출","비용","이익"으로 이루어진다.
# - 이익=매출-비용 : 가공필드로 생성
#     
# - 또한 1년간의 총 실적을 마지막 열로 덧붙인다.

# **상반기(1-6월) 실적 데이터프레임 생성**
# - month 변수 생성

# In[67]:


month = [str(i)+'월' for i in range(1,13)]
month


# - 1~6월의 매출, 비용 데이터 생성(딕셔너리)

# In[68]:


# 매출, 비용 data random  생성
np.random.seed(3)
data={}
for i in month[0:6]:
    data[i]=np.random.randint(1,100,2)
    
data


# - 1~6월의 매출과 비용 데이터프레임 생성

# In[21]:


# 데이터프레임 생성


# - '이익' 행이 추가된 데이터 프레임 작성

# In[22]:


# '이익' 행 생성 : 매출-비용


# **하반기(7~12월) 실적 데이터프레임 생성**
# - 매출, 비용으로 구성

# In[23]:


# 매출, 비용 data random  생성


# 데이터프레임 생성


# 가공 행 이익 생성


# **상반기 실적 데이터프레임과 하반기 실적 데이터프레임 연결**

# In[25]:





# - '총실적' 열 추가

# In[26]:




