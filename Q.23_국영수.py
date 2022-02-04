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
#pg.359
#Q23_국영수(내풀이)

n = int(input())
li =[]
for i in range(n):
    input_data = list(input().split())
    li.append((input_data[0],int(input_data[1]),int(input_data[2]),int(input_data[3])))
#이름 사전 순
def data(x):
    return ord(x[0])
li.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))

for i in li:
    print(i[0])
