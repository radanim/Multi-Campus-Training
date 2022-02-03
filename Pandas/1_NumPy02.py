#!/usr/bin/env python
# coding: utf-8

# <img src='img/1_numpy.png' width=50 style='float:left'>
# 
# # NumPy 연산과 인덱싱

# - 배열 연산
# - 통계,수학, 행렬 연산
# - 인덱싱과 슬라이싱

# **numpy 모듈 선언**

# In[1]:


import numpy as np


# # Array 연산

# ## 기본 연산(합, 차, 곱, 나눗셈 등) 
# 
# : 기본적으로 동일한 크기의 array 간 연산 수행

# In[52]:


arr1 = np.array([[1,3,4], [4,3,6]])
arr1


# In[53]:


arr2 = np.array([[10,11,12],[13,14,15]])
arr2


# **배열의 합**

# In[54]:


arr1 + arr2


# **배열의 차**

# In[55]:


arr1 - arr2


# **배열의 곱**

# In[56]:


arr1 * arr2


# **배열의 나눗셈**

# In[57]:


arr1 / arr2


# **배열의 스칼라 곱**

# In[58]:


arr2 * 2


# **배열의 비교 연산**

# In[59]:


arr2 > 20


# ## 배열의 Broadcasting 
# - 서로 크기가 다른 array들의 연산이 가능하도록 배열을 자동적으로 변환하여 연산 수행

# In[60]:


arr1


# In[61]:


arr3 = np.array([10,11,12])
arr3


# In[62]:


arr1 + arr3


# In[63]:


arr1 * 10


# In[64]:


arr1 ** 2


# **브로드캐스팅이 일어날 수 있는 조건**
# - 두 배열 간의 연산에서 최소한 하나의 배열의 차원이 1인 경우(0번 축이든 1번 축이든; 1행이든 1열이든)
# - 차원의 짝이 맞을 때(차원에 대해 축의 길이가 동일하면)

# ![image.png](attachment:image.png)
# 출처: http://www.astroml.org/book_figures/appendix/fig_broadcast_visual.html

# ##  통계를 위한 연산

# - 배열의 합, 평균, 표준편차, 분산, 최소값, 최대값, 누적합, 누적곱 등
# - https://numpy.org/doc/stable/reference/routines.statistics.html

# In[2]:


arr1 = np.arange(5)
arr1


# In[3]:


# 합과 (산술)평균 : sum(), mean()
[arr1.sum(), arr1.mean()]


# In[4]:


# 표준편차와 분산 : std(), var()
[arr1.std(), arr1.var()]


# In[5]:


# 최소값과 최대값 : min(), max()
[arr1.min(), arr1.max()]


# In[6]:


# 누적합과 누적곱
arr2 = np.arange(1,5)
arr2


# In[8]:


# 누적합 : cumsum()
arr2.cumsum()


# In[9]:


# 누적곱 : cumprod()
arr2.cumprod()


# ## 행렬 연산

# - 선형 대수(Linear algebra)를 위한 행렬(2차원 배열) 연산
# - 행렬 곱, 전치 행렬, 역행렬, 행렬식 등
# 
#     - 행렬곱(matrix product)  : A.dot(B) 혹은 np.dot(A,B)
#     - 전치행렬(transpose matrix) : A.transpose() 혹은 np.transpose(A)
#     - 역행렬(inverse matrix) : np.linalg.inv(A)
#     - 행렬식(determinant) : np.linalg.det(A)

# In[11]:


A = np.arange(1,5).reshape(2,2)
# A = np.array([[1,2],[3,4]])
# A = np.array([1,2,3,4]).reshape(2,2)
A


# In[13]:


B = np.array([3,2,0,1]).reshape(2,2)
B


# **행렬의 곱**

# In[15]:


# 행렬의 곱
A.dot(B)  


# In[16]:


np.dot(A,B)


# **전치행렬**

# In[17]:


# 전치행렬
A.transpose()


# In[18]:


# 전치행렬
np.transpose(A)


# **역행렬**

# In[19]:


# 역행렬(inverse)
np.linalg.inv(A)


# In[20]:


# 행렬식(determinant)
np.linalg.det(A)


# In[21]:


# A * inv(A) = I (단위행렬)
np.dot(A, np.linalg.inv(A))


# ## Array 인덱싱(indexing)과 슬라이싱(Slicing)

# - 인덱싱(indexing) : 배열의 위치나 조건을 지정해 배열의 원소를 선택하는 것
# - 슬라이싱(slicing) : 범위를 지정해 배열의 원소를 선택하는 것
#     - : 연산자를 주로 사용

# ### 1차원 배열의 인덱싱
# 
# **배열명[위치]**
# 
# 
# - 파이썬의 인덱싱과 동일
# - 0번째로 시작함

# In[22]:


arr1 = np.arange(10)
arr1


# In[23]:


# 0번째 요소
arr1[0]


# In[24]:


# 3번째 요소
arr1[3]


# **배열명[[위치1, 위치2, ... ,위치n]]** 

# In[26]:


# 1, 3, 4, 위치 : 
# shape : (m, ) => 1차원, (m, n) => 2차원,  (m, n, p) => 3차원
# 인덱스 [ ]  : [m] => 1차원,  [m,n] => 2차원,  [m,n,p] => 3차원
# arr1[[1,3,4] => 3차원 배열의 위치 1면 3행 4열
# 여러 인덱스의 요소드를 지정 : 리스트로 주어야 한다
arr1[[1,3,4]]


# ### 2차원 배열의 인덱싱
# **배열명[행위치, 열위치]**

# In[29]:


arr2 = np.arange(1,13).reshape(3,4)
arr2


# In[31]:


# 2차원의 array에서 인덱싱을 하기 위해선 2개의 인자를 입력해야 합니다.
arr2[2,3]  # 2행3열의 요소


# In[33]:


# 0행0열 값 변경
arr2[0,0]=90


# In[34]:


# 변견된 array
arr2


# **2차원배열명[행위치]**
# 
# : 2차원 배열에서 지정한 행 전체가 선택됨

# In[36]:


# 두번째 행(1행) 선택
arr2[1]


# **2차원배열명[:,열위치]**
# 
# : 2차원 배열에서 지정한 열 전체 선택

# In[38]:


# 1열 선택 : 
arr2[:,1]


# **2차원 배열의 특정 행을 지정해서 행 전체를 변경**

# In[39]:


# 두번째 행 변경
arr2[1] = np.array([-5, 1, 10, 9])


# In[40]:


# 변경된 배열 확인
arr2


# **배열명[[행위치1, 행위치2, ..., 행위치n],[열위치1, 열위치2,...,열위치n]]**
# 
# : 지정한 (행위치1, 열위치1), (행위치2, 열위치2), ... ,(행위치n, 열위치n)의 원소를 가져옴 

# In[41]:


arr2[[0,2],[0,1]]


# ### 배열명[조건]
# 
# : 배열에서 조건을 만족하는 원소만 선택

# - 10 이상인 원소 선택

# In[42]:


# 비교 연산
arr2 > 10


# In[43]:


# 비교연산 결과를 인덱스로 지정
arr2[arr2 > 10]


# In[46]:


# 짝수인 원소 선택
arr2[arr2 % 2 == 0]


# ### 1차원 배열의 슬라이싱(Slicing)

# **배열[시작위치:끝위치]**
# 
# : 시작위치에서 끝위치-1 에 해당하는 배열의 원소를 반환

# In[47]:


arr1


# In[48]:


# 3번째 요소부터 8번째 요소
arr1[3:9]


# **배열[start:end+1:step]**
# 
#   : start에서 end 범위까지의 자료 중 step 간격의 인덱스를 지정

# In[49]:


arr1[3:9:2]
# arr1[[3, 5, 7]]와 같음


# In[50]:


arr1[:9:2]


# In[51]:


arr1[3::2]


# In[52]:


arr1[::3]


# In[53]:


arr1[::-1]


# In[54]:


arr1[::-2]


# **배열[:끝위치]**
# 
# : 처음부터 '끝위치-1' 원소 반환

# In[55]:


arr1[:3]


# **배열[시작위치:]**
# 
# : 시작위치부터 마지막 원소까지 반환

# In[56]:


arr1[2:]


# **배열[:]**
# 
# : 모든 원소 반환

# In[57]:


arr1[:]


# ### 2차원 배열의 슬라이싱

# **배열[행시작위치:행끝위치, 열시작위치:열끝위치]**

# In[58]:


arr2


# In[59]:


# 2행의 모든 요소 꺼내기
arr2[2,:]


# In[60]:


arr2[2]


# In[61]:


# 3열의 모든 요소 꺼내기
arr2[:,3]


# In[62]:


# 1~2행, 1~2열의 요소 
arr2[1:3, 1:3]


# **배열[행위치][열시작위치:열끝위치]**
# 
# : 특정 행을 선택한 후 열을 슬라이싱

# In[63]:


arr3 = np.arange(10,100, 10).reshape(3,3)
arr3


# In[65]:


# 1행의 0열과 1열 요소 선택
# arr3[1,:2]
arr3[1][:2]


# In[66]:


# 참고. 인덱싱 예
arr3[2][1]


# **슬라이싱 된 배열에 값을 지정**

# In[71]:


# 0~1행, 1~2열의 요소 변경
arr3[:2, 1:3]=np.array([[1,3],[4,1]])
arr3


# ## Array boolean 인덱싱(Mask)

# - 다차원의 인덱싱을 응용하여 boolean 인덱싱
# - boolean인덱싱을 통해 만들어낸 array를 통해 원하는 행 또는 열의 값만 뽑아냄
# - 가리고 싶은 부분은 가리고, 원하는 요소만 꺼냄

# In[72]:


names = np.array(['Beomwoo','Beomwoo','Kim','Joan','Lee','Beomwoo',
                  'Park','Beomwoo'])
names


# In[73]:


# names 크기 확인
names.shape


# In[74]:


# 8행4열의 실수 난수 배열 생성
data = np.random.randn(8,4)
data


# In[75]:


# 배열 크기 확인
data.shape


# In[77]:


# 요소가 Beomwoo인 항목에 대한 mask 생성
names_mask_Beomwoo=(names == 'Beomwoo')
names_mask_Beomwoo


# In[79]:


# 요소가 Beomwoo인 항목의 위치와 같은 행의 자료 가져오기
data[names_mask_Beomwoo, :]
# data[names_mask_Beomwoo] : 같은 결과


# In[81]:


# 요소가 Kim인 행의 데이터만 꺼내기
data[names=='Kim',:]


# In[89]:


# 논리 연산을 응용하여, 요소가 Kim 또는 Park인 행의 데이터만 꺼내기
data[(names == 'Kim') | (names == 'Park')]


# **마스크 인덱싱 문제**
# 
# - 문제1. data array에서 0번째 열이 0보다 작은 행 데이터 가져오기

# In[86]:


# 1단계. 마스크를 만든다.
#       data array에서 0번째 열이 0보다 작은 요소의
#       boolean 값을 선택하기 위하 마스크
data[:,0] < 0


# In[87]:


# 2단계. 생성된 마스크를 이용하여 0번째 열의 값이 0보다 작은 행을 구한다.
data[data[:,0]<0]


# - 문제2. data array에서 0번째 열이 0보다 작은 행의 2, 3번째 열 데이터 가져오기

# In[95]:


# 1. 마스크 생성 : 0번째 열의 값이 0보다 작은 행의 2,3번째 열 값
# data[data[:,0]<0][:, 2:4]
# data[data[:,0]<0, 2:4]
mask = data[:,0]<0
mask


# In[96]:


# 2. 생성된 마스크로 데이터 가져오기
data[mask, 2:4]


# ## array에 적용되는 다양한 함수

# ### 하나의 array에 적용되는 함수

# **random.randn(d0,d1,.., dn) : 표준정규난수 생성**
# 
# : https://numpy.org/doc/stable/reference/random/legacy.html

# In[99]:


# 5행3열의 실수난수 배열 생성
data = np.random.randn(5,3)
data


# **수학 관련 함수**
# 
# - 제곱근, 절대값, 삼각함수, 지수로그함수, 반올림함수 등
# 
# https://numpy.org/doc/stable/reference/routines.math.html

# In[100]:


# 각 성분의 절대값 계산하기
np.abs(data)


# In[103]:


# 각 성분의 제곱근 계산하기 : data**0.5
np.sqrt(np.abs(data))


# In[104]:


# 각 성분의 제곱 계산하기
np.square(data)


# **지수함수**

# In[105]:


# 각 성분을 자연대수 e의 지수로 삼은 값을 계산하기 : e^x
np.exp(data)


# **로그함수**
# 
# - 자연로그 : log()
# - 상용로그 : log10()
# - 밑이2인 로그 : log2()

# In[106]:


# 자연로그
np.log(abs(data))


# In[107]:


# 상용로그
np.log10(abs(data))


# In[108]:


# 밑이 2인 로그
np.log2(abs(data))


# **각 성분의 부호 계산 : sign()**
# 
# : +인 경우 1, -인 경우 -1, 0인 경우 0

# In[109]:


# 각 성분의 부호 계산하기(+인 경우 1, -인 경우 -1, 0인 경우 0)
np.sign(data)


# **반올림 함수**

# In[110]:


data


# In[111]:


# 각 성분의 소수 첫 번째 자리에서 내림한 값을 계산하기
np.floor(data)


# **NaN 여부 확인**

# In[112]:


# 각 성분이 NaN인 경우 True를, 아닌 경우 False를 반환하기
np.isnan(data)


# In[115]:


# 로그변환한 배열 중 Nan 확인
np.isnan(np.log(data))


# **무한대(inf) 확인**

# In[116]:


#각 성분이 무한대인 경우 True를, 아닌 경우 False를 반환하기
np.isinf(data)


# **삼각함수**
# 
# : 각 성분에 대해 삼각함수 값을 계산하기(cos, cosh, sin, sinh, tan, tanh)

# In[117]:


# cos() 
np.cos(data)


# In[119]:


# tan()
np.tan(data)


# **Sums, products, differences함수**

# In[120]:


data


# In[121]:


# 전체 성분의 합을 계산
np.sum(data)


# In[122]:


# 같은 열을 갖는 행의 요소들을 합한 결과(axis=0)
np.sum(data, axis=0)


# In[123]:


# 같은 행을 갖는 열의 요소들을 합한 결과(axis=1)
np.sum(data, axis=1)


# **평균(mean), 표준편차(std), 분산(var)**

# In[124]:


# 전체 성분의 평균 계산
np.mean(data)


# In[127]:


# 행별로 평균 계산 axis=1
np.mean(data, axis=1)


# In[128]:


# 열별로 평균 계산 axis=0
np.mean(data, axis=0)


# In[129]:


# 전체 성분의 표준편차 계산
np.std(data)


# In[130]:


# 열별 표준편차 계산
np.std(data, axis=0)


# In[131]:


# 행별 표준편차 계산
np.std(data, axis=1)


# **최대값(max), 최소값(min)**

# In[132]:


# 열방향에서 최소값
np.min(data, axis=0)


# **최대값, 최소값 위치 인덱스 : argmax(), argmin()**

# In[133]:


data


# In[136]:


# 전체 성분의 최소값, 최대값이 위치한 인덱스를 반환(argmin, argmax)
[np.argmax(data), np.argmin(data)]
# [np.max(data), np.min(data)]


# In[138]:


# 행방향으로 최대값이 위치한 인덱스 반환
np.argmax(data, axis=1)


# **누적합(cumsum), 누적곱(cumprod)**

# In[139]:


# 맨 처음 성분부터 각 성분까지의 누적합 또는 누적곱을 계산(cumsum, cumprod)
np.cumsum(data)


# In[141]:


data


# In[140]:


# 열기준 누적합
np.cumsum(data, axis=0)


# In[142]:


# 누적곱
np.cumprod(data)


# In[143]:


np.cumprod(data, axis=1)


# In[145]:


data


# In[144]:


# 전체 성분에 대해서 오름차순으로 정렬
np.sort(data)


# In[146]:


# 전체 성분에 대해서 [::-1]를 적용 : 정렬 후 마지막행부터 표시
np.sort(data)[::-1]


# In[148]:


data


# In[149]:


# 행방향으로 오름차순으로 정렬
np.sort(data, axis=1)


# In[147]:


# 열방향으로 오름차순으로 정렬
np.sort(data, axis=0)


# ### 두 개의 array에 적용되는 함수

# In[153]:


data1 = np.random.randn(5,3)
data2 = np.random.randn(5,3)


# In[155]:


# 5행3열의 실수난수 배열 생성
print(data1)
print(data2)


# **두 개의 array에 대해 동일한 위치의 성분끼리 연산**
# 
# - add(), subtract(), multiply(), divide()

# In[156]:


# 두 배열의 합
np.add(data1, data2)


# In[157]:


# 두 배열의 차
np.subtract(data1, data2)


# In[158]:


# 두 배열의 곱
np.multiply(data1, data2)


# In[159]:


# 두 배열의 나누기
np.divide(data1, data2)


# - 최대값 또는 최소값 계산
# : maximum(), minimum()

# In[160]:


# 두 개의 array에 대해 동일한 위치의 성분끼리 비교하여 
# 최대값 또는 최소값 계산하기(maximum, minimum)
np.maximum(data1, data2)


# In[161]:


# 최대값 또는 최소값 계산하기(maximum, minimum)
np.minimum(data1, data2)

