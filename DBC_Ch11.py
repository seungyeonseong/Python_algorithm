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
#pg.311
#Q1_모험가 길드(내풀이)

#입력
n = int(input())
li = list(map(int,input().split()))

count = 0

#정렬
li.sort(reverse=True)
#print(li[0])
#print(len(li))
m = li[0]
#최댓값의 수만큼 리스트의 크기를 만든다 
while m <= len(li):
    count += 1
    li = li[max(li):]
    if len(li) > 0: 
        m = li[0]

print(count)
    


# +
#Q1_모험가 길드(답안 예시)

#공포도를 오름차순으로 정렬 후, 앞에서부터 확인하며 
#'현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다
#크거나 같다면, 이를 그룹으로 설정

n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도가 낮은 것부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가시키기
        count  = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) #총 그룹의 수 출력



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

# +
#pg.313
#Q3_문자열 뒤집기(내풀이)

data = list(input())    #데이터 입력
group_0 = 0    #0이 연속된 데이터의 개수
group_1 = 0    #1이 연속된 데이터의 개수

#연속된 숫자들의 그룹 수 구하기
#숫자가 달라지는 부분 찾기-> 왼쪽에있던 수에 따라 그룹 개수 추가
for i in range(len(data)-1):
    if data[i] != data[i+1] and data[i] == '0':
        group_0 += 1
    elif data[i] != data[i+1] and data[i] == '1':
        group_1 += 1

#마지막 숫자도 고려해줘야함. 마지막 숫자에 따라 그룹에 추가        
if data[-1] =='0':
    group_0 += 1
elif data[-1] =='1':
    group_1 +=1
    
#print(group_0) 
#print(group_1)

#뒤집는 숫자가 더 작은 쪽 출력
if group_0 >= group_1:
    print(group_1)
else:
    print(group_0)

# +
#pg.313
#Q3_문자열 뒤집기(답안 예시)

#전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산

data = input()
count0 = 0    #전부 0으로 바꾸는 경우
count1 = 0    #전부 1로 바꾸는 경우

#첫번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
#두번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        #다음 수에서 1로 바뀌는 경우
        if data[i+1] =='1':
            count0 += 1
        #다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1
print(min(count0,count1))

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
# +
#pg.315
#Q5_볼링공 고르기(내풀이)

n,m = map(int,input().split())
ball = list(map(int,input().split()))
li =[]
total = 0

#무게 별 개수를 li리스트에 추가
for x in range(1,m+1):
    if x in ball:
        li.append(ball.count(x))
print(li)

for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        total += li[i]*li[j]
        
print(total)



# +
#pg.315
#Q5_볼링공 고르기(답안 예시)

n,m = map(int,input().split())
data = list(map(int,input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in data:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
#1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]    #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i]*n #B가 선택하는 경우의 수와 곱하기
    
print(result)


# +
#pg.316
#Q6_무지의 먹방 라이브(내풀이)
#프로그래머스에 돌렸는데 효율성 0점으로 틀림

def solution(food_times, k):
    answer = 0
    sec = 0
    li=[]
    while sec < k+1:
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] = food_times[i]-1
                sec += 1
                li.append(i+1)
    
            if sec == k+1:
                answer = li[k]
                #print(li)
                break
            if sum(food_times) == 0:
                return -1
    return answer

food_times = list(map(int,input().split()))
k = int(input())


print(solution(food_times,k))


# -



