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

# [최단경로]
# 벨만-포드 알고리즘
# -방향 그래프에서 음의 가중치를 지닌 간선이 존재할 때 사용
# -음의 순환이 있는 경우 최단 거리를 찾지 못함
#
# +원리
# -시작 노드에 대해 거리를 0, 나머지는 INF으로 초기화
# -정점 수 n-1만큼 다음 과정 반복
# -매 반복마다 모든 간선 확인
# -현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 정보 갱신
# -n-1번 반복 후, n번째 반복에서도 거리 값이 갱신된다며 음수 순환 존재
#
# +다익스트라와의 차이점은 매 반복마다 모든 간선을 확인한다는 것, 다익스트라는 방문하지 않은 노드 중에서 최단거리가 가장 가까운 노드만을 방문
#
#

# +
#백준 11657 타임머신

#import sys
#input = sys.stdin.readline
INF = int(1e9)  #무한을 의미하는 값으로 10억을 설정

def bf(start):
    dist[start] = 0 #시작 노드에 대해서 초기화
    for i in range(n):  #전체 n번의 라운드를 반복
        for j in range(m):  #매 반복마다 "모든 간선"을 확인하며
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                #n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False

#노드의 개수, 간선의 개수 입력받기
n,m = map(int,input().split())
#모든 간선에 대한 정보를 담는 리스트 만들기
edges=[]
#최단 거리 테이블을 모두 무한으로 초기화
dist = [INF]*(n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a,b,c))
    
#벨만-포드 알고리즘 수행
negative_cycle = bf(1) #1번 노드가 시작 노드

if negative_cycle:
    print("-1")
else:
    #1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리 출력
    for i in range(2,n+1):
        if dist[i] == INF:
            print("-1")  #도달할 수 없는 경우, -1을 출력
        else:
            print(dist[i]) #도달할 수 있는 경우 거리를 출력
                


