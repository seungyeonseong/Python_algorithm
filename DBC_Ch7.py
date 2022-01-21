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
#Chapter7_이진 탐색

# +
#순차 탐색 소스코드 구현

def sequential_search(n, target, array):
    #각 원소를 하나씩 확인하며
    for i in range(n):
        #현재의 원소가 찾고자하는 원소와 동일한 경우
        if array[i] == target:
            return i+1 #현재의 위치 반환(인덱스는 0부터 시작하므로 1더하기)
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) #원소의 개수
target = input_data[1] #찾고자하는 문자열

print("앞서 적은 원소 개수 만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

#순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))


# +
#재귀함수로 구현한 이진 탐색 소스코드

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자하는 값이 적은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start,mid-1)
    #중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)

#n(원소의 개수)과 target(찾고자하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
#전체 원소 입력받기
array = list(map(int,input().split()))

#이진탐색 수행 결과 출력
result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)


# +
#반복문으로 구현한 이진 탐색 소스코드

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        #찾은 경우 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1 
        #중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid +1
    return None

#n(원소의 개수)와 target(찾고자하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
#전체 원소 입력받기
array = list(map(int,input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

# +
#한 줄 입력받아 출력하는 소스코드
import sys
#하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

#입력받은 문자열 그대로 출력
print(input_data)

# +
#실전문제_부품찾기(내 풀이)
n = int(input())
li = list(map(int,input().split()))

m = int(input())
check = list(map(int,input().split()))

for i in check:
    if i in li:
        print("yes",end=' ')
    else:
        print("no",end = ' ')


# +
#실전문제_부품찾기(이진 탐색)

#이진탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        #중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

#N(가게의 부품 개수) 입력
n = int(input())
#가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int,input().split()))
array.sort() #이진탐색을 수행하기 위해 사전에 정렬 수행
#M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    #해당 부품이 존재하는지 확인
    result = binary_search(array,i,0,n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')


# +
#실전문제_부품찾기(계수 정렬)

#N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0]*1000001

#가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

#M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))
#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    #해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes',end=' ')
    else:
        print('no', end=' ')


# +
#실전문제_부품찾기(집합자료형 이용)

#N(가게의 부품 개수)을 입력받기
n = int(input())
#가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int,input().split()))

#M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x= list(map(int,input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    #해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# +
#실전문제_떡볶이 떡 만들기(내풀이)

n,m =map(int,input().split())
li = list(map(int,input().split()))
li.sort()
length = li[-1]

while (1):
    s = 0
    for i in li:
        if length < i:
            s += (i-length)
    if s >= m:
        break
    else:
        length -= 1
    
print(length)




# +
#실전문제_떡볶이 떡 만들기(답안예시)

#떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n,m = list(map(int,input().split(' ')))
#각 떡의 개별 높이 정보를 입력받기
array = list(map(int,input().split()))

#이진탐색을 위한 시작점과 끝 점 설정
start =0 
end = max(array)

#이진탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        #잘랐을때의 떡의 양 계산
        if x > mid:
            total += x-mid
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
    if total <m:
        end=mid-1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1
#정답 출력
print(result)
# -


