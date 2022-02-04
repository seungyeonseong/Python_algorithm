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
#pg.363
#Q.26_카드 정렬하기(내풀이)


n = int(input())
card =[]
for i in range(n):
    card.append(int(input()))

card.sort()
cnt=card[0]
res= 0
if n ==1:
    print(cnt)
else:
    for i in range(1,n):
        cnt = cnt+card[i]
        res += cnt
    print(res)

    

# +
#pg.363
#Q.26_카드 정렬하기(답안 예시)

#항상 작은 크기의 두 카드 묶음을 힙쳤을 때 최적의 해 보장
#--> 우선순위 큐를 이용하면 효과적으로 수행할 수 있음
#다익스트라 알고리즘 공부 후 다시 보기

import heapq

n =  int(input())

#힙(heap)에 초기 카드 묶음을 모두 삽입
heap=[]
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)
    
result = 0
    
#힙의 원소가 1개 남을 때까지
while len(heap) != 1:
    #가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    #카드 묶음을 합쳐서 다시 삽입 
    sum_value =one +two
    result += sum_value
    heapq.heappush(heap,sum_value)
        
print(result)
        

# -


