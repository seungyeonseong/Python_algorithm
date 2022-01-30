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
####엉망진창 오류 난리남 주의
#접근법
#해당 부분의 상하좌우 살펴서 범위 벗어나지 않으면서 값이 0으로 접근가능할 때
# 상하좌우로 이동해서 반복 실행하도록, 더 이상 이동할 수 없을 때 ans += 1하는 함수를 구현하고자힘.

#정답은 DBC_Ch5에 있음

# +
#pg.149
#음료수 얼려 먹기(내풀이)



#입력
n,m = map(int,input().split())
ice = list(list(map(int,input())) for i in range(n))

#상하좌우에 '0'이 있나 확인
def dfs(ice,i,j):
    ans = 0 
    direction(ice,i,j)
    if direction(ice,i,j) == False:#이동할 수 있는지 확인
        ans += 1
    if direction(ice,i,j) == 'left':
        ice[i][j-1] = 1 #방문 처리
        dfs(ice,i,j-1)
    elif direction(ice,i,j) == 'right':
        ice[i][j+1] = 1 #방문 처리
        dfs(ice,i,j+1)
    elif direction(ice,i,j) == 'up':
        ice[i-1][j] = 1 #방문 처리
        dfs(ice,i+1,j)
    elif direction(ice,i,j) == 'down':
        ice[i+1][j] = 1 #방문 처리
        dfs(ice,i+1,j)
    return ans
    
        
    
        
    
#상하좌우 확인하는 함수
def direction(ice,i,j):
    #상 빙향 확인
    if ice[i-1][j] == 0 and i != 0 :
        return 'up'
    elif ice[i+1][j] == 0 and i != n-1:
        return 'down'
    elif ice[i][j-1]==0 and j!=0 :
        return 'left'
    elif ice[i][j+1] == 0 and j != n-1:
        return 'right'
    else:
        return False
    
    

print(dfs(ice,0,0))


# +
#pg.152
#미로 탈출(답안 예시)

# +
from collections import deque

n,m = map(int,input().split())
graph =[list(map(int,input())) for _ in range(n)]

dx = [0,1,0,-1] #동->남->서->북 방향으로 확인
dy = [1,0,-1,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue: #큐가 빌 때까지 반복
        x,y = queue.popleft()
        #현재 위치에서 4 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] ==0:
                continue
                
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
# -


