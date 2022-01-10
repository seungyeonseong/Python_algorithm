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
#Chapter 5 DFS/BFS

# +
#인접 행렬
#2차원 배열에 각 노드가 연결된 형태를 기록하는 방식

INF = 9999999999 #무한의 비용

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# +
#인접 리스트
#모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저징

#행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

#노드0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

#노드2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)


# +
#DFS 예제

#DFS 메서드 정의
def dfs(graph,v,visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v,end=" ")
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9


#정의된 DFS 함수 호출

dfs(graph,1,visited)
# -

visited = [False]*9
visited

# +
#BFS 예제
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start]) 
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=" ")
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9


#정의된 BFS 함수 호출
bfs(graph,1,visited)


# +
#실전문제
#3_음료수 얼려먹기

#입력
n, m = map(int,input().split())

#얼음틀
graph =[]
for _ in range(n):
    graph.append(list(map(int,input())))
    

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<= -1 or x >= n or y <= -1 or y>=m:
                 return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
                 graph[x][y] = 1 #해당 노드 방문 처리
                 dfs(x-1,y)      #상,하,좌,우 위치도 재귀 처리
                 dfs(x+1,y)
                 dfs(x,y+1)
                 dfs(x,y-1)
                 return True
    return False
                 
#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
        for j in range(m):
                 #현재위치에서 DFS수행
                 if dfs(i,j) == True:
                     result += 1
print(result)
# -


