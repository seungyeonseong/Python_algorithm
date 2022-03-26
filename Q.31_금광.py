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
##내풀이
#1.일차원 리스트 ->2차원
#2. dp 작성
# -

for _ in range(int(input())):
    n, m = map(int,input().split())
    graph=[[] for _ in range(m)]
    li = list(map(int,input().split()))
    for i in range(n*m):
        j = i%m
        graph[j].append(li[i])

    dp=[[0]*n for _ in range(m)]
    dp[0]=graph[0]
    for i in range(1,m):
        for j in range(n):
            if j ==0:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j+1])+graph[i][j]
            elif j==n-1:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+graph[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+graph[i][j]
    print(max(dp[-1]))    
    

# +
#답안예시
#2차원 테이블을 이용한 다이나믹 프로그래밍
#왼쪽위, 왼쪽 아래, 왼쪽에서 오는 경우 존재
# -

#tc입력
for tc in range(int(input())):
    #금광 정보 입력
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    
    #다이나믹 프로그래밍을 위한 DP 테이블 초기화
    dp=[]
    index=0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    #다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i==0:
                left_up=0
            else:
                left_up= dp[i-1][j-1]
            #왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j]= dp[i][j]+max(left_up,left_down,left)
            
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
        
    print(result)
        
