#!/usr/bin/env python
# coding: utf-8

# # t-검정

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats

get_ipython().run_line_magic('precision', '3')
np.random.seed(1111)


# ### 가설검정 과정
# ![image.png](attachment:image.png)

# - One Sample t-test
#     - 정규성 가정
#     - stats.ttest_1samp()
# - Two Sample t-test
#     - 정규성, 등분산성 가정
#     - 등분산 stats.ttest_ind(a,b, equal_var=True)
#     - 이분산 stats.ttest_ind(a,b, euqal_var=False)        
#     - 정규성 만족하지 않는 경우: Mann-Whitney rank test
#         - stats.mannwhitneyu(a,b)
#         
# - Paied Sample t-test
#     - 정규성 만족 : stats.ttest_1samp(a, b, popmean=모집단평균)
#     - 정규성 만족하지 않는 경우 : Wilcoxon signed-rank test
#         - stats.wilcoxon(before, after)    

# ### p-value란?
# 
# - 귀무 가설이 참이라고 했을 때 표본 데이터가 수집될 확률
# - P-value가 낮을 수록 대립가설 채택
# - 통상적으로 p-value < 0.05 면 대립가설 채택
# - 이때 0.05를 유의 수준이라고 하며 대게 0.05 또는 0.01 중 선택 

# ## t-test와 관련된 검정

# <img src='./img/T검정.png' width=500 height=500>

# #### 단일 표본 t 검정 - sample은 정규성을 띈다
# 
# - 목적 : 그룹의 평균이 기준값과 차이가 있는지를 확인
# 
# - 귀무가설 : sample의 평균과 모집단의 평균은 같다
# - 대립가설 : sample의 평균과 모집단의 평균은 다르다
# 
# - 가설 수립 예시 : 한 사이트를 운영하고 있는데 고객이 웹사이트에서 체류하는 평균시간이 10분이지 아닌지를 알고 싶어 가설 수립
# 
# ![image.png](attachment:image.png)

# ####  선행조건
# 
# - 해당 변수가 정규분포를 따라야 함 : 정규성 검정이 선행되어야 함
#     - 단, 샘플수가 많을수록 정규성을 띌 가능성이 높아지므로, 샘플수가 보족한 경우에만 정규성 검정을 수행
#     - 만약, 정규성을 띄지 않으면 비모수적인 방법인 부호검정 을 진행
#     
#     
# #### t 통계량
# 
# ![image.png](attachment:image.png)

# <img src='./img/단일표본t검정표.png' width=500 height=300 >

# #### 정규성 검정 방법
# 
# 1. Kolmogorov-Smornov Test
#     - KS test라 함 
#     - 관측한 샘플들이 특정 분포를 따르는지 확인 하기 위한 검정 방법
#     - KS test는 특정 분포를 따른다면 나올 것이라 예상되는 값과 실제 값의 차이가 유의한지를 확인하는 방법
#     - 해당분포를 정규분포로 설정하여 정규성 검정에도 사용
#     - scipy.stats.kstest(x, 'norm')
#     
#     
# 2. Shapiro-Wilk test
#     - 정규성 검정을 위해 많이 사용
#     - 양적 데이터 5000개 미만의 경우
#     - scipy.stats.shapiro(x)
# 
# 
# 3. Anderson-Darling Test
#     - 양적 데이터 5000개 이상의 경우
#     - scipy.stats.anderson(x, dist='norm')    

# ### 대응표본 t-test

# - 근력 운동 전후 집중력 비교
# - 귀무가설 : 전과 후에 차이가 없다
# - 대립가설 : 전과 후에 차이가 있다

# In[2]:


# 대응표본 샘플데이터 
data = pd.read_csv('./data/ch11_training_rel.csv')
print(data.shape)
data.head()


# In[19]:


# 기술통계
data.describe()


# In[15]:


# 데이터의 시각화 : 상자그림표
import matplotlib.pyplot as plt

plt.boxplot(data)
plt.show()


# **정규성 검정**

# In[12]:


# 정규성 검정
stats.shapiro(data.전)


# In[13]:


stats.shapiro(data.후)


# In[20]:


diff = data.전 - data.후
diff


# In[21]:


stats.shapiro(diff)


# In[22]:


plt.boxplot(diff)
plt.show()


# **대응표본 t 검정 수행**

# In[18]:


stats.ttest_1samp(data.전-data.후, 0)


# => 귀무가설을 기각하므로, 근력운동이 집중력에 영향이 있다고 볼 수 있다.

# ### 독립 표본 t 검정
# - 독립된 두 집단의 평균 비교
# 
# - 귀무가설 : 두 집단의 평균은 같다
# - 대립가설 : 두 집단의 평균은 차이가 있다

# #### 선행조건
# 
# - 독립성 : 두 그룹은 서로 독립적이어야 함
# - 정규성 : 데이터는 정규분포를 따라야 함
#     - 만약, 정규성을 띄지 않으면 비모수적인 방법인 부호검정 을 진행
#     
# - 등분산성 : 두 그릅의 데이터에 대한 분산이 같아야 함
#     - Levene의 등분산 검정 : p-value가 0.05 미만이면 분산이 다르다고 판단
#     - 분산이 같은지 다른지에 따라 사용하는 통계량이 달라지므로, 설정을 달리 한다
#     
# <img src='./img/독립t등분산.png' width=500 height=300 >
# <img src='./img/독립표본t이분산.png' width=500 height=300 >

# - 반별 점수 차가 있는지?
# 
# - 두 집단은 정규성을 띄어야 한다, 두 집단의 분산에 따라 다른 검정식을 사용한다

# <img src='./img/독립표본t표.png' width=500 height=300 >

# **예제 데이터**
# - 두 학급(A,B)에 근력운동을 수행하여 집중력 테스트
# - 귀무가설 : 두 학급의 집중력 차이가 없다
# - 대립가설 : 두 학급의 집중력 차이가 있다(양측검정)

# In[23]:


data = pd.read_csv('./data/ch11_training_ind.csv')
data.shape


# In[24]:


data.head()


# In[25]:


data.describe()


# In[26]:


plt.boxplot(data)
plt.show()


# **1. 정규성 검정**

# In[27]:


# 정규성 검정
stats.shapiro(data.A)


# In[28]:


stats.shapiro(data.B)


# => 두 학급의 데이터는 모두 정규성을 만족

# **2. 등분산성 검정**
# - 귀무가설 : 두 집단의 분산이 같다

# In[29]:


stats.levene(data.A, data.B)


# => p값이 0.05 보다 크므로 귀무가설을 기각하지 않음. 즉 두 집단의 분산은 같다(등분산)

# **3. 독립표본 t-검정**

# In[30]:


# equal_var=False로 지정된 경우 웰치 방법 사용

stats.ttest_ind(data.A, data.B, equal_var=True)


# => 귀무가설 채택 : 두 집단의 집중력 차이가 없다

# In[31]:


stats.ttest_ind(data.A, data.B, equal_var=False)


# ### 정규성을 만족하지 않는 경우
# 
# 1. 대응표본 t-test는 윌콕슨 부호순위검정을 적용
#     - stats.wilcoxon(전, 후)
#     - stats.wilcoxon(전-후)
#     
#     
#     
# 2. 독립표본 t-test는 맨휘트니 U검정 적용
#     - stats.mannwhitneyu(A,B, alternative='two-sided')

# In[32]:


# 앞의 20명 학생의 집중력 테스트 대응표본 데이터
stats.wilcoxon(diff)


# In[33]:


# 두 학급의 학생들의 집중력 테스트 데이터(독립표본)
stats.mannwhitneyu(data.A, data.B)

