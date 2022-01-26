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
#92pg
#큰 수의 법칙

#입력
n,m, k = map(int,input().split())
li = list(map(int,input().split()))

result = 0

#정렬
li.sort(reverse=True)

#한 묶음: k번의 최댓값 + 1번의 2번째 최댓값 
result += (li[0]*k+li[1])*(m//(k+1))

#나머지는 무조건 최댓값
result += (m%(k+1))*li[0]
    
print(result)


# +
#96pg
#숫자 카드 게임

n, m  = map(int,input().split())
for i in range(n):
    li[i] = list(map(int,input().split()))

#각 행에서 min값 고르기
m_li =[]
for i in range(n):
    m_li.append(min(li[i]))

#그 중 최댓값 출력
print(max(m_li))
#print(li)
        


# +
#99pg
#1이 될 때까지

n, k = map(int,input().split())

count = 0

while n != 1:
    if n%k == 0:
        n = n//k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

# +
#N이 100억 이상의 큰 수가 되는 경우

#N이 K의 배수가 되도록 한번에 빼는 것이 효율적
n, k = map(int,input().split())

count = 0

while True:
    #(N ==K 로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    count += (n%k)
    n = n-(n%k)
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때 반복문 탈출)
    if n < k:
        break
    n = n//k
    count += 1    
count += (n-1)

print(count)
# -


