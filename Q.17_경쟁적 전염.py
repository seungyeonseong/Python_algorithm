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
###내풀이
#접근법: 1~k까지 순서대로 좌표 찾아서 append하고 q.append()할 때 sec추가해서 해당 시간에 반복문 탈출

# +
from collections import deque


dx = [1,0,-1,0]
dy = [0,1,0,-1]


n,k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
s,x,y = map(int,input().split())

q =deque()
for v in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:
                q.append((i,j,0))

while q:
    a,b,sec = q.popleft()
    if sec == k:
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or nx >=n or ny <0 or ny >=n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[a][b]
            graph.append((nx,ny,sec+1))
        
        
print(graph[x-1][y-1])
    

# +
#답안예시
#낮은 번호부터 증식하므로, 초기에 큐에 원소를 낮은 번호부터 삽입 후 bfs로 해결

# +
from collections import deque

n,k = map(int,input().split())

graph = []    #전체 보드 정보를 담는 리스트
data = []    #바이러스에 대한 정보를 담는 리스트

for i in range(n):
    #보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int,input().split())))
    for j in range(n):
        #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            #(바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j],0,i,j))
            
#정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s,target_x,target_y  = map(int,input().split())

#바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#너비 우선 탐색(BFS) 진행
while q:
    virus,s,x,y = q.popleft()
    #정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    #현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and  0 <=ny and ny < n:
            #아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))
                
print(graph[target_x -1][target_y -1])
# -


