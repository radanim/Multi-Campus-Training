#!/usr/bin/env python
# coding: utf-8

# # 데이터 전처리

# ![image.png](attachment:image.png)
# 
# - 출처 : R로 배우는 데이터과학, 한빛출판사

# ![image.png](attachment:image.png)

# ### 데이터 분석을 위한 데이터 정제 및 가공
# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # pandas 데이터 조작

# - 데이터 집계
#     - 빈도, 비율, 합계, 평균, 최대값, 최소값 등
# - 데이터 정렬
# - 결측치 처리
# - apply()
# - 데이터 범주화
# - 인덱스 변경

# In[1]:


# 모듈 import
import numpy as np
import pandas as pd


# In[2]:


# 설정 변경 코드
# 변수 명이 두번 이상 출력되어도 모두 콘솔에서 보여줄 것
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"

# InteractiveShell.ast_node_interactivity : 'all' | 'last' | 'last_expr' | 'none' (기본값은 'last_expr')


# # 데이터 집계

# ## 1. 데이터 개수 세기
# 
# - count() 함수 
#     - NaN값은 세지 않음
# 
# - value_count() 함수

# ### 시리즈에 count()적용하여 개수 세기

# In[3]:


# 시리즈 생성
s = pd.Series(range(10))
s[3]=np.nan  # 결측치 nan을 이용하여 NaN 저장
s


# In[4]:


# 시리즈 개수 세기
s.count() # NaN은 세지 않음


# ### 데이터 프레임에 count()함수 적용
# - 각 열마다 데이터 개수를 세기 때문에 누락된 부분을 찾을 때 유용

# **난수 발생시켜 데이터프레임 생성**

# - 참고. 난수 생성
#     - seed(값) 함수 사용하여 동일한 난수 발생
#         - seed : 난수 알고리즘에서 사용하는 기본 값
#         - seed 값이 같으면 동일한 난수 발생
#         - 예. np.random.seed(10) 
# 
#     - 계속 변경되는 난수를 생성하려면 time.time()을 사용하여 시드값이 매번 변하도록 지정
#         - 예. np.random.seed(int(time.time()))

# In[6]:


# 고정 시드값
np.random.seed(20)
np.random.randint(5, size=4)


# In[8]:


# 변경 시드값
import time

np.random.seed(int(time.time()))
np.random.randint(5, size=4)


# In[9]:


np.random.randint(5, size=4)


# - 4행 4열 실수형 데이터를 갖는 데이터 프레임 생성
#     - 데이터 0~4범위의 난수 발생

# In[10]:


np.random.seed(3)
df1 = pd.DataFrame(np.random.randint(5, size=(4,4)))
df1


# In[11]:


df1.count()


# => 데이터 프레임이므로 각 열의 원소의 갯수를 시리즈 형태로 반환

# In[12]:


# NaN 부여
df1.iloc[2,3]=np.nan
df1


# In[13]:


df1.count()


# **실전 데이터에 count() 적용**

# - 타이타닉 승객 데이터 사용
#     - seaborn 패키지 내에 data로 존재
#     - 데이터셋 읽어오기 : 패키지명.load_dataset("data명")

# In[15]:


import seaborn as sns # seaborn 패키지 : 그래프 패키지

titanic = sns.load_dataset('titanic')
titanic.head()
titanic.tail()


# In[16]:


#titanic df의 각 열의 원소 개수를 산출 - count() 함수 이용

titanic.count()


# ###  카테고리 값 세기 
# 
# - 시리즈, 데이터프레임의 범주형 데이터에 대한 **범주별 빈도(비율) 계산**
# - **value_counts( )** 함수 적용

# #### 시리즈 데이터의 빈도 계산
# - 시리즈의 값이 정수,문자열 등 카테고리 값인 경우에
# - 시리즈.value_counts()메서드를 사용해 각각의 값이 나온 횟수를 셀 수 있음
# - 파라미터 normalize=True 를 사용하면 각 값 및 범주형 데이터의 비율을 계산
#     - 시리즈.value_counts(normalize=True)

# In[17]:


# 항상 같은 값이 나오도록 생성
np.random.seed(1)


# In[18]:


# 데이터 마지막 부분 확인
s2 = pd.Series(np.random.randint(6,size=100))
s2


# In[19]:


# 데이터 길이
len(s2)


# In[20]:


# 0,1,2,3,4,5 각 값이 몇번 나왔는지 확인
s2.value_counts()


# #### 범주형 데이터에 value_counts() 함수 적용
# - 범주형 데이터 : 관측 별과가 몇개의 버무 또는 항목의 형태로 나타나는 자료
#     - ex. 성별(남,여), 선호도(종다, 보통, 싫다), 혈액형(A,B,O,AB) 등

# In[22]:


# titanic df 의 alive 열 : 생존여부가 yes/no 로 표시 되어 있음
# 문자열(Object type)
titanic['alive'].dtype
# 
titanic['alive'].value_counts()


# In[24]:


# 생존자 사망자 비율 계산
titanic['alive'].value_counts(normalize=True)
titanic['alive'].value_counts(normalize=True)*100


# #### 데이터프레임에  value_counts()  함수 사용
# 
# 
# - 행을 하나의 value로 설정하고 동일한 행이 몇번 나타났는지 반환
# - 행의 경우가 인덱스로 개수된 값이 value로 표시되는 Series 반환

# In[25]:


# 예제 df
df = pd.DataFrame({
                 'num_legs':[2,4,4,6],
                 'num_wings':[2,0,0,0]},
                index=['falcon','dog','cat','ant'])
df
# df = pd.DataFrame(np.array([2,2,4,0,4,0,6,0]).reshape(4,2),
#                            index = ['falcon','dog','cat','ant'],
#                            columns = ['num_legs','num_wings'])
# df
# df = pd.DataFrame(([2,4,4,6],[2,0,0,0]),
#                   index = ['num_legs','num_wings'],
#                   columns =['falcon','dog','cat','ant'])
# df=df.T
# df


# In[28]:


df['num_legs'].value_counts()
df.value_counts()


# In[29]:


# 예제 df
df1


# In[31]:


df1.value_counts()  # NaN은 제외


# In[34]:


df1.value_counts().sort_index()
df1.value_counts().sort_index().shape
df1.value_counts().sort_index().index


# In[37]:


# column : 시리즈 -> value_count() 적용가능
df1[0].value_counts()
df1.iloc[2,3]=np.nan
df1
df1[3].value_counts()


# ## 2. 데이터 정렬 
# 
# - 데이터 정렬을 위한 정렬 함수 사용
# - **sort_index()** : 인덱스를 기준으로 정렬
# - **sort_value()** : 데이터 값을 기준으로 정렬

# ### 2-1. 시리즈 정렬

# In[38]:


#예제 시리즈
s2


# In[40]:


# 결과 인덱스가 순서 없이 반환
s2.value_counts()

# 인덱스 기준 정렬
s2.value_counts().sort_index()


# In[41]:


# 인덱스 기준 내림차순 정렬
s2.value_counts().sort_index(ascending=False)


# In[42]:


# 값을 기준으로 오름차순 정렬
s2.value_counts().sort_values()


# In[43]:


# 값을 기준으로 내림차순 정렬
s2.value_counts().sort_values(ascending=False)


# In[44]:


s2.sort_values()


# ### 2-2. 데이터 프레임 정렬
# 
# - df.sort_values() : 특정열 값 기준 정렬
#     - 데이터프레임은 2차원 배열과 동일하기 때문에
#         - 정렬시 기준열을 줘야 한다. by 인수 사용 : 생략 불가
#         - by = 기준열, by=[기준열1,기준열2]
#     - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
#     
#     
# - df.sort_index() : DF의 INDEX 기준 정렬
#     - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)

# In[45]:


df1


# In[32]:


# df1.sort_values() #sort_values() missing 1 required positional argument: 'by'


# In[47]:


df1.sort_values(by=0)


# In[48]:


df1.sort_values(by=0, ascending=False)


# In[49]:


#1열을 기준으로 정렬, 1열 값이 동일 할때는 2열값을 기준으로 정렬
df1.sort_values(by=[1,2])


# In[50]:


# 예제 df 확인
df


# In[56]:


df.sort_values(by='num_wings')


# - 데이터프레임의 index를 기준으로 정렬

# In[53]:


# 인덱스 기준 정렬
df.sort_index()

# 인덱스 기준 내림차순 정렬
df.sort_index(ascending=False)


# ---------------------------------------------------

# ### 연습문제 
# 
# 1. 타이타닉 데이터에서 승객의 성별(sex) 인원수, 나이별(age) 인원수, 선실별(class) 인원수, 사망/생존(alive)인원수를 구하시오.
# 
# 2. 성별 인원수는 인덱스 기준으로 정렬하고, 나이별 인원수는 값 기준으로 정렬하며, 나머지는 임의 기준으로 선정하여 정렬 하시오.

# In[38]:


# 타이타닉 승객에 대하여 성별 인원수 구하기


# In[39]:


# 타이타닉 승객에 대하여 나이별 인원수 구하기


# In[40]:


# 타이타닉 승객에 대하여 선실별 인원수 구하기
#파이썬에서는 형태 분류 class로 작업


# In[41]:


#타이타닉 승객에 대하여 사망/생존 인원수 구하기


# In[42]:


#타이타닉 승객에 대하여 사망/생존 인원수 구하기
#.연산자 이용해서 data에 접근


# ------------------------------------------------------

# ## 3. 행/열의 합계
# 
# - **df.sum()** 함수 사용
# - 행과 열의 합계를 구할때는 sum(axis=0/1) - axis는 0이 기본
#     - 각 열의 합계를 구할때는 sum(axis=0)
#     - 각 행의 합계를 구할때는 sum(axis=1)

# **데이터 프레임 생성**
# 예제 DF 생성
# 4행 8열의 데이터프레임 작성, 난수를 발생시키고
# 0-9범위에서 매번 같은 난수 발생되어 반환되도록 설정
# In[57]:


np.random.seed(1)
df2 = pd.DataFrame(np.random.randint(10, size=(4,8)))
df2


# **각 행의 합계 계산**

# In[58]:


# 각 행의 합계를 구할때는 sum(axis=1)
df2.sum(axis=1)
# 시리즈 형태로 반환


# **각 열의 합계 계산**

# In[59]:


# 각 열의 합계를 구할때는 sum(axis=0)
df2.sum(axis=0)


# In[60]:


# axis인수 생략 : df.sum() : 기본값이 0이므로 열방향 합계를 구한다.
df2.sum()


# ## 4. 평균, 최소값, 최대값
# 
# - 데이터프레임에 적용되는 집계 관련 함수
#     - 평균 : mean(axis=0/1)
#     - 최소값 : min(axis=0/1)
#     - 최대값 : max(axis=0/1)

# In[61]:


# 예제 DF 확인
df2


# In[63]:


# df의 기본 함수 : min(), max(), mean()
# df2.mean()
# df2.min()
# df2.max()
df2.mean(axis=0)
df2.min(axis=0)
df2.max(axis=0)


# In[70]:


# 각 행의 합계를 새로운 열로 추가
df2['RowSum']=df2.sum(axis=1)
df2


# In[71]:


# 새로운 행 추가(loc 인덱서 사용이 가장 간단함)
# 각 열의 합계를 구한후에 행으로 추가
# 행 이름은 ColTotal
df2.loc['ColTotal']=df2.sum(axis=0)
df2


# # 데이터 삭제
# 
# - drop() 함수

# ## 행 삭제
# - df.drop('행이름',0) : 행삭제 
#      - 행삭제 후 df로 결과를 반환
# - 원본에 반영되지 않으므로  원본수정하려면 저장 해야 함

# In[66]:


# 각 행의 합계 계산
df2


# In[68]:


# - df.drop('행이름',0) : 행삭제 
#     - 행삭제 후 df로 결과를 반환
df2 = df2.drop('ColTotal', 0)
df2


# ## 열 삭제
# - df.drop('행이름',1) : 열 삭제
#      - 행삭제 후 df로 결과를 반환
# - 원본에 반영되지 않으므로  원본수정하려면 저장 해야 함

# In[69]:


# df.drop('컬럼명(열이름)',1) 열삭제 - 삭제 후 df로 반환
# 원본반영안됨
df2.drop('RowSum',1)
df2


# # 결측치 처리
# 
# : **NaN 값 처리** 함수
# 
# - **df.dropna(axis=0/1)**
#     - NaN값이 있는 열 또는 행을 삭제
#     - 원본 반영되지 않음
# 
# 
# - **df.fillna(0)**
#     - NaN값을 정해진 숫자로 채움
#     - 원본 반영 되지 않음

# ### 결측치 적용

# In[72]:


# df2에 결측치 값 적용
df2


# ### 결측치 포함 행 삭제 : dropna()

# In[73]:


df2.iloc[0,0]=np.nan
df2


# In[74]:


# NaN이 포함된 행을 삭제
df2.dropna()  # df2.dropna(axis=0)와 같음
df2


# ### 결측치 포함 열 삭제 : dropna(axis=1)

# In[75]:


#NaN이 포함된 열삭제
df2.dropna(axis=1)
df2


# ### 결측치를 다른 값으로 대체 : fillna() 함수

# In[76]:


df2


# **결측치를 0으로 변경**

# In[79]:


df2.fillna(0)


# : fillna() 적용 후 결과값은 실수가 됨 (NaN이 실수형)

# **결측치를 1로 변경**

# In[80]:


df2.fillna(1)


# In[82]:


# NaN 이 실수형이어서 fillna 후 결과값이 실수 임
# 정수 변환 함수 astype(데이터형)
df2.fillna(0).astype(int)
df2.fillna(0).astype(float)


# # 행/열에 동일한 연산 적용
# 
# - 열 또는 행에 동일한 연산 반복 적용할 때
# 
# 
# - apply() 함수
#     - DataFrame의 행이나 열에 복잡한 연산을 vectorizing 할 수 있게 해주는 함수
#     - 매우 많이 활용되는 함수
# 
# 
# - **형식 : apply(반복적용할 함수, axis=0/1)**
#     - 0 : 열마다 반복
#     - 1 : 행마다 반복 
#     - 생략시 기본값 : 0

# **데이터프레임 생성**

# In[83]:


# 예제 df 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3


# **데이터프레임의 각 열에 sum() 함수 적용**

# In[86]:


# df3의 각 열에 대해 np.sum 함수를 반복 적용
# sum함수는 열 또는 행단위로 적용되는 함수여서 각 열별로 적용 됨
# df3.sum(axis=0)
df3.apply(np.sum, 0)
# df3.apply(np.sum)


# **데이터프레임의 각 행에 sum() 함수 적용**

# In[87]:


# df3의 각 행에 대해 np.sum 함수를 반복 적용
# sum함수는 열 또는 행단위로 적용되는 함수여서 각 행별로 적용 됨
# df3.sum(axis=1)
df3.apply(np.sum, 1)


# **데이터프레임의 각 원소의 제곱값을 계산**

# In[88]:


# df3의 각 열별 모든 원소에 대하여 np.square 함수 적용(제곱값)
# square 함수는 원소에 적용이 가능 한 함수이므로 열별로 원소에 대하여 벡터화 연산을 진행
df3.apply(np.square)


# **데이터프레임의 행별로 각 원소의 제곱값을 계산**

# In[89]:


# 행별 각 원소에 대하여  np.square 함수 연산을 진행 
## 원소에 대하여 진행하는 함수여서 열/행 모두 동일한 결과
df3.apply(np.square,1)


# ## 사용자가 정의한 연산을 행/열단위 적용 : lambda() & apply()
# 
# - 데이터프레임의 기본 집계함수(sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
#     - apply() 함수를 사용할 필요가 없음
# 
# 
# - apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 또는 행에 일괄 적용시키기 위해 사용
#     - lambda 함수로 필요한 연산 기능을 구현하고, apply()를 통해 열/행 단위로 적용

# ### 1회성 함수 lambda 함수를  apply()에  사용하는 예제

# - 집합데이터의 최대값과 최소값의 차이를 구하는 lambda 함수 정의

# In[91]:


# 집합데이터의 최대값과 최소값의 차이를 구하는 lambda 함수
diff= lambda x:x.max()-x.min()


# - 정의한 lambda함수 diif() 적용

# In[92]:


# df3의 a열에 최대값과 최소값의 차이를 위에서 생성한 lambda 함수를 이용하여 구하시오
df3.apply(diff, 0)


# In[93]:


# apply 함수를 이용하여 위에서 생성한 lambda diff를 df3의 모든 행에 반복 적용하여 모든 행의 최대값과 최소값의 차이를 구하시오

df3.apply(diff, 1)


# - 직접 연산으로 통해 최대값과 최소값 차이 계산

# In[94]:


# 다른 방법 : 직접 연산
# df3의 각 열에 대하여 최대값과 최소값의 차이를 구하시오

df3.max(axis=1)-df3.min(axis=1)


# **데이터프레임 각 열의 데이터에 대한 범주별 빈도 계산**

# In[95]:


# df3의 각 열의 데이터에 대해서 카테고리 세기를 수행하시오
df3


# In[99]:


# apply()함수를 사용해서 value_counts()적용 test
# df3['a'].value_counts()
df3.apply(pd.value_counts)


# **각 열의 데이터에 대한 범주별 빈도 계산 후, NaN값은 0으로 변환하고 전체 데이터 타입을 정수로 변환**

# In[100]:


# df3 각 열 데이터의 빈도를 세고, NaN값은 0으로 변환 전체 데이터 타입을 정수로 변환하시오.
df3.apply(pd.value_counts).fillna(0).astype(int)


# # 수치형 데이터를 범주형 데이터로 변환
# 
# : 데이터값을 카테고리 값으로 변환
# 
# - 값의 크기를 기준으로 하여 카테고리 값으로 변환하고 싶을때
#     - **cut(data, bins, label)**
#         - data : 구간 나눌 실제 값
#         - bins : 구간 경계값
#         - label: 카테고리 값
#         
#     - **qcut(data, bins, label)**

# ### 1. 구간 경계선을 선정하여 범주형 데이터로 변환 : cut()

# #### 리스트 데이터를 범주형 데이터로 변환
# **구간을 나눌 실제 값 : 관측 데이터**

# In[101]:


ages=[0,0.5,4,6,4,5,2,10,21,23,37,15,38,31,61,20,41,31,100]


# **구간 경계값, 범주 리벨 설정**

# In[102]:


# 구간 경계값 설정
bins = [0, 4, 15, 25, 35, 60, 100]


# In[103]:


#label : 카테고리 명
labels = ['영유아','미성년자','청년', '중년', '장년', '노년']

# 0 < 영유아 <= 4
# 4 < 미성년자 <= 15


# **카테고리 생성 함수 cut() 적용**

# In[106]:


# 함수 적용해서 카테고리 생성
catAge = pd.cut(ages, bins, labels=labels)
catAge
list(catAge)


# In[105]:


ages


# In[107]:


type(catAge)


# **참고: Categorical 클래스 객체**
# 
# - 카테고리명 속성 : Categorical.categories
# 
# 
# - 코드 속성 : Categorical.codes 
#     - 인코딩한 카테고리 값을 정수로 갖음

# In[108]:


catAge.categories


# In[109]:


catAge.codes
# -1로 나오는 데이터는 결측치를 나타냄


# ### 데이터프레임 데이터를 범주형으로 변환

# In[110]:


# age 리스트를 이용해서 df 생성
df4 = pd.DataFrame(ages, columns=['age'])
df4


# In[112]:


df4['age_cut']=pd.cut(df4.age, bins, labels=labels)
df4


# ### 2. 데이터 개수가 같도록 데이터 분할 :  qcut()
# 
# : 구간 경계선을 지정하지 않고 데이터의 사분위수(quantile) 기준으로 분할
# 
# - 형식 : pd.qcut(data,구간수,labels=[d1,d2....])
#     
#     
#     - 예)1000개의 데이터를 4구간으로 나누려고 한다면
#         - qcut 명령어를 사용 한 구간마다 250개씩 나누게 된다.
#         - 예외)같은 숫자인 경우에는 같은 구간으로 처리한다.
# 

# **랜덤정수 20개를 생성하고 생성된 정수를 4개의 구간으로 나누시오.**
# 
# : 각 구간의 label은 Q1,Q2,Q3,Q4 로 설정

# In[113]:


# 랜덤정수 생성 : 범위 0-19, size =20
# seed 설정해서 재 실행해도 랜덤정수가 변하지 않도록 생성
# seed 설정
np.random.seed(2)

# 랜덤정수 생성
data = np.random.randint(20, size=20)
data


# In[114]:


qcutData = pd.qcut(data, 4, labels=['Q1','Q2','Q3','Q4'])
qcutData


# In[115]:


np.sort(data)


# In[116]:


#값이 겹치면 같은 구간으로 들어가게 된다.
pd.value_counts(qcutData)


# In[117]:


df5 = pd.DataFrame(data, columns=['data'])
df5['qcut']=pd.qcut(data, 4, labels=['Q1','Q2','Q3','Q4'])
df5


# ### 연습문제 : 수치형-> 범주형 데이터 생성
# 
# : 타이타닉호 승객을 사망자와 생존자 그룹으로 나누고(alive), 각 그룹에 대해 미성년자, 청년, 중년, 장년, 노년 승객의 비율을 구하시오.
# 
# - bins=[1,15,25,35,60,99]
# - labels=['미성년자','청년','중년','장년','노년']
# - 각 그룹별 비유의 전체 합은 1이 되어야 한다.

# **타이타닉 데이터셋 로딩**

# In[118]:


# 타이타닉 승객 dataset 읽어오기
import seaborn as sns 
titanic = sns.load_dataset('titanic')
titanic.head()


# In[119]:


titanic.info()


# In[120]:


titanic.count()


# **데이터 셋 분리 : 생존자 그룹과 사망자 그룹**

# In[121]:


# 사망자 그룹 데이터 프레임 추출
titanic[titanic['alive']=='no']


# In[86]:


# 생존자 그룹 데이터 프레임 추출


# **데이터 범위 설정**

# In[87]:


# 라벨과 범위 간격 설정


# In[88]:


# 범위 유효성 검사
# bins=[1,15,25,35,60,99]



#제시된 bins의 최초값 1 이하인 값 1.0과 0.42가 각
#그룹의 최소나이로 확인되므로 bins 수정
#최대나이는 74와 80으로 확인되어서 수정 필요 없음


# In[89]:


# Warning 표시 안하도록 설정
import warnings
warnings.filterwarnings('ignore')


# **범주형 데이터 생성**

# In[90]:


# 카테고리 데이터 생성


# **범주형 데이터 확인**

# In[91]:


#카테고리 데이터 확인


# **범주형 데이터 빈도 계산**

# - 사망자 그룹의 연령대별 승객수

# In[92]:


# 카테고리 데이터들의 빈도 수 계산

# 사망자그룹 계산


# 각 연령대별 승객수의 비율 계산


# 전체 비율의 합 계산


# - 사망자 그룹의 연령대별 빈도

# In[93]:





# - 생존자 그룹 빈도

# In[94]:


# 생존자그룹 계산


# - 생존자 그룹의 연령대별 빈도

# In[95]:





# ------------------------

# # 인덱스 설정

# ### 데이터프레임 인덱스 설정: set_index(), reset_index()
# 
# - 기본인덱스 : 0부터 1씩 증가하는 정수 인덱스
#     - 따로 설정하지 않으면 기존 인덱스는 데이터열로 추가 됨
#     
#     
# - set_index() : 기존 행 인덱스를 제거하고 데이터 열 중 하나를 인덱스로 설정해주는 함수
# 
# 
# - reset_index() : 기존 행인덱스를 제거하고 기본인덱스로 변경

# **데이터프레임 생성**

# In[139]:


# 예제 데이터프레임 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3


# **데이터프레임의 인덱스를 a열로 설정**

# In[140]:


# df3은 index 설정이 없어서 기본 인덱스로 생성되어 있음
# df3 데이터 프레임의 인덱스를 a 열로 설정하시오.
df3 = df3.set_index('a')
df3


# **행 인덱스를 제거하고 기본 인덱스로 설정**

# In[141]:


# df3의 행 인덱스를 제거하고 기본 인덱스로 설정하시오.
# df3.reset_index()

## 원래 index의 처리 : 설정 없으면 원 인덱스가 data로 처리

df3 = df3.reset_index(drop=True)
## 원래 index의 처리 : 원index 제거 (drop=True)
## 원본 반영되지 않으므로 반드시 저장해야 한다.


# In[142]:


df3


# **인덱스 이름 바꾸기**

# **행인덱스의 첫번째 인덱스 값을 1반으로 변경**

# In[143]:


# index 이름 바꾸기(행 인덱스)
# df3 데이터 프레임의 인덱스를 제거하고 기본 인덱스로 설정하시오.
# 단, 원 인덱스는 삭제한다.
df3=df3.rename(index={0:'1반'})
df3


# **열이름 값 변경**

# In[144]:


# 열이름(columns) 첫번째 이름 값을 학생으로 바꾸시오
# rename() 사용
# df.rename(columns={현재컬럼명:바꿀컬럼명})
df3=df3.rename(columns={'b':'학생'})
df3


# In[ ]:




