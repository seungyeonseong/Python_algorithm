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
#pg.198
#실전문제_부품 찾기(내풀이)-->재귀함수

n = int(input())
li = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

#정렬
li.sort()

def func(array, target, start, end):
    if start > end:
        return print('no')
    mid = (start+end)//2
    if array[mid] == target:
        return print('yes')
    elif array[mid] > target: #타겟이 왼 편에 있으면
        end = mid -1
        func(array,target,start,end)
    else:
        start = mid +1
        func(array,target,start,end)
    
for i in check:
    func(li,i,0,n)


# +
#pg.198
#실전문제_부품 찾기(답안예시)-->반복문

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end= mid -1
        else:
            start = mid +1
            
#가게의 부품 개수 입력
n = int(input())
#가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int,input().split()))
array.sort() #이진 탐색을 수행하기 위해 사전에 정렬 수행

# 손님이 확인 요청한 부품 개수 입력
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))

#손님이 확인 요청한 부품 번호를 공백으로 구분하여 입력
for i in x:
    #해당 부품이 존재하는지 확인
    result = binary_search(array,i,0,n-1)
    if result != None:
        print("yes",end=" ")
    else:
        print("no",end=" ")
            


# +
#pg.198
#실전문제_부품 찾기(답안예시)-->계수 정렬: 리스트의 인덱스에 직접 접근하여 존재하는지 확인

#가게의 부품 개수 입력
n = int(input())
array = [0]*1000001

#가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
for i in input().split():
    array[int(i)] = 1
    
# 손님이 확인 요청한 부품 개수 입력
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))

#손님이 확인 요청한 부품 번호를 공백으로 구분하여 입력
for i in x:
    #해당 부품이 존재하는지 확인
    if array[i] == 1:
        print("yes",end=" ")
    else:
        print("no", end=" ")


# +
#pg.198
#실전문제_부품 찾기(답안예시)-->집합 자료형: 단순히 특정한 수가 한 번이라도 등장했는지 검사

            
#가게의 부품 개수 입력
n = int(input())
#가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = set(map(int,input().split()))

# 손님이 확인 요청한 부품 개수 입력
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))

#손님이 확인 요청한 부품 번호를 공백으로 구분하여 입력
for i in x:
    #해당 부품이 존재하는지 확인
    if i in array:
        print("yes",end=" ")
    else:
        print("no", end=" ")

# +
#pg.201
#실전문제_떡볶이 떡 만들기(내풀이)

#입력
n,m = map(int,input().split())
li = list(map(int,input().split()))
start = 0
end = max(li)

while start <= end:
    
    mid = (start+end)//2
    ans = 0
    for x in li:
        if x > mid:
            ans += x-mid
    if ans < m:
        end = mid -1

    else:
        start = mid +1
print(end)



# +
#pg.201
#실전문제_떡볶이 떡 만들기(답안예시)

#떡의 개수와 요청한 떡의 기리를 입력받기
n,m = map(int,input().split())
#각 떡의 개별 높이 정보를 입력받기
li = list(map(int,input().split()))

#이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(li)

#이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in li:
        #잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x- mid
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid -1
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1
#정답 출력
print(result)
# -




