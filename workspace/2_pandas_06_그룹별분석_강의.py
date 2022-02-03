#!/usr/bin/env python
# coding: utf-8

# # pandas 피봇팅과 그룹별 분석
# 
# - 피봇팅
# - 스태킹과 언스태킹
# - 그룹별 집계, 변형, 필터

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# # 1. 피봇팅(pivoting)
# 
# - 가지고 있는 데이터원본을 원하는 형태의 가공된 정보를 보여주는 것
#     - 자료의 형태를 변경하기 위해 많이 사용하는 방법 

# ### 예.
# **왼쪽표 : 제품이 생산될 때 마다 코드, 크기, 생산 수량을 기록**

# - 피벗테이블1(오른쪽 표)
#     - **지역과 제품코드별 생산수량 요약**
# ![](./img/피벗1.png)
# 
# 
# - 피벗테이블2(오른쪽 표)
#     - **제품크기와 제품코드별로 생산수량 요약**
# ![](./img/피벗2.png)

# ### 피보팅을 위한 메소드 : pivot(), pivot_table()

# ![](./img/pivoting.png)
# 
# - 출처 : https://rfriend.tistory.com/275

# ### pivot( )
# - pandas.pivot(data, index=None, columns=None, values=None)
# - DataFrame.pivot(index=None, columns=None, values=None)

# ### pivot_table( )

# - 방법 : **두 개의 키를 사용**해서 데이터를 선택
# 
# 
# 
# - **pivot_table(data, index=None, columns=None, values=None**,
#     aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False, sort=True)
#     
#     - data : 분석할 데이터 프레임의 메서드 형식일 때는 필요하지 않음 
#         - ex1. pandas.pivot_table(df1, )
#         - ex2. df1.pivot_table()
#     - index :  **행 인덱스**로 들어갈 키열 또는 키열의 리스트
#     - columns : **열 인덱스**로 들어갈 키열 또는 키열의 리스트
#     - values : 분석할 데이터 프레임에서 분석할 열
#     - fill_value : NaN이 표출될 때 대체값 지정
#     - margins : 모든 데이터를 분석한 결과를 행으로 표출할 지 여부
#     - margins_name : margins가 표출될 때 그 열(행)의 이름`

# #### 피봇테이블을 작성할 때 반드시 설정해야 되는 인수
# - data : 사용 데이터 프레임
# - index : 행 인덱스로 사용할 필드(기준 필드로 작용됨)
# - values : 인덱스 명을 제외한 나머지 값(data)은 수치 data 만 사용함
# - aggfunc: 기본 함수가 평균(mean)함수 이기 때문에 각 데이터의 평균값이 반환

# ### 예제1. pivot() 사용

# In[3]:


data = {
    "도시": ["서울", "서울", "서울", "부산", 
           "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015",
           "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737,
           3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권",
           "경상권", "경상권", "수도권", "수도권"]
}

columns = ["도시", "연도", "인구", "지역"]

df1 = pd.DataFrame(data, columns=columns)
df1


# **피벗데이블1 : 각 도시에 대한 연도별 평균 인구**

# In[4]:


# 각 도시에 대한 연도별 평균 인구

df1.pivot('도시', '연도', '인구')

# index='도시', column='연도', value='인구', aggfunc=mean (기본값)


# **피벗테이블2: 지역별 도시에 대한 연도별 평균 인구**

# In[5]:


# 각 지역별 도시에 대한 연도별 평균 인구

df1.pivot(['지역','도시'], '연도', '인구')


# ### 예제2. 타이타닉 데이터 : pivot_table() 사용

# In[6]:


import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]
df.head()


# **피봇테이블1 : 선실등급별 숙박객의 성별 평균 나이**

# In[12]:


# 각 선실 등급별로 숙박객의 성별 평균 나이
pd.pivot_table(df, index='class', columns='sex', values='age', aggfunc='mean')


# **피봇테이블2 : 선실등급별 숙박객의 생존여부에 따른 평균 나이**

# In[13]:


# 각 선실 등급별 숙박객의 생존 여부에 따른 평균 나이
pd.pivot_table(df, index='class', columns='survived',
               values='age', aggfunc='mean')


# **피봇테이블3 : 선실등급과 성별에 대해 생존여부에 따른 나이와 티켓값의 평균과 최대값 계산**

# In[15]:


pd.pivot_table(df, index=['class','sex'], columns='survived',
               values=['age','fare'], aggfunc=['mean','max'])


# # 2. 스태킹(stacking)과 언스태깅(unstacking)
# 
# : 피벗팅과 유사하지만 계층형 인덱스의 특정 수준도 회전이 가능함
# 
# - 스태킹(stacking) : 컬럼 레이블과 그 값을 로우 인덱스와 값으로 회전시킴
# - 언스태킹(unstacking) : 로우 인덱스와 그 값이 컬럼 레이블과 값으로 회전시킴

# - DataFrame.unstack(level=- 1, fill_value=None)
#     - level : int, str, list, default=-1
#         - 언스태킹을 적용하는 레벨
#         - 기본값은 마지막 레벨 : 언스태킹 결과 항상 마지막 레벨로 이동
#     - fill_value : int, str or dict
#         - 언스태킹 결과 결측치는 NaN으로 대체
#         
#         
# - DataFrame.stack(level=- 1, dropna=True)
#     - level : int, str, list, default=-1
#         - 언스태킹을 적용하는 레벨
#         - 기본값은 마지막 레벨 : 언스태킹 결과 항상 마지막 레벨로 이동
#     - dropna : bool, default True
#         - 스태킹 결과 결측치 처리 여부, 기본값은 True로 결측치 제외

# ![](./img/stacking.png)

# ### 스태킹(stacking)

# **예제. single level columns를 갖는 데이터**

# In[16]:


# single level coloumns
df = pd.DataFrame([[0, 1], [2, 3]],
                  index=['cat', 'dog'],
                  columns=['weight', 'height'])
df


# **스태킹(stacking)**

# In[17]:


df.stack()


# **예제. multi-level columns을 갖는 데이터1**

# In[18]:


multicol = pd.MultiIndex.from_tuples([('weight','kg'),
                                      ('weight','pounds')])
df2 = pd.DataFrame([[0, 1], [2, 3]],
                  index=['cat', 'dog'],
                  columns=multicol)
df2


# **스태킹(stacking)**

# In[19]:


# 마지막 레벨로 이동
df2.stack()


# **예제. multi-level columns을 갖는 데이터2**

# In[20]:


multicol2 = pd.MultiIndex.from_tuples([('weight','kg'),
                                      ('height','m')])
df3 = pd.DataFrame([[0, 1], [2, 3]],
                  index=['cat', 'dog'],
                  columns=multicol2)
df3


# **스태킹(stacking)**

# In[21]:


# 스태킹 결과 마지막 레벨로 이동
df3.stack()


# In[22]:


# 스태킹 결과 첫번째 레벨로 이동
df3.stack(0)


# In[23]:


# 두 단계 레벨 모두 이동
df3.stack([0,1])


# **예제. multi-level columns을 갖는 데이터3**

# In[24]:


multicol2 = pd.MultiIndex.from_tuples([('weight', 'kg'),
                                       ('height', 'm')])
df4 = pd.DataFrame([[None, 1.0], [2.0, 3.0]],
                     index=['cat', 'dog'],
                     columns=multicol2)
df4


# **스태킹(stacking) 결과 결측치 처리 : dropna 인수**

# In[26]:


# 스태킹 결과 결측치 행 포함
df4.stack(dropna=False)


# In[27]:


# 스태킹 결과 결측치 행 삭제
df4.stack(dropna=True)
# df4.stack()와 같은 결과


# : row의 각 열에 모두 결측치가 있는 경우 스태킹 결과 삭제됨 

# ### 언스태킹(unstacking)

# **예제 데이터**

# In[28]:


index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),
                                   ('two', 'a'), ('two', 'b')])
s = pd.Series(np.arange(1.0, 5.0), index=index)
s


# **마지막 레벨로 언스태킹(unstacking)**

# In[29]:


s.unstack()
# s.unstack(level=-1)  # 같은 결과


# **첫번째 레벨로 언스태킹(unstacking)**

# In[30]:


s.unstack(level=0)


# # 3. 그룹 분석

# - 그룹분석(group analysis)은 피봇테이블과 달리 키에 의해서 결정되는 데이터가 여러 개 있는 경우 미리 지정한 연산을 통해 각 그룹 데이터의 대표값을 계산하는 것
# 
# 
# - 만약 키가 지정하는 조건에 맞는 데이터가 하나 이상이라서 데이터 그룹을 이루는 경우에는 그룹의 특성을 보여주는 그룹분석을 해야 함

# ### 데이터 분석을 위한 분할-적용-조합 패턴
# 
# - 분할(SPLIT) : 어떤 기준에 따라 데이터셋을 작은 조각으로 분할한다
# - 적용(APPLY) : 각 조각에 대해 독립적으로 연산을 수행한다
# - 조합(COMBINE) : 모든 결과를 다시 하나의 단위로 조합한다

# ![](./img/groupby.png)

# ### 데이터 분할(split) 작업
# - 시리즈나 데이터프레임의 **groupby() 메소드**로 수행
# - 하나 이상의 인덱스 레이블이나 컬럼명을 지정하여 이에 기초하여 연관된 값들이 그룹화 됨
# 
# 
# - 판다스에서는 **groupby() 메서드**를 사용하여 다음과 같이 그룹분석을 진행
#     - 분석하고자 하는 시리즈나 데이터프레임에 **groupby() 메서드**를 호출하여 그룹화 수행
#     - 그룹 객체에 대해 그룹연산을 수행

# ##### groupby () 메서드¶
# 
# - 데이터를 그룹 별로 분류하는 역할을 함 
# 
# - groupby() 메서드의 인수
# 
#     - 열 또는 열의 리스트
# 
#     - 행 인덱스
# 
# - 연산 결과 : 그룹 데이터를 나타내는**GroupBy 클래스 객체를 반환**
#     - 이 객체에는 그룹별로 연산을 할 수 있는 그룹연산 메서드가 있음

# ### 데이터 분할 후 각 그룹에 적용되는 작업
# 
# - 집계(aggregation) : 각 그룹의 아이템에 대한 평균이나 개수 계산
# - 변형(transform) : 그룹이나 아이템에 특정적인 계산을 수행
# - 필터링(filtering) : 그룹 단위의 계산에 기초해 불필요한 데이터 그룹 제거

# #### GroupBy 클래스 객체의 그룹연산 메소드
# 
# - size, count: 그룹 데이터의 갯수
# 
# - mean, median, min, max: 그룹 데이터의 평균, 중앙값, 최소, 최대
# 
# - sum, prod, std, var, quantile : 그룹 데이터의 합계, 곱, 표준편차, 분산, 사분위수
# 
# - first, last: 그룹 데이터 중 가장 첫번째 데이터와 가장 나중 데이터
# 
# 
# #### 그외 자주 이용되는 그룹별 연산관련 메소드
# 
# - agg, aggregate
# 
#     - 만약 원하는 그룹연산이 없는 경우 함수를 만들고 이 함수를 agg에 전달한다.
# 
#     - 또는 여러가지 그룹연산을 동시에 하고 싶은 경우 함수 이름 문자열의 리스트를 전달한다.
# 
# - describe
# 
#     - 하나의 그룹 대표값이 아니라 여러개의 값을 데이터프레임으로 구한다.
# 
# - apply
# 
#     - describe 처럼 하나의 대표값이 아닌 데이터프레임을 출력하지만 원하는 그룹연산이 없는 경우에 사용한다.
# 
# - transform
# 
#     - 그룹에 대한 대표값을 만드는 것이 아니라 그룹별 계산을 통해 데이터 자체를 변형한다.

# ![](./img/groupby2.png)

# ## 데이터 분할
# 
# 1. 단일 컬럼의 그룹화
# 2. 복수 컬럼의 그룹화
# 3. 인덱스 레벨을 이용한 그룹화

# ### 예제 데이터 준비

# In[31]:


data=pd.DataFrame({
    'key1':['A','A','B','B','A'] , 
    'key2': ['one', 'two', 'one', 'two' , 'one'],
    'data1':[1,2,3,4,5],
    'data2':[10,20,30,40,50]})
data


# ### 단일 컬럼의 그룹화

# In[32]:


groups = data.groupby(data.key1)
groups


# **groups 속성 : GroupBy클래스객체 groups의 그룹정보 확인**
# - 각 그룹의 이름을 키로 갖는 파이썬 딕셔너리를 반환
# - 딕셔너리 값은 각 그룹에 속하는 인덱스 레이블의 배열
# - Dict {group name -> group labels}

# In[33]:


groups.groups


# **ngroups 속성 : group 수 반환**

# In[34]:


groups.ngroups


# **그룹화된 결과 접근**
# - 그룹 내용 출력함수 정의 : print_groups(group_object)

# In[36]:


def print_groups(group_object):
    for name, group in group_object:
        print(name)
        print(group[:5])


# In[37]:


print_groups(groups)


# -> 각 그룹은 그룹명과 일치하는 값들의 로우들로 구성된 데이터프레임을 하나씩 포함하고 있음

# **그룹정보 groups를 데이터프레임으로 저장**

# In[38]:


pd.DataFrame(groups)


# - 첫번째 그룹 정보

# In[39]:


pd.DataFrame(groups).loc[0]


# In[41]:


pd.DataFrame(groups).loc[0].values


# - 두번째 그룹 정보

# In[42]:


pd.DataFrame(groups).loc[1]


# In[43]:


pd.DataFrame(groups).loc[1].values


# **.size() 메소드 : 각 그룹의 크기 반환**

# In[44]:


groups.size()


# **.count() 메소드 : 각 그룹의 컬럼별 아이템 개수 반환**

# In[45]:


groups.count()


# **.sum() 메소드 : 각 그룹의 컬럼별 합계 반환**

# In[46]:


groups.sum()


# **선택한 컬럼에 대한 그룹별 합계 반환1**
# - 그룹객체[컬럼명].sum()
# - 그룹객체.sum()[컬럼명]
# - 반환값은 시리즈 형식

# In[48]:


groups['data1'].sum()
groups.sum()['data1']


# In[49]:


type(groups['data1'].sum())


# **선택한 컬럼에 대한 그룹별 합계 반환2**
# - [컬럼명]리스트로 지정한 경우 : 데이터프레임 형식으로 반환
# - 그룹객체[[컬럼명]].sum()
# - 그룹객체.sum()[[컬럼명]]

# In[50]:


groups[['data1']].sum()
groups.sum()[['data1']]


# In[51]:


type(groups[['data1']].sum())


# ### 복수 컬럼의 그룹화
# 
# - .groupby( ) 메소드에 그룹명의 리스트를 전달하면 여러 컬럼에 대해 그룹화를 수행

# In[52]:


groups2 = data.groupby([data.key1, data.key2])
groups2


# **그룹정보 확인**
# - 복수 컬럼으로 된 그룹정보 : 튜플형태로 반환

# In[53]:


groups2.groups


# **그룹수 반환**

# In[54]:


groups2.ngroups


# **그룹정보 출력 : print_groups()함수 정의**

# In[55]:


print_groups(groups2)


# ### 인덱스 레벨을 이용한 그룹화
# 
# - 컬럼 대신 인덱스의 값을 사용해 그룹화

# **예제 데이터**
# - 앞의 df2를 계층형 인덱스를 갖도록 데이터 구성 변경

# In[56]:


data


# In[57]:


data2 = data.copy()
data2 = data2.set_index(['key1','key2'])
data2


# **레벨0(key1)을 사용해 그룹화**

# In[58]:


print_groups(data2.groupby(level=0))


# **레벨1(key2)을 사용해 그룹화**

# In[59]:


print_groups(data2.groupby(level=1))


# ## 그룹별 집계

# ### 참고. GroupBy객체에 적용되는 집계 관련 내장메소드
# 
# - gb.agg()
# - gb.boxplot()
# - gb.cummin()
# - gb.describe()
# - gb.filter()
# - gb.get_group()
# - gb.height()
# - gb.last()
# - gb.median()
# - gb.ngroups()
# - gb.plot()
# - gb.rank()
# - gb.std()
# - gb.transform()
# - gb.aggregate()
# - gb.count()
# - gb.cumprod()
# - gb.dtype()
# - gb.first()
# - gb.groups()
# - gb.hist()
# - gb.max()
# - gb.min()
# - gb.nth()
# - gb.prod()
# - gb.resample()
# - gb.sum()
# - gb.var()
# - gb.apply()
# - gb.cummax()
# - gb.cumsum()
# - gb.fillna()
# - gb.gender()
# - gb.head()
# - gb.indices()
# - gb.mean()
# - gb.name()
# - gb.ohlc()
# - gb.quantile()
# - gb.size()
# - gb.tail()
# - gb.weight()

# **예제 데이터 : iris**

# In[60]:


import seaborn as sns
iris = sns.load_dataset("iris")


# In[61]:


iris


# **픔종별로 그룹화**

# In[62]:


# iris 품종별로 그룹
i_groups = iris.groupby(iris.species)
i_groups


# **품종별 합계 계산**

# In[63]:


i_groups.sum()


# **품종별 평균 계산**

# In[64]:


i_groups.mean()


# **품종별 기술통계**

# In[65]:


i_groups.describe()


# In[66]:


iris.describe()


# ### [ ] 연산자를 사용해 특정 컬럼에 대한 집계 연산 수행

# In[55]:


i_groups['sepal_length'].mean()


# In[68]:


i_groups[['sepal_length','petal_length']].mean()


# In[69]:


i_groups['petal_length'].describe()


# ## 그룹별 집계 함수 : apply() / agg() , aggregate()

# ### agg() 또는 aggregate()

# - 각 그룹에 대해 집계함수를 모두 적용
# - 적용할 함수의 참조를 파라미터로 전달
# - 데이터프레임의 경우 그룹 안의 각 컬럼 데이터에 적용됨
# - 숫자 타입의 스칼라만 리턴하는 함수를 적용하는 apply()의 특수한 경우
#     - 참고. 스칼라(scalar)
#         - 하나의 수치(數値)만으로 완전히 표시되는 양
#         - 방향의 구별이 없는 물리적 수량
#         - 질량·에너지·밀도(密度)·전기량(電氣量) 따위

# **GroupBy.agg(func, *args, **kwargs)**
# 
# - func : 함수이름
#     - 내장함수는 np.sum 또는 'sum'으로 지정, 사용자정의함수는 함수이름 그대로
# - *args : 함수의 매개변수들
# - **kwargs : 함수에 들어가는 키워드 인수들

# **각 컬럼의 최대값과 최소값의 비율 계산**
# - 함수 peak_to_peak_ratio() 작성

# In[70]:


def peak_to_peak_ratio(x):
    return x.max() / x.min() # 함수 반환 값이 수치 스칼라 타입


# - 품종(그룹)별 최대값과 최소갑의 비율 계산

# In[71]:


# 품종별로 사용자 정의함수 peak_to_peak_ratio 연산 적용
i_groups.agg(peak_to_peak_ratio)


# ### agg() 메소드에 여러 함수 적용
# 
# **.agg([함수1, 함수2,...])**

# In[72]:


i_groups.agg([np.sum, np.mean])


# In[77]:


i_groups.agg(['sum', 'mean'])


# ### apply( )
# 
# : 어떤 함수나 적용 가능

# **GroupBy.apply(func, *args, **kwargs)**
# 
# - func : 함수이름
#     - 내장함수는 np.sum 또는 'sum'으로 지정, 사용자정의함수는 함수이름 그대로
# - *args : 함수의 매개변수들
# - **kwargs : 함수에 들어가는 키워드 인수들

# **Top3 산출**
# - petal_length 기준으로 Top3 항목 선택

# In[75]:


def top3_petal_length(df):
    return df.sort_values(by="petal_length", ascending=False)[:3] 

# 함수 반환값이 수치 집합


# - 품종별로 petal_length 기준의 Top3

# In[76]:


# iris.groupby(iris.species).apply(top3_petal_length)
i_groups.apply(top3_petal_length)


# - agg( )는 반환값이 수치스칼라인 경우만 사용 가능
# - apply()는 반환값이 수치 집합인 경우 적용 가능

# In[48]:


# iris.groupby(iris.species).agg(top3_petal_length) 
# 반환값이 수치 스칼라인 경우 적용 가능한데 반환값이 수치 집합 이므로 에러 발생


# - 품종별로 최대값과 최소값 비중

# In[78]:


iris.groupby(iris.species).apply(peak_to_peak_ratio) 


# **수치형자료를 대,중,소 3범주를 갖는 범주형으로 변환 : qcut()**

# In[79]:


def q3cut(s):
    return pd.qcut(s, 3, labels=["소", "중", "대"]).astype(str)


# **품종별로 petal_length를 대,중,소 3범주로 변환**

# In[80]:


iris.groupby(iris.species).petal_length.apply(q3cut)


# **품종별로 petal_length를 대,중,소 3범주로 변환된 값을 petal_length_class변수로 추가** 

# In[81]:


iris["petal_length_class"] = iris.groupby(iris.species).petal_length.apply(q3cut)
iris.head(10)
iris.tail(10)


# ----------------------------------------

# ## 그룹함수  및 피봇 테이블 이용 간단한 분석 예제

# #### 식당에서 식사 후 내는 팁(tip)과 관련된 데이터 : tips
# 
# - seaborn 패키지 내 tips 데이터셋 사용
# 
#     - total_bill: 식사대금
# 
#     - tip: 팁
# 
#     - sex: 성별
# 
#     - smoker: 흡연/금연 여부
# 
#     - day: 요일
# 
#     - time: 시간
# 
#     - size: 인원

# In[82]:


tips = sns.load_dataset("tips")
tips.tail()


# ##### 식사 대금 대비 팁의 비율이 언제 가장 높아지는가?

# - 가공 필드 생성 : 식사대금 대비 팁의 비율
#     - tip_pt = 팁 / 식사대금

# In[68]:





# In[69]:





# In[70]:





# In[72]:


# 성별 인원수를 계산


# In[73]:


# 흡연 유무에 따른 성별 인원


# In[75]:


# 흡연 유무에 따른 성별 인원을 피봇테이블로 구현


# In[78]:


# 성별 팁 비율의 평균


# In[79]:


# 흡연 유무에 따른 팁 비율의 평균


# In[77]:


# 성별과 흡연 유무에 따른 팁 비율의 평균


# ##### 여성 혹은 흡연자의 팁 비율이 조금 높고, 여성 흡연자가 팁을 많이 줌 

# In[82]:


# 평균 통계량만 확인 했으므로 다른 통계값도 확인


# ------------------------------------------------

# ## 데이터 그룹의 변형 : transform()
# 
# ### 데이터 변형의 일반적인 과정
# 
# : transform() 메소드는 데이터프레임의 모든 값에 함수를 적용하며, 다음의 특성을 갖는 새 데이터프레임을 반환한다
# 
# - 모든 그룹의 인덱스가 합쳐진 인덱스를 갖는다
# - row의 개수는 모든 그룹의 row 개수의 총합과 같다
# - 그룹화 대상이 아닌 컬럼도 함수가 성공적으로 적용된다면 결과에 포함되며, 그렇지 않은 컬럼은 삭제될 수 있다

# **예제 데이터1**

# In[83]:


trans_data = pd.DataFrame({'Label' : ['A','C','B','A','C'],
                           'Values': [0, 1, 2, 3, 4],
                           'Values2' : [5, 6, 7, 8, 9],
                           'Other': ['foo','bar','baz','fiz','buz']},
                         index=list('VWXYZ'))
trans_data


# **Label 컬럼으로 그룹화**

# In[84]:


groups = trans_data.groupby('Label')
groups


# In[85]:


print_groups(groups)


# In[86]:


groups.groups


# ### 각 값에 10을 더하는 함수를 적용해 데이터프레임 변형 수행

# In[87]:


groups.transform(lambda x:x+10)


# -> 'Label'과 'Other' 컬럼은 문자열 값들이므로 함수 적용에 실패하여 두 컬럼은 결과에서 제외됨

# ### 그룹의 평균으로 결측값 채우기

# **예제 데이터2**

# In[88]:


trans_data2 = pd.DataFrame({'Label' : list('ABABAB'),
                            'Values' : [10, 20, 11, np.nan, 12, 22]})
trans_data2


# In[91]:


groups= trans_data2.groupby('Label')
groups.groups
print_groups(groups)


# **각 그룹의 평균 계산**

# In[90]:


groups.mean()


# **결측치(Nan) 채우기**
# 
# - 그룹별 평균으로 채우기

# In[92]:


fillna = groups.transform(lambda x : x.fillna(x.mean()))
fillna


# ## 그룹 필터링 : filter()

# - 데이터그룹을 선택적으로 삭제

# **예제 데이터3**

# In[93]:


df3 = pd.DataFrame({'Label' : list('AABCCC'),
                    'Values' : [1, 2, 3, 4, np.nan, 8]})
df3


# **아이템의 개수가 지정한 최소한의 수를 넘지 않는 그룹을 제외**

# In[94]:


df3.groupby('Label').filter(lambda x:x.Values.count() > 1)


# **NaN이 하나라도 존재하는 그룹 제외**

# In[95]:


df3.groupby('Label').filter(lambda x:x.Values.isnull().sum() == 0)


# **전체 데이터셋 평균과의 차이가 2.0이 넘는 그룹 평균을 가진 그룹만 필터링**

# In[96]:


df3.groupby('Label').mean()


# In[98]:


# 그룹간 평균
gmean = df3.groupby('Label').mean().mean()


# In[100]:


df3.groupby('Label').filter(lambda x: (x.Values.mean()- gmean) > 2.0)

