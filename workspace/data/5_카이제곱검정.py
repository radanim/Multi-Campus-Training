#!/usr/bin/env python
# coding: utf-8

# # 카이제곱 검정

# - 범주형 데이터에 대하여 
# - 카이제곱 분포 근거
# 
# 
# 
# 1. 적합도 검정 : 한 표본데이터가 어떤 분포를 하는지?
# 2. 동질성 검정 : 두 범주형 데이터가 동일한 분포를 하는지?
# 3. 독립성 검정 : 두 범주형 데이터가 서로 관련성 있는지?(독립)

# **독립성 검정**
# - 목적 : 두 범주형 변수가 서로 독립적인지 검정  
# 
#     - 귀무가설 : 두 변수가 서로 독립이다
#     - 대립가설 : 두 변수가 서로 종속된다  
# 
# - 교차테이블로 시각화

# #### 교차 테이블(분할표)  
# 
# - 두 변수가 취할 수 있는 값의 조합의 출현 빈도를 나타냄  
# 
# <img src='./img/분할표.png' width=500 height=300 >

# <img src='./img/분할표위치.png' width=500 height=300 >

# <img src='./img/관측값.png' width=500 height=300 >

# <img src='./img/n11기대값.png' width=500 height=300 >

# <img src='./img/카이기대값1.png' width=500 height=300 >

# <img src='./img/카이수식.png' width=500 height=300 >

# <img src='./img/카이제곱통계량계산.png' width=300 height=200 >

# - 기대값과 실제값의 차이가 클수록 통계량이 커지며 통계량이 커질수록 영가설이 기각될 가능성이 높아짐
# - p-value가 감소함

# <img src='./img/카이제곱함수.png' width=500 height=300 >

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats

get_ipython().run_line_magic('precision', '3')
np.random.seed(1111)


# In[2]:


# 예제 데이터 :
data = pd.read_csv('./data/ch11_ad.csv')
data.shape


# In[4]:


data.head()


# In[5]:


# 교차표 생성
cross = pd.crosstab(data.광고, data.구입)
cross


# In[8]:


# 카이제곱 독립성 검정
stat, p, df, exp_tab =stats.chi2_contingency(cross, correction=False)


# In[9]:


stat


# In[10]:


p


# In[11]:


df


# In[12]:


exp_tab

