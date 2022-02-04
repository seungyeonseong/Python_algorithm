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
#pg.311
#Q1_모험가 길드(내풀이)

#입력
n = int(input())
li = list(map(int,input().split()))

count = 0

#정렬
li.sort(reverse=True)
#print(li[0])
#print(len(li))
m = li[0]
#최댓값의 수만큼 리스트의 크기를 만든다 
while m <= len(li):
    count += 1
    li = li[max(li):]
    if len(li) > 0: 
        m = li[0]

print(count)

# +
#Q1_모험가 길드(답안 예시)

#공포도를 오름차순으로 정렬 후, 앞에서부터 확인하며 
#'현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다
#크거나 같다면, 이를 그룹으로 설정

n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도가 낮은 것부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가시키기
        count  = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) #총 그룹의 수 출력
