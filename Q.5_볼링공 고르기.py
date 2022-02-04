# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#pg.315
#Q5_볼링공 고르기(내풀이)

n,m = map(int,input().split())
ball = list(map(int,input().split()))
li =[]
total = 0

#무게 별 개수를 li리스트에 추가
for x in range(1,m+1):
    if x in ball:
        li.append(ball.count(x))
print(li)

for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        total += li[i]*li[j]
        
print(total)


# +
#pg.315
#Q5_볼링공 고르기(답안 예시)

n,m = map(int,input().split())
data = list(map(int,input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in data:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
#1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]    #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i]*n #B가 선택하는 경우의 수와 곱하기
    
print(result)
