# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:32:40 2019

@author: kosmo05-teacher
"""

# 단열 주석
"""
다열주석
"""
#변수: 숫자형
a=1
a=1.1
b=5
# 변수 타입이 없음 문자열 홑따옴표 쌍따옴표 무관
a="안녕하세요"
a='hello world'
#a='문자열"  따옴표 혼용 금지
# 리스트형 []
a=[1,2,"3입니다.",4,'4',[5,6,7]]
#리스트 접근방식 0부터 시작하는 인덱스 로 접근
a=a[4]
#튜플()  변형 불가 리스트
a=(1,3,3,'4',"test",['part',1,2])
# 접근방식 인덱스
a=a[4]
# 수정시도 에러
#a[4]='111'

# 딕셔너리 : 객체화 {key:value}
a={'name':'홍길동','age':14}
#접근방식: key
a['age']=22
a=a['age']
# 집합 {} 중복 허용 금지
a=set([1,2,3,3])
# bool 불 참 /거짓
a=True
#print("답은",a)
########### 제어문
#if 판단문
a=3
b=3
if a>b:
    print("a는","b보다","큽니다.")
elif a==b:
    print("a는","b와","같습니다.")
else:
    print("a는","b보다","작습니다.")
######### for ####
# range 는 시작은 포함 끝은 불포함
for i in range(2,5):
    print("답은",i)

week=['월','화','수','목','금','토','일']
for day in week:
    print("오늘은",day,"입니다.")
    
#### while 조건식 조건에 맞을때 까지 반복
i=0
while i<10:
    i+=1
    print(i,"번째입니다.")

############### def 함수명(): 선언부
### 매개변수 없음
def test():
    print("함수 test:")
###  실행부 잘쓰는 부분 반복사용용 구문
test()
### 매개변수와 리턴값이 있는 함수
def  add(x,y):
    return x+y

c = add(7,3)
print(" 답은",c,"입니다." )

############# 클래스 class 클래스명:
### 함수명뒤에는 괄호 클래스뒤에는 없음
class Calc:
    def __init__(self):
        self.res=0
        
    def add(self,a):
        self.res+=a
        print("결과는",self.res)
        return self.res
    
    def minus(self,a):
        self.res-=a
        print("결과는",self.res)
        return self.res        

    def mul(self,a):
        self.res*=a
        print("결과는",self.res)
        return self.res
    
    def div(self,a):
        self.res/=a
        print("결과는",self.res)
        return self.res
print("*"*50)
c1=Calc() # 클래스 인스턴스 생성
c1.add(1)
c1.mul(10)
c1.div(5)
c1.minus(3)