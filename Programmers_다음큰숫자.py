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

def solution(n):
    answer = n+1
    bi = bin(n)[2:]
    cnt = bi.count("1")
    while True:
        if bin(answer)[2:].count("1")==cnt:
            return answer
        answer +=1 
