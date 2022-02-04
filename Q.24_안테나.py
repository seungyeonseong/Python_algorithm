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
#pg.360
#Q24_안테나(내풀이)

n = int(input())
house = list(map(int,input().split()))
res=[]
ans = 0
for temp in range(1,max(house)+1):
    for j in house:
        ans += abs(j-temp)
    res.append((temp,ans))
    ans = 0

res.sort(key=lambda x:x[1])
print(res[0][0])
    
    

# +
#pg.360
#Q24_안테나(답안 예시)
#중간값(median)에 해당하는 위치의 집에 안테나를 설치해야지 안테나부터 모든 집까지 거리의 총 합이 최소가 됨 

n = int(input())
data = list(map(int,input().split()))

data.sort()

#중간값(median)을 출력
print(data[(n-1)//2])
