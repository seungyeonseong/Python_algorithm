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
n,m = map(int,input().split())

from itertools import combinations

items = [i for i in range(1,n+1)]
for k in list(combinations(items,m)):
    for i in range(m):
        print(k[i],end=" ")
    print()
    
# -


