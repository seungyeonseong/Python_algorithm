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
#pg.312
#Q2_곱하기 혹은 더하기(내풀이)

num = list(input()) #문자열로 받아서 리스트로 넣기

total = int(num[0]) #첫 문자를 total로 저장, 배열끝까지 연산 비교
#print(total)
#print(num)

for i in range(1,len(num)): 
    if total*int(num[i]) >= (total + int(num[i])): #덧셈와 곱셈의 크기 비교
        total = total*int(num[i])
    else:
        total = (total + int(num[i]))
        
        
print(total)

# +
#pg.312
#Q2_곱하기 혹은 더하기(답안 예시)

#두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1이하인 경우에는
#더하며, 두 수가 모두 2이상인 경우에는 곱하면 된다.

data = input()

#첫 번째 문자를 숫자로 변경하며 대입
result = int(data[0])

for i in range(1,len(data)):
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num
        
print(result)
