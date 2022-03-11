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

###내풀이 --> 50/100 예제 정답, 1~4번 테스트 중 1,2번 실패


# +
from collections import deque

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    answer=[]
    answer.append("ICN")
    tickets.sort(key = lambda x:x[1])
    visited = [0]*(len(tickets))
    
    while sum(visited) != len(tickets):
        for i in range(len(tickets)):
            if tickets[i][0] == answer[-1] and visited[i] == 0:
                answer.append(tickets[i][1])
                visited[i] = 1
    
    return answer

print(solution(tickets))

# +
#고수의 방법,,
#1.주어진 티켓들을 dictionary형식(출발점-도착점)으로 저장
#2.ICN을 기준으로 dictionary를 탐색하여 스택을 쌓아줌
#3.더 이상 쌓을 스택이 존재하지 않으면 스택의 top부터 확인하면서 dictionary에 스택의 top으로 시작하는 경로가 있는지 확인
#4. 없을 경우 스택의 top을 answer배열에 넣어주고 만약 새로운 경로가 있다면 다시 dictionary를 탐색하면서 스택을 쌓아줌
#5. 결과적으로 스택의 top은 정답의 뒤부터 탐색했으므로 뒤집어줌

# +
import collections import defaultdict

def solution(tickets):
    answer =[]
    routes = defaultdict(list)
    
    for ticket in tickets:
        routes[tickets[0]].append(ticket[1])
        
    for key in routes.key():
        routes[key].sort(reverse=True)
        
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    
    return answer
    
