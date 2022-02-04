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
#pg.316
#Q6_무지의 먹방 라이브(내풀이)
#프로그래머스에 돌렸는데 효율성 0점으로 틀림

def solution(food_times, k):
    answer = 0
    sec = 0
    li=[]
    while sec < k+1:
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] = food_times[i]-1
                sec += 1
                li.append(i+1)
    
            if sec == k+1:
                answer = li[k]
                #print(li)
                break
            if sum(food_times) == 0:
                return -1
    return answer

food_times = list(map(int,input().split()))
k = int(input())


print(solution(food_times,k))
# -

food_times=[3,1,2]
print(len(food_times))
k=5
cnt=0
while True:
    for i in range(len(food_times)):
        if food_times[i]==0:
            continue
        a=food_times[i]-1
        food_times[i]=a
        answer = i + 1
        cnt += 1
    if cnt == k:
        break
