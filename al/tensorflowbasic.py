# -*- coding: utf-8 -*-
# 라이브러리 가져오기
import tensorflow as tf
##### 상수 constant 정의 ############
# 노드를 설정(텐서 정의)
hello=tf.constant("Hello tensor!")
#print(hello)
# Tensor("Const:0", shape=(), dtype=string)
# 실행부 (세션정의및 처리)
sess=tf.Session()
#print(sess)
#print(sess.run(hello))
# 세션 처리 b'Hello tensor!'
# 세션 닫기
sess.close()
######### 텐서 연산 #########
# constant 변하지 않는 변수(상수)
node1=tf.constant(3)
node2=tf.constant(4.0)
node3=tf.constant(5,dtype=tf.float32)
print("3:",node1)
#묵시적 정수 인식 int32
#Tensor("Const_8:0", shape=(), dtype=int32)
print("4.0:",node2)
#묵시적 실수 인식 float32
#Tensor("Const_9:0", shape=(), dtype=float32)
print("5 dtype:",node3)
#명시적 데이터 타입 지정
#Tensor("Const_10:0", shape=(), dtype=float32)
# 데이터 타입이 안맞으면 에러 tf.add(node1,node2)
node4=tf.add(node3,node2)
node5=node4*node3
print("node5:",node5)
#node5: Tensor("mul:0", shape=(), dtype=float32)
sess=tf.Session()
print("result:",sess.run(node5))
sess.close()
######### 변수 [데이터, 가중치변수]
#ML 용 데이터 변수의 입력부 placeholder
print('*'*50)
x=tf.placeholder(dtype=tf.float32)
print("placeholder:",x)
# 모델 설정 fetch 모델
y=tf.multiply(x,2.0)
########### 세션 실행부 #########
sess=tf.Session()
input_data=[1,3,5,7,9.0]
# placeholder 가 들어가면 feed_dict 변수를
# 딕셔너리 형태로 변수 투입
result=sess.run(y,feed_dict={x:input_data})
print(result)
sess.close()


print('*'*10,"변수 Variable ",'*'*10)
###### Variable
input_data=[1,3,4,5,7]
x=tf.placeholder(dtype=tf.float32)
b=tf.constant(3.0, dtype=tf.float32)
w=tf.Variable([2],dtype=tf.float32)
#### 모델 만들기##
y=w*x+b
#### Variable 초기화 
####  변수 Variable 가 있으면 반드시 초기화
init=tf.global_variables_initializer()
#### 세션 정의
sess=tf.Session()
#### 변수 초기화
sess.run(init)
result=sess.run(y,feed_dict={x:input_data})
print(result)











