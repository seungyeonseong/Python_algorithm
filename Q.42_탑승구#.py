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
###내풀이 못품 ㅠ
#접근법: 도킹가능한 탑승구번호 정렬 (탑승구 번호,비행기번호)
#-> 탑승구 최소 번호부터 배치 후 비행기 순서대로 도킹확인
#근데 find/union 연산 활용 방법이 떠오르지 않음,,,

# +
###답안예시
#접근법__서로소 집합 자료구조 이용!
#1.비행기 순서대로 가능한 큰 번호의 탑승구로 도킹
#2.도킹은 해당 집합을 왼쪽에 있는 집합과 합치는 연산으로 수행
#3.단, 집합의 루트가 0이면, 더 이상 도킹이 불가능한 것으로 판단

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
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
#탑승구의 개수 입력받기
g = int(input())
#비행기의 개수 입력받기
p = int(input())
parent = [i for i in range(0,g+1)]  #부모 테이블상에서, 부모를 자기 자신으로 초기화

result = 0
for _ in range(p):
    data = find_parent(parent,int(input()))  #현재 비행기의 탑승구의 루트 확인
    if data == 0:    #현재 루트가 0이라면, 종료
        break
    union_parent(parent,data,data-1)    #그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1
    
print(result)
# -


