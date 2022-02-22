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
#내풀이,,,못품ㅋ
#접근법:상하좌우로 이동하면서 최단경로 구하기,,dfs/bfs인가?

# +
#답안예시
#2차원 배열의 각 칸을 '노드'로 보고, 상하좌우가 인접하다고 판단

# +
import heapq
#import sys
#input = sys.stdin.readline

INF = int(1e9)    #무한을 의미하는 값으로 10억 설정

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#전체 테스트 케이스(test case)만큼 반복
for tc in range(int(input())):
    #노드의 개수를 입력받기
    n = int(input())
    #전체의 맵 정보를 입력받기
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))
        
    #최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF]*n for _ in range(n)]
    
    x,y = 0,0 #시작 위치는 (0,0)
    #시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y],x,y)]
    distance[x][y] = graph[x][y]
    
    #다익스트라 알고리즘 수행
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist,x,y = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            #맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))
                
print(distance[n-1][n-1])
# -


