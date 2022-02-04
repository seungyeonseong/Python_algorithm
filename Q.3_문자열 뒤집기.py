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
#pg.313
#Q3_문자열 뒤집기(내풀이)

data = list(input())    #데이터 입력
group_0 = 0    #0이 연속된 데이터의 개수
group_1 = 0    #1이 연속된 데이터의 개수

#연속된 숫자들의 그룹 수 구하기
#숫자가 달라지는 부분 찾기-> 왼쪽에있던 수에 따라 그룹 개수 추가
for i in range(len(data)-1):
    if data[i] != data[i+1] and data[i] == '0':
        group_0 += 1
    elif data[i] != data[i+1] and data[i] == '1':
        group_1 += 1

#마지막 숫자도 고려해줘야함. 마지막 숫자에 따라 그룹에 추가        
if data[-1] =='0':
    group_0 += 1
elif data[-1] =='1':
    group_1 +=1
    
#print(group_0) 
#print(group_1)

#뒤집는 숫자가 더 작은 쪽 출력
if group_0 >= group_1:
    print(group_1)
else:
    print(group_0)

# +
#pg.313
#Q3_문자열 뒤집기(답안 예시)

#전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산

data = input()
count0 = 0    #전부 0으로 바꾸는 경우
count1 = 0    #전부 1로 바꾸는 경우

#첫번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
#두번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        #다음 수에서 1로 바뀌는 경우
        if data[i+1] =='1':
            count0 += 1
        #다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1
print(min(count0,count1))
