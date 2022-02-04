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
#pg.168
#퀵 정렬 소스 코드

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫 번째 원소
    left = start +1
    right = end
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left>right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot] = array[pivot],array[right]
        else:    #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left],array[right] = array[right], array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
    
quick_sort(array,0,len(array)-1)
print(array)

# +
#pg.169
#파이썬의 장점을 살린 퀵 정렬 소스 코드

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <=1:
        return array
    pivot = array[0]    #피벗은 첫 번째 원소
    tail = array[1:]    #피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot ]    #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot ]    #분할된 오른쪽 부분
    
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] +quick_sort(right_side)

print(quick_sort(array))

# +
#pg.178
#실전 문제_위에서 아래로(내풀이)

#수열의 수
n = int(input())
#수열 입력
li=[]
for i in range(n):
    li.append(int(input()))
    
def func(li):
    li = sorted(li,reverse = True)
    return li

for i in func(li):
    print(i,end=" ")

# +
#pg.180
#실전 문제_성적이 낮은 순서로 학생 출력하기(내풀이)

n = int(input())
li=[]
for i in range(n):
    a,b = input().split()
    li.append((a,b))
#정렬
def data(x):
    return x[1]
li = sorted(li,key = data)

for i in range(len(li)):
    print(li[i][0],end=" ")

# +
#pg.182
#실전 문제_두 배열의 원소 교체(내풀이)

n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = sum(a)
a.sort()
b.sort(reverse=True)

for i in range(n):
    for j in range(n):
        if k==0:
            break
        if a[i] < b[j]:
            a[i],b[j] = b[j],a[i]
            k -= 1
print(sum(a))
    
    
# -


