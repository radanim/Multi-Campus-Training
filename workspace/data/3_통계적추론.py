#!/usr/bin/env python
# coding: utf-8

# # 통계적 추론(statistical inference)

# - 모집단에서 추출한 표본을 이용하여 모집단의 특성(모수)을 예측하는 과정
# - 추정, 가설검정

# ![image.png](attachment:image.png)

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

get_ipython().run_line_magic('precision', '3')
np.random.seed(1111)


# **참고. 정규분포 관련 함수들**
# 
# - stat.norm(평균, 표준편차) : 평균과 표준편차의 정규분포를 따르는 확률변수 생성
# - .pdf(확률변수) : 밀도함수 계산
# - .cdf(확률변수) : 누적분포함수 P(X<=확률변수)
# - .isf(alpha) : 상위 alpha%가 되는 확률변수값 반환
# - .interval(alpha) : 확률이 alpha가 되는 가운데 부분의 구간 반환
# 

# In[3]:


# 성적 데이터

df = pd.read_csv('./data/ch4_scores400.csv')
scores = np.array(df['score'])


# ## 추정(estimation)

# ### 모평균의 구간추정

# **문제1**
# 
# 표준정규분포로부터 뽑아 95% 신뢰구간을 구하는 것을 20번 반복했을 때, 몇 개의 신뢰구간이 모평균을 포함할지 확인

# In[2]:


# 성적 데이터

df = pd.read_csv('./data/ch4_scores400.csv')
scores = np.array(df['score'])


# In[3]:


# 성적데이터 모집단의 평균과 분산 계산

p_mean = np.mean(scores)
p_var = np.var(scores)

p_mean, p_var


# In[4]:


# 모집단의 분포
xs = np.arange(101)
rv = stats.norm(p_mean, np.sqrt(p_var))
plt.plot(xs, rv.pdf(xs), color='gray') # 평균 69.53, 분산 206.67 정규분포
plt.hist(scores, bins=100, range=(0,100), density=True)
plt.show()


# In[5]:


# sample 데이터 생성
n_sam = 10000
n = 20
samples = np.random.choice(scores, (n_sam, n))
samples[:5]


# In[6]:


rv = stats.norm()
rv.isf(0.025)


# In[7]:


rv.isf(0.975)


# In[12]:


# 모분산을 아는 경우 95% 신뢰구간 : 정규분포를 이용

rv = stats.norm()
n_samples = 20
n = 20
plt.vlines(p_mean, 0, 21)
for i in range(n_samples):
    sample_ = samples[i]
    s_mean = np.mean(sample_)
    lcl = s_mean - rv.isf(0.025) * np.sqrt(p_var/n)
    ucl = s_mean + rv.isf(0.025) * np.sqrt(p_var/n)
#     ucl = s_mean - rv.isf(0.975) * np.sqrt(n_var/20)
    if lcl <= p_mean <= ucl:
        plt.scatter(s_mean, n_samples-i, color='gray')
        plt.hlines(n_samples-i, lcl, ucl, color='gray')
    else:
        plt.scatter(s_mean, n_samples-i, color='b')
        plt.hlines(n_samples-i, lcl, ucl, color='b')
    
plt.xticks([p_mean])
plt.xlabel('populaion mean')
plt.show()


# In[13]:


# 모분산을 모르는 경우 95% 신뢰구간 : t-분포를 이용

n = 20
alpha = 0.25
sample_ = samples[0]
s_mean = np.mean(sample_)
s_var = np.var(sample_)
rv = stats.t(df=n-1)
lcl = s_mean - rv.isf(alpha)  * np.sqrt(s_var/n)
ucl = s_mean + rv.isf(alpha)  * np.sqrt(s_var/n)
lcl, ucl


# In[14]:


n_samples = 20
n = 20
rv = stats.t(df=n-1)
alpha = 0.25

plt.vlines(p_mean, 0, 21)
for i in range(n_samples):
    sample_ = samples[i]
    s_mean = np.mean(sample_)
    s_var = np.var(sample_)
    lcl = s_mean - rv.isf(alpha) * np.sqrt(s_var/n)
    ucl = s_mean + rv.isf(alpha) * np.sqrt(s_var/n)
#     ucl = s_mean - rv.isf(0.975) * np.sqrt(n_var/20)
    if lcl <= p_mean <= ucl:
        plt.scatter(s_mean, n_samples-i, color='gray')
        plt.hlines(n_samples-i, lcl, ucl, color='gray')
    else:
        plt.scatter(s_mean, n_samples-i, color='b')
        plt.hlines(n_samples-i, lcl, ucl, color='b')
    
plt.xticks([p_mean])
plt.xlabel('populaion mean')
plt.show()


# **문제2.**
# 만 7세 어린이 중 부모의 동의를 얻은 학생 중 10명을 표본으로 추출.
# 머리 둘레를 측정한 결과를 기준으로 모평균에 대한 95% 신뢰구간을 추정하시오.

# In[17]:


# 표본 데이터
data = [520, 498, 481, 512, 515, 542, 520, 518, 527, 526]
s_mean = np.mean(data)
s_var = np.var(data)
print(s_mean, np.sqrt(s_var))

n=len(data)
print(n)

# t-분포를 이용

rv = stats.t(df=n-1)
alpha = 0.025
lcl = s_mean - rv.isf(alpha)  * np.sqrt(s_var/n)
ucl = s_mean + rv.isf(alpha)  * np.sqrt(s_var/n)
lcl, ucl


# In[18]:


# 정규분포를 이용한 경우

rv = stats.norm()
alpha = 0.025
lcl = s_mean - rv.isf(alpha)  * np.sqrt(s_var/n)
ucl = s_mean + rv.isf(alpha)  * np.sqrt(s_var/n)
lcl, ucl


# ## 통계적 가설검정(test)

# ![image.png](attachment:image.png)

# In[19]:


# 감자 무게 측정데이터

df = pd.read_csv('./data/ch11_potato.csv')
sample = np.array(df['무게'])
sample


# In[20]:


# 표본 평균 확인
s_mean = np.mean(sample)
s_mean


# In[21]:


# 표본 분산 확인
s_var = np.var(sample)
s_var


# ### 통계적 가설 검정이란?
# 
# - 모집단의 모수에 관하여 두 가지 가설을 세우고, 표본으로부터 계산되는 통계량을 이용하여 어느 가설이 옳은지 판단하는 통계적 방법
# - A학생이 확인하고 싶은 것은 모평균이 130g보다 적은지 여부
# 
# 
# 

# ### 통계적 가설검정의 흐름
# 
# - A학생이 감자튀김에 관하여 확인하고 싶은 것은 모평균이 130g보다 적은지 여부 임
#     - 여기서는 감자튀김의 모집단이 정규분포를 따르고 있고, 모분산이 9임을 알고 있다고 전제
# 
# - 가정은 ‘모평균이 130g’
# - 감자튀김 표본 14개는 독립성을 띄고 X1,X2,X3,...,X14 ~ N(130,9) 를 따르고 표본평균은 N(130,9/14)를 따른다
# 
# 
# - 표본평균 $\overline{x}$ 가 P($\overline{X}$ <= x) = 0.05를 만족하는 x를 생각
# 

# In[22]:


# 모분산 = 9 
rv = stats.norm(130, np.sqrt(9/14))
rv.isf(0.95)


# ![image.png](attachment:image.png)
# - 가 되고, 표본평균이 128.681g 이하의 무게가 되는 것은 5%의 확률로 발생
# 
# ![](그림11-1.jpg)

# ###  가설
# 
# - 대립가설: 주장하고 싶은 가설 
#     - 예: “차이가 있다”, “효과가 있다”
# 
# - 귀무가설: 대립가설과 반대 
#     - 예: “차이가 없다”, “효과가 없다”
# 
# - 가설검정의 결론
#     - 귀무가설을 기각한다: 귀무가설은 옳지 않다
#     - 귀무가설을 채택한다: 귀무가설이 옳지 않다고 말할 수 없다
# 
# 

# ![image.png](attachment:image.png)

# - ‘귀무가설을 기각한다/채택한다’의 판단은 귀무가설의 가정을 바탕으로 했을 때 표본으로부터 계산되는 통계량이 드문 값인지 여부로 결정
# - 드문 값을 얻으면, 우연이 아니라 의미 있는 값이라고 생각하여 귀무가설을 기각
#     - 유의하다: 우연이 아니라 의미가 있다
#         
#         
# 
# - 귀무가설 ‘모평균은 130g이다’라는 가정을 바탕으로 했을 때 표본평균이 128.451g이 되는 것은 유의하므로 귀무가설은 기각
#     - 표본평균이 128.681g보다 작다면 귀무가설은 기각되고, 128.681g보다 크다면 귀무가설을 채택
# 

# - 기각역: 귀무가설이 기각되는 구간
# - 채택역: 귀무가설이 채택되는 구간
# 
# ![](기각역채택역.png)
# 

# - p값과 유의수준을 비교
# - p값이 유의수준보다 작으면 귀무가설 기각
# 
# ![image-2.png](attachment:image-2.png)
# 
# ![](그림11-2.jpg)
# 
# ### p 값은 누적분포 함수로 구할 수 있음

# ##### 검정통계량 z는 아래와 같이 설정하자
# - 유의수준은 0.05(5%)로 설정

# In[23]:


# 검정 통계량 Z
Z=(s_mean-130)/np.sqrt(9/14)
Z


# In[29]:


# p-value
rv.cdf(Z)


# - p값을 기준으로 하는 가설 검정
# 
# <img src='./img/그림11-3.jpg' width = 500 height=300 >

# In[24]:


rv=stats.norm()
rv.isf(0.95)


# ### 단측검정과 양측검정
# 
# - 모평균은 130보다 작다=>단측검정 라는 대립가설이 아닌 모평균은 130g이 아니다라는 대립가설로 가설 검정 수행    
# 
# 
#     - 모평균이 130g보다 작은 경우와 큰 경우도 고려하게 됨 => 양측 검정
#     
# - 동일한 유의수준 $\alpha$ 의 검정이라도 단측 검정 쪽의 기각역이 넓어진다. 
#     - 단측검정은 양측검정보다 귀무가설을 기각하기 쉽다

# #### 단측 검정과 양측 검정에서는 기각역이 다르다
# 
# ![](단측검정양측검정.png)

# In[25]:


# 검정 통계량
Z=(s_mean-130)/np.sqrt(9/14)
Z


# In[13]:


# 양측검정, 임계값 :표준 정규분포의 95% 구간에 따라 구할 수 있음
rv=stats.norm()
rv.interval(0.95)


# - 임곗값과 검정 통계량을 비교해 보면 검정통계량이 채택역에 들어 있다. => 귀무가설이 기각되지 않는다

# In[28]:


# 양측검정의 p값
rv.cdf(Z)*2


# - p값의 유의 수준이 0.05보다 큼 => 귀무가설은 기각되지 않는다

# ### 가설검정에서의 두 가지 오류

# ![](제12종오류.png)
# 
# - 제1종 오류
#     - 실제로 ‘평균이 130g’인데도 ‘평균은 130g보다 작다’라는 결론을 내리는 상황
#     - 본래 검출하지 말아야 할 것을 검출한 것이므로 오탐(false negative)
#     - 위험률: 제1종 오류를 범하는 확률 $\alpha$
# 
# - 제2종 오류
#     - 실제로 ‘평균이 130g보다 작다’인데도 ‘평균은 130g보다 작다’라는 결론을 얻을 수 없는 상황
#     - 본래 검출해야 하는 것을 검출하지 못했으므로 미탐(false negative)
# 

# In[16]:


# 모집단에서 14개의 표본을 추출하여 가설검정을 수행하는 작업을 1만번 함. 
# 제 1종 오류를 범하는 비율, 즉 평균이 130g인데도 평균은 130g보다 작다 라는 결론을 내려버리는 비율을 계산

c = stats.norm().isf(0.95)
n_samples = 10000
cnt = 0
for _ in range(n_samples):
    sample_ = np.round(rv.rvs(14), 2)
    s_mean_ = np.mean(sample_)
    z = (s_mean_ - 130) / np.sqrt(9/14)
    if z < c:
        cnt += 1
cnt / n_samples


# ### 정규분포의 모평균에 대한 검정(모분산을 알고 있음)
# 
# - 모 평균이 어떤 값 $\mu0$이 아니라고 주장하기 위한 검정
#     - 모집단에 정규분포를 가정하고 그 모분산 $\sigma$도 알고 있는 상황은 매우 단순한 설정임
#     - 감자튀김의 모 평균이 130g이 아니라고 주장했을때와 동일한 상황
# 
# ![](정규분포모분산알때.png)

# In[30]:


# 모분산을 아는 경우 모평균에 대한 양측검정을 위한 함수
# 정규분포를 기반

def pmean_test(sample, mean0, p_var, alpha=0.05):
    s_mean = np.mean(sample)
    n = len(sample)
    rv = stats.norm()
    interval = rv.interval(1-alpha)

    z = (s_mean - mean0) / np.sqrt(p_var/n)
    if interval[0] <= z <= interval[1]:
        print('귀무가설을 채택')
    else:
        print('귀무가설을 기각')

    if z < 0:
        p = rv.cdf(z) * 2
    else:
        p = (1 - rv.cdf(z)) * 2
    print(f'p값은 {p:.3f}')


# In[31]:


# 감자 튀김의 표본 데이터로 확인 
# : 양측검정으로 계산한 것과 동일한 결과 얻음
pmean_test(sample, 130, 9)


# ### 정규분포의 모분산에 대한 검정
# 
# 모분산이 어떤 값 $\sigma^2_0$이 아닌것을 주장하기 위한 검정
# 
# ![](정규분포모분산검정.png)

# In[24]:


def pvar_test(sample, var0, alpha=0.05):
    u_var = np.var(sample, ddof=1)
    n = len(sample)
    rv = stats.chi2(df=n-1)
    interval = rv.interval(1-alpha)
    
    y = (n-1) * u_var / var0
    if interval[0] <= y <= interval[1]:
        print('귀무가설을 채택')
    else:
        print('귀무가설을 기각')

    if y < rv.isf(0.5):
        p = rv.cdf(y) * 2
    else:
        p = (1 - rv.cdf(y)) * 2
    print(f'p값은 {p:.3f}')


# In[25]:


pvar_test(sample, 9)


# ### 정규분포의 모평균에 대한 검정(모분산을 알지 못함)
# 
# - 모 분산을 알지 못하는 상황에서 정규분포이 모평균에 대한 검정을 1표본 t검정이라 함
# - t 검정 통계량 사용 : 자유도가 n-1인 t분포를 따름
# ![](정규분포모분산모를때.png)

# In[32]:


# 양측검정, t-분포를 이용

def pmean_test(sample, mean0, alpha=0.05):
    s_mean = np.mean(sample)
    u_var = np.var(sample, ddof=1)
    n = len(sample)
    rv = stats.t(df=n-1)
    interval = rv.interval(1-alpha)  # 임계값 계산

    t = (s_mean - mean0) / np.sqrt(u_var/n)
    if interval[0] <= t <= interval[1]:
        print('귀무가설을 채택')
    else:
        print('귀무가설을 기각')

    if t < 0:
        p = rv.cdf(t) * 2
    else:
        p = (1 - rv.cdf(t)) * 2
    print(f'p값은 {p:.3f}')


# In[33]:


pmean_test(sample, 130)


# - scipy.stats 에 구현되어 있음

# In[28]:


t, p = stats.ttest_1samp(sample, 130)
t, p # 통계량, p-value

