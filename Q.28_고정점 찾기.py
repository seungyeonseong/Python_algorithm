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
#내풀이(반복문)

# +
n = int(input())
li = list(map(int,input().split()))

def binary_search(li,start,end):
    while start <= end:
        mid = (start+end)//2
        if li[mid]==mid:
            return mid
        elif li[mid]  > mid:
            end = mid -1
        else:
            start = mid +1
res = binary_search(li,0,n-1)
if res is  None:
    print(-1)
else:
    print(res)
            

# +
#답안예시

# +
#이진 탐색 소스코드 구현(재귀함수)
def binary_search(array,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    #고정점을 찾은 경우 인덱스 반환
    if array[mid] ==mid:
        return mid
    #중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array,start,mid-1)
    #중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,mid+1,end)
    
n = int(input())
array = list(map(int,input().split()))

#이진 탐색(binary_search) 수행
index = binary_search(array,0,n-1)

#고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
#고정점이 있는 경우 해당 인덱스 출력
else:
    print(index)
