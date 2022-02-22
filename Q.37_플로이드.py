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
#접근법:플로이드 워셜 알고리즘

# +
n = int(input())
m = int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if c < graph[a][b]:
        graph[a][b] = c
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end=" ")
    print()
    

# +
#답안예시
#도시의 개수n 이 100개 이하의 정수이므로 플로이드 워셜 알고리즘 이용하는 것이 효과적

# +
INF = int(1e9)    #무한을 의미하는 값으로 10억을 설정

#노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
#2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a ==b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    #A에서 B로 가는 비용은 C라고 설정
    a,b,c= map(int,input().split())
    #가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
#수행된 결과를 출력
for a in range(1,n+1):
    for b  in range(1,n+1):
        #도달할 수 없는 경우, 0을 출력
        if graph[a][b] == INF:
            print(0,end=" ")
        #도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b],end=" ")
        print()
