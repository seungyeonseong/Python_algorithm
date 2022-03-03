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
#답안예시
#접근법: x로부터 최단경로를 각각 구하기
#모든 간선의 비용이 동일할 때는 bfs을 이용하여 최단거리를 찾을 수 있다

# +
from collections import deque


#도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]

#모든 도로 정보 입력받기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
#모든 도시에 대한 최단 거리 초기화
distance = [-1] *(n+1)
distance[x] = 0    #출발 도시까지의 거리는 0으로 설정

#너비우선탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            #최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
#최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

#만약 최단 거리가 k인 도시가 없다면, -1출력
if check == False:
    print(-1)
    
    

# +
#내풀이:다익스트라 알고리즘으로 풀이

# +
import heapq
INF = int(1e9)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]= 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n, m, k, x = map(int,input().split())
graph=[[]*(n+1) for _ in range(n+1)]
distance= [INF]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    
dijkstra(x)
res = -1
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        res = 1
if res != 1:
    print(res)
        
# -




