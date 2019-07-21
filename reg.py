# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:37:14 2019

@author: kosmo_27
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf

print("==========================")
print("--------------------------")
print("텐서플로우 시작")
np.random.seed(0) ## 랜덤 값 시드 고정
x_data = []
y_data = []
y_line = []

w = 3 
b = 2
data_size = 100


for i in range(data_size):
    x = np.random.normal(0,1) ## 랜덤 생성 기본 (정규분포)
    #y = np.random.normal(0,1)
    #x = np.random.uniform(0,1) ## 차이가 없을때 생성(유니폼 분포)
    #x = np.random.poisson(10) ## 생픔링 할때 이용(포아송분포)
    e = np.random.normal(0,1) ## 선행 그래프에 에러 생성 
   
    ## 기준선 생성
    yl = w*x**2 +b
    y_line.append(yl)
    y = yl + e ## 
    ## x 데이터 생성    
    x_data.append(x) ## 데이터 저장
    y_data.append(y) ## 데이터 저장

print("--------------------------")
#plt.hist(x_data) ## 막대 그래프 생성
print("--------------------------")
plt.plot(x_data,y_data,'ro') ## 선형 그래프 생성, ro = 레드 점선 점선 만들기 
plt.plot(x_data,y_line)
plt.show() ## 그래프 보여줌
#print(x_data)

print("==========================")

