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
##내풀이,,, 못품 ㅠ
# 아예 아이디어 감이 안잡힘,,,위상정렬 활용을 못하겠음
#역전되는 순위들의 순서를 바꾸자니 '확실한 순위를 찾는 방법'인지 장담불가능,,

#구글링 접근법:
#일관성이 없다=주어진 정보에서 사이클이 발생 
#확실한 순위가 없다 =같은 진입차수에 있어 순서를 구분x
# -


#답안 예시
#작년 순위 정보가 5 4 3 2 1로 주어진다면, 자기보다 낮은 등수를 가진 팀을 가르키도록 방향그래프 설정
#1.노드가 N번 나오기 전에 큐가 비게 된다면, 사이클이 발생한 것
#2.특정 시점에 2개 이상의 노드가 큐에 한꺼번에 들어간다면, 여러가지 결과가 생김
#-->따라서, 위상정렬 수행과정에서 큐에서 노드를 뽑을 때 큐의 원소가 항상 1개로 유지되어야함


# +
from collections import deque

        
#테스트 케이스(test case)만큼 반복
for tc in range(int(input())):
    #노드의 개수 입력받기
    n = int(input())
    #모든 노드에 대한 진입차수는 0으로 초기화
    indegree=[0]*(n+1)
    #각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph=[[False]*(n+1) for i in range(n+1)]
    #작년 순위 정보 입력
    data = list(map(int,input().split()))
    
    #방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    
    #올해 변경된 순위 정보 입력
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        #간선의 방향 뒤집기
        if graph[a][b] :
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1    
            
    #위상 정렬(topology sort) 시작
    result = []    #알고리즘 수행 결과를 담을 리스트
    q = deque()    #큐 기능을 위한 deque 라이브러리 사용
    
    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            
    certain = True    #위상 정렬 결과가 오직 하나인지의 여부
    cycle = False    #그래프 내 사이클이 존재하는지 여부
    
    #정확히 노드의 개수만큼 반복
    for i in range(n):
        #큐가 비어있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        #큐의 원소가 2개이상이라면 가능한 정렬 결과가 여러개라는 의미
        if len(q) >= 2:
            certain = True
            break
        #큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1
                #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)
                    
    #사이클이 발생하는 경우(일관성이 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    #위상 정렬 결과가 여러 개인 경우
    elif not certain:
        print("?")
    #위상 정렬을 수행한 결과 출력
    else:
        for i in result:
            print(i,end=" ")
        print()
# -



