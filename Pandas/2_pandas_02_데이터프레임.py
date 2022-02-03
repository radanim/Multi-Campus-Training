#!/usr/bin/env python
# coding: utf-8

# # pandas의 데이터 구조
# 
# 1. Series 데이터
# 2. 데이터 프레임

# ![pandas_dataType](img/2_pandas_데이터구조.png)

# - 출처 : https://www.kdnuggets.com/2017/01/pandas-cheat-sheet.html

# # 2. 데이터프레임

# ![pandas_datatype](img/5_dataframe.png)

# - Pandas 라이브러리에서 기본적으로 데이터를 다루는 단위는 DataFrame : spreadsheet와 같은 개념
# 
# - 이러한 형태의 데이터는 Structured Data 또는 Panel Data 또는 Tabular Data라고 부름
# 
# - pandas를 공부한다는 것은 결국 dataframe의 사용법을 익히고 활용하는 방법을 배운다는 것과 같음
# 
# - pandas를 잘 활용하면 대부분의 structured data를 자유자재로 다룰 수 있게 됨

# ### 데이터 프레임
# - 2차원 행렬 데이터에 인덱스를 붙인 것
# - 행과 열로 만들어지는 2차원 배열 구조
# - R의 데이터 프레임 에서 유래
# - 데이프레임의 각 열은 시리즈로 구성되어 있음
# - DataFrame()함수를 사용해서 생성

# ![pandas_files](img/5_pandas_files.png)

# In[2]:


import numpy as np
import pandas as pd


# ### 데이터 프레임 생성

# #### 리스트로 데이터 프레임 만들기
# 
# - DataFrame([[list1],[list2]]) 
# - 각 list는 한 행으로 구성됨
# - 행의 원소 개수가 다르면 None 값으로 저장

# In[3]:


# 2차원 리스트로 데이터프레임 생성
df = pd.DataFrame([['a','b','c'],['a','a','g'],['a','a']])
df


# **자동으로 생성된 index와 column을 갖는 DataFrame 데이터**
# ![DataFrame](./img/5_dataFrame2.png)

# #### 딕셔너리로 데이터프레임 생성
#  - dict의 key -> column

# In[4]:


# 열방향 인덱스(문자) 행방향 인덱스(숫자)가 있는 데이터 프레임 생성
# 열 데이터를 dict 형태로 작성하는게 일반적

df1 = pd.DataFrame({'A':[90, 80, 70],
                    'B':[85, 98, 75],
                    'C':[88, 99, 77],
                    'D':[87, 89, 86]})
df1


# In[5]:


# 딕셔너리로 데이터 프레임 생성
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}
data


# In[6]:


# 열방향 인덱스 columns=
columns=['지역','2015','2010','2005','2000','2010-2015 증가율']

# 행방향 인덱스 index =
index=['서울','부산','인천','대구']

# DataFrame(데이터,index=,columns=)
df2 = pd.DataFrame(data, index=index, columns=columns)
df2


# #### 시리즈로 데이터 프레임 생성
#  - 각 Series의 인덱스 -> column

# In[7]:


a=pd.Series([100, 200, 300], ['a','b','d'])
b=pd.Series([101, 201, 301], ['a','b','k'])
c=pd.Series([110, 210, 310], ['a','b','c'])

pd.DataFrame([a,b,c], index=[100,101,102])


# #### csv 데이터로 부터 Dataframe 생성
#  - 데이터 분석을 위해, dataframe을 생성하는 가장 일반적인 방법
#  - 데이터 소스로부터 추출된 csv(comma separated values) 파일로부터 생성
#  - pandas.read_csv() 함수 사용

# In[8]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data

trainData = pd.read_csv('./data/train.csv')
trainData.head()


# #### read_csv() 함수 파라미터
#  - sep : 각 데이터 값을 구별하기 위한 구분자(separator) 설정 
#  - header : header를 무시할 경우, None 설정
#  - index_col : index로 사용할 column 설정
#  - usecols : 실제로 dataframe에 로딩할 columns만 설정

# In[9]:


trainData = pd.read_csv('./data/train.csv', 
                       index_col='PassengerId',
                       usecols=['PassengerId','Survived','Pclass', 'Name'])
trainData


# In[10]:


# 데이터프레임 열인덱스
trainData.columns


# ### 인덱스와 컬럼의 이해
# 
# 1. 인덱스(index)
#  - index 속성
#  - 각 아이템을 특정할 수 있는 고유의 값을 저장
#  - 복잡한 데이터의 경우, 멀티 인덱스로 표현 가능
#  
#  
# 2. 컬럼(column)
#  - columns 속성
#  - 각각의 특성(feature)을 나타냄
#  - 복잡한 데이터의 경우, 멀티 컬럼으로 표현 가능

# In[11]:


df2


# **데이터프레임의 열방향 인덱스와 행방향 인덱스**
# ![image.png](attachment:image.png)

# In[13]:


# 열방향 인덱스 출력
df2.columns


# In[14]:


# 행방향 인덱스 출력
df2.index


# #### 행/열 인덱스 이름 설정
# - index.name 
# - columns.name

# In[15]:


#시리즈처럼 dataFrame에서도 각 방향 인덱스에 name 속성을 지정할 수 있음
df2.index.name = '도시'
df2.columns.name = '특성'
df2


# **데이터프레임의 값 접근 : values 속성**

# In[16]:


# 데이터만 접근 하려면 values 속성을 사용

df2.values
# 반환값은 array 형태


# ### 데이터프레임의 데이터 파악하기
#  - shape 속성 (row, column)
#  - describe() 함수 : 숫자형 데이터의 통계치 계산
#  - info() 함수 : 데이터 타입, 각 아이템의 개수 등 출력

# In[17]:


# DataFrame의 개요 출력
df2.info()


# - describe(): DataFrame의 숫자형 데이터의 기술통계 출력

# In[18]:


# DataFrame의 기술통계 출력 : 수치형 데이터에 대하여
df2.describe()


# - shape : 데이터프레임의 행,렬 개수 출력

# In[19]:


#(행,열)의 개수 출력
df2.shape


# ### 데이터 프레임 전치

# - pandas의 데이터 프레임은 전치를 포함해서 Numpy 2차원 배열의 대부분 속성이나 메서드를 지원.
# 
# - 전치 : 행과 열을 바꾸는 기능

# In[20]:


# data 확인
df2 


# In[21]:


# df2 전치 : .T 속성
dfT = df2.T
dfT
# 원본데이터를 변경하지 않는다.


# ### 데이터 프레임 내용 변경
# 
# : 열추가, 열삭제, 내용 갱신

# In[22]:


# 사용 예제 
df2


# #### 해당열이 있으면 내용 갱신, 열이 없으면 추가
# - 열추가 : df[열이름(key)]=values
# - 열 내용 갱신 : df[열이름(key)]=values

# In[23]:


# 열 내용 변경 : 증가율을 퍼센트값으로 변경
df2['2010-2015 증가율'] = df2['2010-2015 증가율']*100
df2


# In[24]:


# 열 추가
df2['2005-2015 증가율']=((df2['2015']-df2['2005'])/df2['2005']*100).round(2)
df2


# In[29]:


p = ((df2['2015']-df2['2005'])/df2['2005']*100).round(2)
df2['2005-2015 증가율(%)']=p.map('{}%'.format)
df2


# In[25]:


# 열삭제, del df[삭제열]

del df2['2010-2015 증가율']
df2


# ### 데이터 프레임 인덱싱
# 1. 열인덱싱
# 2. 인덱서를 사용하지 않는 행 인덱싱
# 
# - [ ]기호를 이용해서 인덱싱할 때 주의점 : [ ]기호는 열 위주 인덱싱이 원칙

# #### 1. 열인덱싱
# 
# - 열 라벨(컬럼명)을 키값으로 생각하고 인덱싱한다.
#     - 인덱스로 라벨값을 하나 넣으면 시리즈 객체가 반환
#     - 라벨의 배열이나 리스트를 넣으면 부분적 df 가 반환

# In[30]:


# 인덱스로 라벨값 1 개 사용
df2['지역']


# In[31]:


# 열 1개를 접근할때는 . 연산자 사용 가능 : df.컬럼명
df2.지역


# In[32]:


# 지역 컬럼 데이터유형 확인
type(df2['지역'])
# pandas.core.series.Series


# In[33]:


# 열을 추출할 때 df로 반환받고자 하면 []를 사용
# 리스트로 인덱싱 : df로 반환

df2[['지역']]


# In[34]:


# pandas.core.frame.DataFrame
type(df2[['지역']])


# In[35]:


# 여러 개의 열을 추출
# []리스트 사용 : df 반환

df2[['2010','2015']]


# #### pandas 데이터 프레임에 열이름(컬럼명)이 문자열일 경우에는
# - 수치 인덱스를 사용할 수 없음
# - 위치 인덱싱 기능을 사용할 수 없음 : keyerror 발생

# In[36]:


df2[1]


# In[37]:


# 위치적으로 맨 처음 열을 반환받기 위해 위치 인덱스 사용
try : 
    df2[0] # keyerror 발생
except Exception as e :
    print(type(e))

# df2에는 컬럼명에 0 이 없음 : 위치인덱스 사용 불가


# - 위치 인덱싱처럼 보이는 예제

# In[29]:


# 예제 df3 생성
# numpy의 arange 함수 사용해서 0-11범위의 정수 생성 후 
# reshape 함수 이용하여 3행 4열로 배치


# In[38]:


df3 = pd.DataFrame(np.arange(12).reshape(3,4))
df3


# In[39]:


# 컬럼명이 숫자로 되어 있는 df의 접근
df3[0]


# In[40]:


df3[[1,2]]


# #### 2. 행 단위 인덱싱
# - 행단위 인덱싱을 하고자 하면 인덱서라는 특수 기능을 사용하지 않는 경우 슬라이싱을 해야 함(인덱서는 바로 뒤에 배움)
# - 인덱스 값이 문자(라벨)면 문자슬라이싱도 가능하다.

# In[41]:


# 예제 데이터프레임
df2


# In[42]:


# 1행 추출 [:1] - 슬라이싱 사용

df2[:1]


# In[43]:


# 1행 추출
df2[0:1]


# In[44]:


# [시작값:끝값+1]

df2[1:3]


# In[46]:


# 행 인덱스 '서울'부터 '부산'까지 추출

df2['서울':'부산']


# #### 3. 개별요소 접근 [열][행]

# In[47]:


df2['2015']['서울']


# In[48]:


# 원소값의 형태가 출력 - 정수
type(df2['2015']['서울'])


# In[49]:


df2['2015']['서울':'부산']


# In[53]:


df2[['2015','2010','2005']]['서울':'부산']


# - 데이터프레임은 열기준으로 접근 원칙 : [열이름]
# - 행기준 접근을 위해서는 슬라이싱을 적용 : [행이름:행이름]
# - 행과열을 같이 적용(개별요소) : [열이름][행이름]
