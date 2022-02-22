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
#내풀이
#접근법:'4'가 갈 수 있는 노드+'4'로 올 수 있는 노드의 합 = n-1 일 때 만족

# +
n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] == 1:
                continue
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1
ans = 0
for i in range(1,n+1):
    s= sum(graph[i])
    for j in range(1,n+1):
        s += graph[j][i]
    if s == n-1:
        ans += 1
print(ans)
    
                


# +
#답안예시
#성적이 낮은 학생이 높은 학생을 가르키는 방향 그래프로 표현 -> 최단 경로 알고리즘

# +
INF = int(1e9)    #무한을 의미하는 값으로 10억을 설정

#노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
#2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
            
#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    #A에서 B로 가는 비용을 1로 설정
    a,b = map(int,input().split())
    graph[a][b] = 1
    
#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

result = 0
#각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)
        
# -


