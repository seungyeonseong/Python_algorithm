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
#접근법: 모든 여행경로의 출발,목적지마다 연결되어 있는지 확인

# +
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
parent = [i for i in range(n+1)]
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))
    
travel = list(map(int,input().split()))
for i in range(n):
    for j in range(i):
        if li[i][j] == 1:
            union_parent(parent,i+1,j+1)
ans ="YES"            
for x in range(m-1):
    if find_parent(parent,travel[x]) != find_parent(parent,travel[x+1]):
        ans  = "NO"
        break
        
print(ans)
            

# +
##답안예시
#'여행계획'에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능한 여행경로

# +
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
        
#여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n,m = map(int,input().split())
parent = [0]*(n+1)  #부모 테이블 초기화

#부모테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i] = i
    
#union 연산을 각각 수행
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:  #연결된 경우 union 연산 수행
            union_parent(parent,i+1,j+1)
#여행계획 입력받기
plan = list(map(int,input().split()))

result =True
#여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m-1):
    if find_parent(parent,plan[i]) != find_parent(parent,plan[i+1]):
        result = False
        
#여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지) 확인
if result:
    print("YES")
else:
    print("NO")
