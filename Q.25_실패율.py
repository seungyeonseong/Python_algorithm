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
#pg.361
#Q25_실패율(내풀이)--> 답은 출력되지만 런타임에러로 70.4/100점



#N; 전체 스테이지 수

def solution(N, stages):
    answer = []
    user =[0]
    for i in range(1,N+2):
        user.append(stages.count(i))
    s=0            
    for i in range(1,N+1):
        for j in range(i,N+2):
            s+= user[j]
        answer.append((i,user[i]/s))
        s = 0
    answer.sort(key = lambda x:-x[1])
    answer = [i[0] for i in answer]
 
    return answer



N = int(input())
stages = list(map(int,input().split()))
print(solution(N,stages))


# +
#pg.361
#Q25_실패율(답안예시)

def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1,N+1):
        count =stages.count(i)
        
        if length==0:
            fail = 0
        else:
            fail = count/length
        #삽입
        answer.append((i,fail))
        length -= count
    answer.sort(key = lambda x:-x[1])
    answer = [i[0] for i in answer]
 
    return answer

N = int(input())
stages = list(map(int,input().split()))
print(solution(N,stages))

