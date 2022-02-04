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
#pg.314
#Q4_만들 수 없는 금액(답안 예시)

a = int(input())
coin = map(int,input().split())
coin = list(coin)
coin.sort()

target = 1
for x in coin:
    #만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
#만들 수 없는 금액 출력
print(target)
