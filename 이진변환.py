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
def d(n):
    if n==1:
        return '1'
    elif n==0:
        return '0'
    if n%2==0:
        return d(n//2)+'0'
    else:
        return d(n//2)+'1'

print(d(8))
# -

bin(8)[2:]
