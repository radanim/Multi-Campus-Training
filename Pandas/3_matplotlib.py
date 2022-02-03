#!/usr/bin/env python
# coding: utf-8

# # matplotlib

# - 시각화 패키지
# - 파이썬 표준 시각화 도구로 불림
# - 2D 평면 그래프에 관한 다양한 포맷과 기능 지원
# - 데이터 분석 결과를 시각화 하는데 필요한 다양한 기능 제공
# - https://matplotlib.org/

# ### 패키지 사용법
# 
# - matplotlib 주 패키지 사용시 
#     - import matplotlib as mpl
#     
# 
# - pyplot 서브 패키지 사용시 : 주로 사용
#     - import matplotlib.pyplot as plt
# 
# 
# - 매직 명령어
#     - %matplotlib inline 
#     - 주피터 노트북 사용시 노트북 내부에 그림을 표시하도록 지정하는 명령어
#     

# ### 지원 되는 플롯 유형
# 
# - 라인플롯(line plot) : plot()
# - 바 차트(bar chart) : bar()
# - 스캐터플롯(scatter plot) : scatter() 
# - 히스토그램(histogram) : hist()
# - 박스플롯(box plot) : boxplot()
# - 파이 차트(pie chart) : pie()
# - 기타 다양한 유형의 차트/플롯을 지원 : 관련 홈페이지 참고

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# **그래프 패키지 모듈 등록**

# In[2]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
# 그래프는 show()함수를 통해서 독립창에서 실행되는 것이 원칙
# 그래프를 콘솔에서 바로 작동되도록 하는 설정


# In[3]:


# 한글 문제
# matplotlit의 기본 폰트에서 한글 지원되지 않기 때문에
# matplotlib의 폰트 변경 필요

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':  # 맥OS 
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...  sorry~~~')


# ### 그래프 용어 정리
# <img src='./img/matplotlib_용어.png'  width=400  height=500>

# ### 1. plt.plot() : 선그래프(line plot)

# #### plot()
# 
# - 기본으로 선을 그리는 함수
# - 데이터가 시간, 순서 등에 따라 변화를 보여주기 위해 사용

# #### show()
# - 시각화명령(그래프 그리는 함수) 후 실제 차트로 렌더링하고 마우스 이벤트 등의 지시를 기다리는 함수
# - 주피터 노트북에서는 셀 단위로 플롯 명령을 자동으로 렌더링 해주므로 show 명령이 필요 없지만
# - 일반 파이썬 인터프리터(파이참)로 가동되는 경우를 대비해서 항상 마지막에 실행하도록 한다

# ### plot 관련 함수 및 속성    
# - figure(x,y) : 그래프 크기 설정 : 단위 인치
# - title() : 제목 출력
# - xlim : x 축 범위
# - ylim : y 축 범위
# - xticks():yticks() : 축과 값을 잇는 실선    
# - legend() : 범례
# - xlabel() : x축라벨(값)
# - ylabel() : y축라벨(값)
# - grid() : 그래프 배경으로 grid 사용 결정 함수

# #### line plot 에서 자주 사용되는 선 모양관련  속성(약자로도 표기 가능)
#    *  color:c(선색깔)
#    *  linewidth : lw(선 굵기)
#    *  linestyle: ls(선스타일)
#    *  marker:마커 종류
#    *  markersize : ms(마커크기)
#    *  markeredgecolor:mec(마커선색깔)
#    *  markeredgewidth:mew(마커선굵기)
#    *  markerfacecolor:mfc(마커내부색깔)    

# #### plt.plot( ) 형식 
# 
# matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
# 
# : *args : x, y 축값을 리스트 형식으로 입력, y축값만 쓰는 경우 x축값은 자동 생성

# - 기본 plot() 그리기

# In[4]:


# 기본 plot() 그리기
plt.plot([1,4,9,16]) #x축값 [0,1,2,3] 자동으로 생성
plt.show() #그래프 화면 출력 함수


# - 선의 색 지정하기 : plt.plot(*args, color='색상명')

# In[6]:


# 그래프 크기 설정 및 선 색상설정
# 색상은 단어로 지정 : color='green'

# 데이터
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]


plt.figure(figsize=(10,6)) # 단위 인치(가로,세로)
plt.plot(t,y,color='green')
plt.show()


# **선스타일(line style)**

# - linestyle =
# ![](./img/시각화_라인스타일.png)

# - marker = 
# <img src='./img/시각화_마커지정자.png'  width=400  height=500>

# - 선스타일 기호 지정
# ![](./img/시각화_라인스타일지정자.png)

# **선스타일 설정 인수들**
# 
#    *  color:c(선색깔)
#    *  linewidth : lw(선 굵기)
#    *  linestyle: ls(선스타일)
#    *  marker:마커 종류
#    *  markersize : ms(마커크기)
#    *  markeredgecolor:mec(마커선색깔)
#    *  markeredgewidth:mew(마커선굵기)
#    *  markerfacecolor:mfc(마커내부색깔)  

# In[7]:


# 선 스타일 설정
# 색상은 단어로 지정 : color='green'

# 데이터
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]

# 선의 모양 설정
plt.figure(figsize=(10,6))
plt.plot(t,y,color='green',linestyle='dashdot')
plt.show()


# In[9]:


# 색상, 선스타일 설정
# 색상은 단어로 지정 : color='green'

t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]

plt.figure(figsize=(10,6))
plt.plot(t,y,color='green',linestyle='dotted')
plt.show()


# In[10]:


# 색상, 선스타일, 마커 지정

# 데이터
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]

plt.figure(figsize=(10,6))
plt.plot(t,y,color='green',linestyle='dashed',marker='o')
plt.show()


# In[12]:


# 색상, 선스타일, 마커색상, 마커크기 지정

# markerfacecolor: 마커 색상
# markerfacecolor: 마커 크기

# 데이터
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]

# 선그래프 그리기
plt.figure(figsize=(10,6))
plt.plot(t,y,color='green',linestyle='dashed',marker='o',
        markerfacecolor='blue',markersize=12)
plt.show()


# In[13]:


# 선의 스타일들을 약자로 표시 

plt.figure(figsize=(10,6))

plt.plot([10,20,30,40],[1,4,9,16],
         c="b",lw=5,ls='--', 
         marker='o', ms=15, mec='g', mew=5,
         mfc='r') 
plt.title("스타일적용 예")
plt.show()


# In[14]:


# 선의 스타일들을 약자로 표시

plt.figure(figsize=(10,6))

plt.plot([10,20,30,40],[1,4,9,16],
         c="b", lw=5, ls='--',
         marker='o', ms=15, mec='g', mew=5,
         mfc='r')

plt.xlim(0,50) # x축 범위
plt.ylim(-10,30) # y축 범위

plt.title("스타일적용 예")
plt.show()


# #### 여러 개의 선그래프를 한 플롯내에 그리기
# - 여러 데이터를 하나의 그래프에 여러 선 으로 표현
# - plot()을 선그래프 수만큼 지정하거나, 하나의 plot() 함수 내에 지정하여 호출

# In[15]:


# 여러 개의 선 그리기 : plot() 여러 번 사용

# 데이터 생성
t=np.arange(0.,5.,0.2)
t

# 여러 개 선그래프 그리기
plt.figure(figsize=(10,6))
plt.title('라인 플롯에서 여러개의 선 그리기')

plt.plot(t,t,'r--') # r(red),--(dashed lin style)
plt.plot(t,0.5*t**2,'bs:')# b(blue),s(square marker,),:(dot line style)
plt.plot(t,0.2*t**3,'g^-')# g(green),^(triangle_up marker),-(solid lin style)

plt.show()


# - 위 그래프 코드를 plot() 하나로 한번에 표현하기

# In[16]:


plt.plot(t,t,'r--',t,0.5*t**2,'bs:',t,0.2*t**3,'g^-')


# In[17]:


# 여러 개의 선 그리기 : plot() 한 번 사용

# 데이터 생성
t=np.arange(0.,5.,0.2)
t

plt.figure(figsize=(10,6))
plt.title('라인 플롯에서 여러개의 선 그리기:plot 한번 사용')

# 선 그래프 그리기
plt.plot(t,t,'r--',t,0.5*t**2,'bs:',t,0.2*t**3,'g^-')
plt.show()


# #### 축의 눈금 설정 : plt.xticks(), plt.yticks()
# - tick은 축상의 위치 표시 지점
# - 축에 간격을 구분하기 위해 표시하는 눈금
# 
# 
# - xticks([x축값1,x축값2,...]) #튜플,리스트등 이용해서 축 값(위치 나열)
# - yticks([y축값1,y축값2,...]) #튜플,리스트등 이용해서 축 값(위치 나열)
# - tick_params()
# - tick label(눈금 레이블) : tick에 써진 숫자 혹은 글자

# In[19]:


x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x)
plt.yticks(y)
plt.show()


# #### 축의 눈금 레이블 지정

# In[20]:


# 눈금 레이블 지정

# 데이터 생성
x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]

# 그래프 그리기
plt.plot(x,y, color='green',linestyle='dashed',marker='o')

# x,y 축 눈금 레이블 지정
plt.xticks(x,['10대','20대','30대','40대','50대','60대'])
plt.yticks(y,[y[i] for i in range(6)]) 

plt.show()


# In[6]:


# 데이터생성
x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]

# 그래프 그리기
plt.plot(x,y, color='green',linestyle='dashed',marker='o')

# 축의 눈금 표시
plt.xticks(x,['10대','20대','30대','40대','50대','60대'])
plt.yticks([0,10,20,30,40,50])
plt.show()


# #### 그래프 제목 및 축 레이블 설정
# - 그래프 제목 설정: plot.title(data,loc=, pad=, fontsize=)
#      - loc= 'right'|'left'| 'center'| 'right'로 설정할 수 있으며 디폴트는 'center'
#      - pad=point 은 타이틀과 그래프와의 간격 (오프셋)을 포인트(숫자) 단위로 설정
#      - fontsize=제목폰트크기
#         
# - 축 레이블 설정
#     - plot.xlabel()
#     - plot.ylabel()

# In[29]:


# 그래프 제목, x축, y축 라벨 표시

x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]

# plt.title('그래프제목')
# plt.title('그래프제목', loc='right')
# plt.title('그래프제목', loc='right', pad=30)
plt.title('그래프제목', loc='right', pad=30, fontsize=20)

plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x,('10대','20대','30대','40대','50대','60대'))
plt.yticks(y,(y[i] for i in range(6)))
plt.xlabel('x축제목')
plt.ylabel('y축제목')
plt.show()


# #### 그래프 Title 폰트 관련 지정
# 
# - 딕셔너리형식으로 fontsize 및 fontwegith 등 지정 가능

# In[30]:


plt.title('그래프제목', loc='right', pad=20)

title_font = {
    'fontsize': 16,
    'fontweight': 'bold'
}

plt.title('그래프제목', fontdict=title_font, loc='left', pad=20)

plt.show()


# #### plot.grid(True) : 그리드 표시

# In[33]:


# 배경 그리드 표현

# 데이터 생성
x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]

# 그래프 그리기
plt.title('그래프제목')
plt.plot(x,y, color='green',linestyle='dashed',marker='o')
plt.xticks(x,('10대','20대','30대','40대','50대','60대'))
plt.yticks([0,10,20,30,40,50])
plt.xlabel('x축제목')
plt.ylabel('y축제목')

# 그리드 표시
plt.grid(True)
plt.show()


# #### plt.subplot() : 여러 플롯 표시
# 
# : 하나의 윈도우(figure)안에 여러 개의 플롯을 배열 형태로 표시
# 
# - 그리드 형태의 Axes 객체들 생성
# 
# - 형식 : subplot(인수1,인수2,인수3)
#     - 인수1 과 인수2는 전체 그리드 행렬 모양 지시
#     - 인수3 : 그래프 위치 번호
# 
# 
#     - subplot(2,2,1) 가 원칙이나 줄여서 221로 쓸 수 있음
#     - subplot(221) 2행 2열의 그리드에서 첫번째 위치
#     - subplot(224) 2행 2열의 그리드에서 마지막 위치
#     
#     
# - tight_layout(pad=) : 플롯간 간격을 설정
#     - pad = 간격값(실수)

# In[39]:


# 2 x 2 형태의 네 개의 플롯

np.random.seed(0) # 항상 같은 난수가 발생

plt.subplot(221) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes1')

plt.subplot(222) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes2')

plt.subplot(223) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes3')

plt.subplot(224) #그래프 show()-객체생성 하기 전에 먼저 위치를 설정
plt.plot(np.random.rand(5))
plt.title('axes4')

plt.tight_layout(1.5) #플롯간의 간격 설정
# plt.tight_layout(3.0) #플롯간의 간격 설정
plt.show()


# - plt.subplots(행,열)
#     - 여러 개의 Axes 객체를 동시에 생성해주는 함수
#     - 행렬 형태의 객체로 반환
#     - 두 개의 반환값이 있음
#         - 첫번 째 반환은 그래프 객체 전체 이름 : 거의 사용하지 않음
#         - 두번 째 반환값에 Axes 객체를 반환함
#         - 두번 째 반환값이 필요하므로 반환 값 모두를 반환받아 두번 째 값을 사용해야 함
#         
#         - ex. fig, axes = plt.subplots(2,2)

# In[40]:


# subplots() : 여러개의 Axes 객체 동시 생성해주는 함수

fig, axes = plt.subplots(2,2)

np.random.seed(0)

axes[0,0].plot(np.random.rand(5))
axes[0,0].set_title('axes 1')

axes[0,1].plot(np.random.rand(5))
axes[0,1].set_title('axes 2')

axes[1,0].plot(np.random.rand(5))
axes[1,0].set_title('axes 3')

axes[1,1].plot(np.random.rand(5))
axes[1,1].set_title('axes 4')

plt.tight_layout()
plt.show()


# #### plot 함수 응용 예제
# - numpy 모듈의 sin()함수를 이용하여 sin 곡선 그래프 그리기

# In[41]:


# data 생성
t=np.arange(0,12, 0.1) 
t


# In[42]:


# sin 값 생성
y = np.sin(t)


# In[43]:


# sin 곡선 그리기
plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.show()


# **문제.** 위 그래프에 x, y 축 제목, 그래프 제목, 격자무늬를 표시하시오.
# - x축 : time
# - y축 : Amplitude
# - 그래프 제목 : Example of sinewave

# In[44]:


plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.grid() #격자무늬
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()


# **문제.** 위쪽 그래프에 cos 곡선을 추가하는 코드를 작성하시오.
# - np.sin() : sin 값을 계산후 반환
# - np.cos() : cos 값을 계산 후 반환
# - cos 곡선의 색상은 빨간색으로 설정 할 것

# In[45]:


plt.figure(figsize=(10,6)) # figsize=(가로인치,세로인치)

# sin 곡선 추가
plt.plot(t,np.sin(t))

# cos 곡선 추가
plt.plot(t,np.cos(t),c='red')

# 격자무늬
plt.grid()

plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sine/cosine wave')
plt.show()


# #### 범례(legend)표시
# - plot에 label 속성이 추가되어 있어야 함
#     - plt.plot(x,y,label='a')
# - plt.legend(loc=, ncol= ) #범례표시, 
# - loc = 1/2/3/4/5/6/7/8/9/10 # 범례표시 위치값
# - loc = (x,y)
# - ncol= 열갯수

# <img src='./img/그래프범례.png' width=600  >

# In[48]:


# 범례 표시 예
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc=(0.0, 0.0))
# plt.legend(loc=(0.5, 0.5))
# plt.legend(loc=(1.0, 1.0))
# plt.legend(loc=10)
plt.legend(loc='center left')

plt.show()


# **두 개의 선그래프에 대한 범례 표시**

# In[87]:


plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='best') #열 1개
# plt.legend(loc='best', ncol=2) # 열 2개

plt.show()


# ### 2. 막대그래프 : bar(), barh(), df.plot()

# ### 2-1. 세로 막대 그래프 그리기: bar()
# - bar(x,y,color=[],alpha=)
#     - color = [] : 색상값 설정
#     - alpha = 투명도 설정

# In[ ]:


# 데이터 생성
y=[2,3,1,4]
x=np.arange(len(y))

z=[2,3]
s=[0,1]

e=[1,4]
h=[2,3]

xlabel=['가','나','다','라']


# In[90]:


# 막대그래프 그리기
plt.figure(figsize=(10,6))
plt.title('Bar Chart')
plt.bar(x,y)
plt.xticks(x,xlabel)
plt.yticks(sorted(y))
plt.text(-0.1, 1, r'test')

plt.plot(s, z, color='green',linestyle='dashed',marker='o')
plt.plot(h, e, color='green',linestyle='dashed',marker='o')

plt.xlabel('가나다라')
plt.ylabel('빈도수')

plt.show()

# r'문자열' : 문자열 렌더링할때 rowformat으로 렌더링 하는 명령
# rowformat : 장치에서 가장 표준 형태로 변환


# In[91]:


np.random.seed(0)
people=['몽룡','춘향','방자','향단']
y=np.arange(len(people))
#np.arange(4) : 0-4사이의 정수를 순서적으로 추출
#0,1,2,3
#np.random.rand(4) : 0-1사이의 난수를 4개 추출
#array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
# a=np.random.rand(len(people))
# a=np.random.rand(4)
# a

performance = 3+ 10 * np.random.rand(len(people))


# ### 2-2. 가로 막대 그래프 그리기 : barh()
# - barh(x,y,color=[], alpha=)

# In[92]:


# 데이터 생성
np.random.seed(0)
people=['몽룡','춘향','방자','향단']
y=np.arange(len(people))
performance = 3+ 10 * np.random.rand(len(people))

# 가로 막대그래프 그리기
plt.title("Barh Chart")
plt.barh(y, performance, alpha=0.4)
plt.yticks(y,people)
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.grid(True)
plt.show()


# ### 2-3. 데이터프레임으로 막대그래프 그리기
# - **데이터프레임.plot**(kind=그래프종류, grid=T/F, figsize=그래프크기)
# - **plt.bar**(데이터프레임.변수1, 데이터프레임.변수2)

# **데이터프레임.plot()으로 막대그래프 그리기**
# 
# - plt.xticks()의 rotation 인수에 따라 가로형 또는 세로형 막대그래프 생성
#     - plt.xticks(ticks=None, labels=None, **kwargs)
#     - plt.xticks(ticks=None, labels=None) : vertical 기본
#     - plt.xticks(ticks=None, labels=None, rotation='vertical') : 가로형막대
#     - plt.xticks(ticks=None, labels=None, rotation='horizontal') : 세로형막대

# In[ ]:


# 데이터프레임.plot()으로 막대그래프 그리기

# 데이터 생성 : df1
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','이름'])
df1


# In[64]:


# xticks 시 위치 표시에 사용할 변수 지정
x=[0,1,2,3,4,5,6,7] 

# 막대그래프 그리기
df1.plot(kind='bar', grid=True, figsize=(10,10))
plt.xticks(x, df1.이름, rotation='horizontal')
plt.show()


# **데이터프레임.plot()를 이용하여 묶음 막대그래프 그리기**
# - 그래프를 그리기 위한 데이터를 지정하지 않는 경우
# - 데이터프레임에 있는 모든 수치데이터를 이용하여 묶음 막대그래프를 그림

# In[66]:


# 묶음 막대그래프 그리기 : 데이터프레임.plot()이용

# 데이터 생성 :df1
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름'])

# xticks 시 위치 표시에 사용할 변수
x=[0,1,2,3,4,5,6,7] 

# df.plot()으로 막대그래프 그리기
df1.plot(kind='bar',grid=True,figsize=(10,10))
plt.xticks(x,df1.이름,rotation='horizontal')
plt.show()


# **plt.bar(데이터프레임)를 이용하여 막대그래프 그리기**

# In[68]:


# 데이터프레임으로 막대그래프 그리기2 : plt.bar(데이터프레임)
# 데이터 생성 :df1
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름'])

# plt.bar()로 막대그래프 그리기
plt.bar(df1.이름,df1.나이)
plt.show()


# **데이터프레임의 일부 필드를 데이터프레임으로 추출하여 그래프 작성**

# In[69]:


# 데이터 생성 : df1
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름'])

# xticks 시 위치 표시에 사용할 변수
x=[0,1,2,3,4,5,6] 

# 막대그래프 그리기
df1[['키']].plot(kind='bar',grid=True,figsize=(10,10))
plt.xticks(x,df1.이름,rotation='horizontal')
plt.show()


# **정렬된 데이터를 이용하여 막대그래프 그리기**

# In[72]:


# 정렬된 데이터를 이용하여 막대그래프 그리기

# 데이터 생성 : df1 
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','이름'])
 
# xticks 시 위치 표시에 사용할 변수
a=[0,1,2,3,4,5,6] 

# 나이로 df1 정렬하여 새로운 df2 생성
df2=df1.sort_values(by='나이')
df2

# 가로 막대그래프 그리기
df1.sort_values(by='나이').plot(kind='barh',grid=True,figsize=(5,5))

plt.yticks(a, df1.sort_values(by='나이').이름, rotation='horizontal')
plt.show()


# ### 3. 산점도(scatter plot) : scatter()

# - 두 수치형 변수간의 관계를 나타내기 위해 사용하는 그래프
#     - 상관관계 표현 : 선형성

# In[73]:


# 데이터 생성
t = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])


# In[74]:


# 산점도 그리기
plt.figure(figsize=(10,6))
plt.scatter(t,y)
plt.show()


# - 산점도의 marker 변경

# In[75]:


# 산점도에 marker 변경
plt.figure(figsize=(10,6))
plt.scatter(t,y,marker='>') #마커지정
plt.show()


# #### 버블차트
# - 점의 크기와 색상을 이용하여 서로 다른 데이터 값을 표시하는 그래프
# - scatter(c, s)를 이용하여 작성
#     - s 인수 : size
#     - c 인수 : color

# In[78]:


# 데이터 생성
N=30
np.random.seed(0)
x=np.random.rand(N)
y1 =np.random.rand(N)
y2 =np.random.rand(N)
y3=np.pi *(15 * np.random.rand(N))**2

# 버블차트 그리기
plt.title("Bubble Chart")
plt.scatter(x,y1,c=y2,s=y3)
plt.show()


# #### 산점도에 colorbar() 적용
# - 산점도를 그린 후 colorbar()를 생성하여 색상 정보를 막대로 표현

# In[81]:


# colorbar()을 이용해서 산점도 그리기
colormap = t

plt.figure(figsize=(10,6))
plt.scatter(t,y, s=50, c=colormap, marker='>')
plt.colorbar() # 색상 데이터를 bar 형태로 출력
plt.show()


# ### 4. 히스토그램 : hist()

# - 연속형 수치형 데이터의 분포 시각화
# - 참고. 막대그래프는 범주형 데이터의 빈도(비율) 분포 시각화

# In[84]:


# 데이터 생성
np.random.seed(0)
x = np.random.randn(1000) #난수 1000개 발생

# 히스토그램 그리기
plt.figure(figsize=(10,6))
plt.title('Histogram')
plt.hist(x)
plt.show()


# ### 5. 박스플롯 : boxplot()

# - 데이터의 분포를 파악해주는 플롯
#     - 최소값, 제1사분위수, 중위수, 제3사분위수, 최대값
#     
# - 이상치 데이터 탐색을 위해 사용

# In[5]:


# 다차원 array 형태로 무작위 샘플을 생성
# np.random.normal(정규분포평균,표준편차,(행열) or 개수)
# 정규분포 확률 밀도에서 표본 추출해주는 함수

# 데이터 3개 생성
s1=np.random.normal(loc=0,scale=1,size=1000)
s2=np.random.normal(loc=5,scale=0.5,size=1000)
s3=np.random.normal(loc=10,scale=2,size=1000)


# In[86]:


# line 그래프 이용해서 데이터 차이 확인
plt.figure(figsize=(10,6))
plt.plot(s1,label='s1')
plt.plot(s2,label='s2')
plt.plot(s3,label='s3')
plt.legend()
plt.show()


# In[87]:


# boxplot 그리기
plt.figure(figsize=(10,6))
plt.boxplot((s1,s2,s3))
plt.grid()
plt.show()


# ### 6. 파이차트 : pie()

# - 범주형 데이터의 빈도(비율)을 비교하기 위해 사용하는 차트
# - 원의 형태를 유지할 수 있도록 다음 명령을 실행해야 함
#     - plt.axis('equal')
#     - 콘솔에서는 별 다른 변화 없으나 plot창에서는 필요함

# In[95]:


# 데이터 생성
labels=['개구리','돼지','개','통나무']
size=[15, 30, 45, 10]
colors=['yellowgreen','gold','lightskyblue','lightcoral']
explode=(0,0.4,0,0.5)

# plot 그리기
plt.figure(figsize=(10,6))
plt.title('Pie Chart')
plt.pie(size, explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal') # 원의 형태 유지 설정
plt.show()

