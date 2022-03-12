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
        
INF = int(1e9)
def solution(n, edges):
    answer = 0
    parent =[i for i in range(n)]
    distance=[[INF]*n for _ in range(n)]
    for i in edges:#    union_parent(parent,i[0],i[1])
        distance[i[0]][i[1]] = 1
        distance[i[1]][i[0]] = 1
    for i in range(n):
        for j in range(n):
            if i==j:
                distance[i][j] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])
    li=[]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i ==j or i==k or j==k:
                    continue
                if distance[i][j]+distance[j][k]==distance[i][k]:
                    li.append((i,j,k,distance[i][j],distance[j][k]))           


    
    
    return li

#edges = [[0,1],[0,2],[1,3],[1,4]]
edges = [[2,3],[0,1],[1,2]]
solution(5,edges)

# +


def fac(n):
    if n ==1:
        return 1
    if n==0:
        return 1
    return fac(n-1)*n

def solution(width, height, diagonals):
    answer = 0
    i=[0,0]
    i[0],i[1] = diagonals[0][0], diagonals[0][1]
    answer += fac(width+height-1)/fac(width)/fac(height-1)
    answer += fac(width+height-1)/fac(width-1)/fac(height)
    answer = answer*len(diagonals)
    return answer%10000019

diagonals = [[1,1],[2,2]]
solution(2,2,diagonals)
# -


