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

# CH3 greedy algorithm


# +

#거스름돈
n = 1260
count =0

#큰 단위부터 차례대로 확인
coin_types = [500,100,50,10]

for coin in coin_types:
    count += n//coin
    n %= coin

print(count)


# +
#큰수의 법칙
#입력 
n,m,k = map(int,input().split())
li = list(map(int,input().split()))
total=[]

#정렬
li.sort()

#m번 더해질 수 있다
while (1):
    if len(total)==m:
        break
    else:
        for _ in range(k):
            total.append(li[-1])
    if len(total) == m:
            break
    else:
        total.append(li[-2])

print(sum(total))
# -

a= [6,3,3]
a.sort()
print(a)
print(a[-2])
print(a[-3])

# +
#숫자카드 게임

#입력
n,m = map(int,input().split())
minimum=[]
for i in range(n):
    card = []
    card = list(map(int,input().split()))
    minimum.append(min(card))
print(max(minimum))

# +
#1이 될때 까지
n, k = map(int,input().split())
cnt = 0

while n != 1:
    if n%k == 0:
        n = n//k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)

# -


