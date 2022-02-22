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
#접근법:1번에서 최단 거리가 가장 큰 것-->다익스트라
#접근,풀이 맞긴한데 다익스트라 알고리즘 구현하는 과정 책 참고함 ㅋㅎ 

# +
import heapq

INF = int(1e9)

n,m = map(int,input().split())

graph=[[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append((y,1))
    graph[y].append((x,1))
    
def dijkstra(start):
    
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(1)
res=0
cnt = 0
for i in range(2,n+1):
    if distance[i]>res:
        res = distance[i]
        index = i
for i in range(2,n+1):
    if res == distance[i]:
        cnt+=1
print(index,res,cnt)
        
    
    
        
    
