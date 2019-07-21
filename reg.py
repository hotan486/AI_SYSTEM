# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf
# 테스트할때 일정한 결과를 보기위해
# 램덤시드를 고정
np.random.seed(0)
x_data=[]
y_data=[]
y_line=[]
data_size=100
w=3  ##??
b=2  ##??
for i in range(data_size):
    # 정규분포
    x = np.random.normal(0,1)
    # 유니폼 분포
    #x=np.random.uniform(0,1)
    # 포아송 분포
    #x= np.random.poisson(1000)
    # x 데이터 생성
    x_data.append(x)
    #y 기준선 데이터 생성 yl
    yl= w*x**1 + b
    y_line.append(yl)
    #y 에러 포함 데이터생성
    e=np.random.normal(0,1)    
    y = yl+e
    y_data.append(y)

#plt.hist(x_data)
plt.plot(x_data,y_data,'ro')
#plt.plot(x_data,y_line)
x_min=np.min(x_data)
x_max=np.max(x_data)
print("shape***********")
print("*"*50)
### 텐서 플로우로 회귀분석하기 ###
# 랜덤시드 고정으로 결과값 항상성 유지
tf.set_random_seed(0)
#tf 데이터 입력부 지정(placeholder)
x_h=tf.placeholder(dtype=tf.float32)
#tf 학습 변수 지정
w_ini=tf.random_uniform([1],-10,10)
w_=tf.Variable(w_ini,dtype=tf.float32)
b_=tf.Variable(tf.zeros([1]),dtype=tf.float32)
# 모델 지정 
y=w_*x_h+b_

# 최적화 방향 변수: loss error cost
loss=tf.reduce_mean(tf.square(y-y_data))
# 옵티마이저 정의
lr=0.1
optimizer=tf.train.GradientDescentOptimizer(lr)
# 옵티마이저 최적화 방법
train_step=optimizer.minimize(loss)
#초기화
init=tf.global_variables_initializer()
#세션지정
sess=tf.Session()
### 초기화 실행
sess.run(init)
#session run
for i in range(100):
    res=sess.run(train_step,feed_dict={x_h:x_data})
    #해당결과 빼오기
    #print("y 결과는:",res)
    w_h=sess.run(w_)
    b_h=sess.run(b_)
    print("step:",i,",w_ :",w_h,"b_:",b_h)
    #print("b_ :",b_h)
    y_min=w_h*x_min+b_h
    y_max=w_h*x_max+b_h
    y_test=[y_min,y_max]
    x_test=[x_min,x_max]
    plt.plot(x_test,y_test)
    
#print("loss:",sess.run(loss))
plt.show()
sess.close()






