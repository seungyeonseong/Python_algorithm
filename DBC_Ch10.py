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
#기본적인 서로소 집합 알고리즘 소스코드

#특정한 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
#노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = map(int,input().split())
parent = [0]*(v+1)    #부모 테이블 초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

#union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
    
#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=" ")
for i in range(1,v+1):
    print(find_parent(parent,i),end=" ")
print()

#부모 테이블 내용 출력
print('부모 테이블: ',end=" ")
for i in range(1,v+1):
    print(parent[i],end=' ')


# +
#경로 압축 기법 소스코드

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


# +
#개선된 서로소 집합 알고리즘 소스코드

#특정한 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
#노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = map(int,input().split())
parent = [0]*(v+1)    #부모 테이블 초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

#union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
    
#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=" ")
for i in range(1,v+1):
    print(find_parent(parent,i),end=" ")
print()

#부모 테이블 내용 출력
print('부모 테이블: ',end=" ")
for i in range(1,v+1):
    print(parent[i],end=' ')


# +
#서로소 집합을 활용한 사이클 판별 소스코드

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
#노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int,input().split())
parent = [0]*(v+1)    #부모 테이블 초기화

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i
    
cycle = False    #사이클 발생 여부

for i in range(e):
    a,b = map(int,input().split())
    #사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    #사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent,a,b)
        
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
# +
#크루스칼 알고리즘 소스코드

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
        
#노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int,input().split())
parent = [0] *(v+1)    #부모 테이블 초기화

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i
    
#모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))
    
#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        
print(result)
    


# +
#위상 정렬 소스코드

from collections import deque

#노드의 개수와 간선의 개수를 입력받기
v,e = map(int,input().split())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

#방향그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)    #정점 A에서 B로 이동 가능
    #진입차수를 1 증가
    indegree[b] += 1
    
#위상 정렬 함수
def topology_sort():
    result =[]    #알고리즘 수행 결과를 담을 리스트
    q = deque()   #큐 기능을 위한 deque 라이브러리 사용
    
    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
            
    #큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                
    #위상 정렬을 수행한 결과 출력
    for i in result:
        print(i,end=" ")
        
topology_sort()
    

# +
#pg.298
#실전문제_팀 결성(내풀이)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b :
        parent[b] = a
    else:
        parent[a] = b
        
def check_parent(parent,a,b):
    if find_parent(parent,a) == find_parent(parent,b):
        return "yes"
    else:
        return "no"
        
        
n,m = map(int,input().split())
parent = [i for i in range(0,n+1)]

for _ in range(m):
    x,a,b = map(int,input().split())
    if x==0:
        union_parent(parent,a,b)
    else:
        print(check_parent(parent,a,b))
        
        


# +
#pg.298
#실전문제_팀 결성(답안예시)

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a <b:
        parent[b] = a
    else:
        parent[a] = b
        
n,m = map(int,input().split())
parent=[0]*(n+1)  #부모 테이블 초기화

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0,n+1):
    parent[i] = i
    
#각 연산을 하나씩 확인
for i in range(m):
    oper,a,b = map(int,input().split())
    #합집합(union) 연산인 경우
    if oper == 0:
        union_parent(parent,a,b)
    #찾기(find) 연산인 경우
    elif oper == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')


# +
#pg.300
#실전문제_도시 분할 계획(내풀이)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
 
parent=[i for i in range(n+1)]

cost = []
for _ in range(m):
    a,b,c = map(int,input().split())
    cost.append((c,a,b))
    
    
cost.sort()

total =  0
last = 0
for i in cost:
    a,b = i[1],i[2]
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total += i[0]
        last = i[0]
print(total-last)


# +
#pg.303
#실전문제_커리큘럼(답안 예시)

#각 노드에 대하여 인접한 노드를 확인할 때, 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우를 찾는다면,
#더 오랜 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블을 갱신한다.

from collections import deque
import copy

#노드의 개수 입력받기
 v = int(input())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]
#각 강의 시간을 0으로 초기화
time = [0] *(v+1)
#방향 그래프의 모든 간선 정보를 입력받기
for i in range(1,v+1):
    data = list(map(int,input().split()))
    time[i] = data[0]    #첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
#위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)    #알고리즘 수행 결과를 담을 리스트
    q = deque()    #큐 기능을 위한 deque 라이브러리 사용
    
    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] ==0:
            q.append(i)
            
    #큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                
    #위상 정렬을 수행한 결과 출력
    for i in range(1,v+1):
        print(result[i])
        
topology_sort()

