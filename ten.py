# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:40:40 2019

@author: kosmo_27
"""

import tensorflow as tf

## 텐서플로우 시작
print("============================================================")

## 노드를 설정(텐서 정의)
hello=tf.constant("Hello tensor!")
print(hello);
## 실행부(세션정의및 처리) - 
sess = tf.Session() ## 세션 객체 생성 -> 각각을 따로 관리 하나봄
print(type(sess));
print(sess.run(hello)); ## 세션 rum

print("##---------------------------------------------------")
print("##상수---------------------------------------------------")
print("##---------------------------------------------------")

print("------------------------------------------------------------")
sess.close() ## 인트턴스 반납
print("연산------------------------------------------------------------")
node1 = tf.constant(3)
node2 = tf.constant(4.0)
node3 = tf.constant(5,dtype=tf.float32)
print("3:",node1) ## 묵시적으로 반환형 인식 
print("4.0:",node2) ## 반환형 기본값 인식 
print("5 dtype:",node3) ## 반환형 변경(명시적 데이터 타입 지정)
print("node1------------------------------------------------------------")
sess = tf.Session()
print(sess.run(node1)); ## 세션 rum
sess.close()
print("node2------------------------------------------------------------")
sess = tf.Session()
print(sess.run(node2)); ## 세션 rum
sess.close()
print("node3------------------------------------------------------------")
sess = tf.Session()
print(sess.run(node3)); ## 세션 rum
sess.close()
print("node5------------------------------------------------------------")
## 반환형을 맞추어야 한다 
node4=tf.add(node3,node2)
node5=node4*node3
print("node5",node5)
print("node5->Session---------------------------------------------------")
sess = tf.Session()
print("result =",sess.run(node5)); ## 세션 rum
sess.close()

print("##---------------------------------------------------")
print("##변수[데이터,가중치]---------------------------------------------------")
print("##ml용 데이터변수의 입력부 placeholder---------------------------------------------------")
print('-'*50)
x = tf.placeholder(dtype=tf.float32)
print("placeholder",x)
y=tf.multiply(x,2.0)
sess = tf.Session()

## placeholder가 들어갈떄
## run에 입력 데이터를 딕셔너리 형태로 넣어 주어야 한다 

input_data = [1,3,5,7,9,0] ## 사전 형식 
result=sess.run(y,{x:input_data})
print(result)
sess.close()
print('-'*20,"변수 Variable",'-'*20)
input_data = [1,3,4,5,7]
x=tf.placeholder(dtype=tf.float32)
b=tf.constant(3.0,dtype=tf.float32)
w=tf.Variable([2],dtype=tf.float32)
print('-'*20,"모델만들기",'-'*20)
y=w*x+b
print('-'*20,"Variable 초기화",'-'*20)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) ## 세션 rum

result=sess.run(y,feed_dict={x:input_data})
print(result) ## 세션 rum







print("============================================================")
