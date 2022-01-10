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
#Chapter4 구현

# +
#예제 4-1

#입력
n = int(input())
x=1
y=1
direction = list(input().split())

for i in direction:
    if i == "R":
        y += 1
    elif i =="L":
        y -= 1
    elif i == "U":
        x -= 1
    else:
        x+= 1
    #범위를 지나치면 방금 이동한 것 무시(이동전으로 되돌리기)
    if x==0:
        x+=1
    elif y==0:
        y+=1
print(x,y)

# +
#예제 4-2

#입력
n = int(input())
cnt =0

for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            time = list(str(i)+str(j)+str(k))
            #print(time)
            if str(3)in time:
                #print(time)
                cnt+=1
print(cnt)


# +
#왕실의 나이트 _멍청한 풀이
#입력
n = list(input())
cnt = 0
#print(n)

#행 이름 -> 행 번호로 변환
x = int(ord(n[0])-96)
y = int(n[1])

#방향 
if 1<=x+2<=8 and 1<=y+1<=8:
    cnt+= 1
if 1<=x-2<=8 and 1<=y+1<=8:
    cnt+= 1
if 1<=x+2<=8 and 1<=y-1<=8:
    cnt+= 1    
if 1<=x-2<=8 and 1<=y-1<=8:
    cnt+= 1
if 1<=x+1<=8 and 1<=y+2<=8:
    cnt+= 1
if 1<=x+1<=8 and 1<=y-2<=8:
    cnt+= 1
if 1<=x-1<=8 and 1<=y+2<=8:
    cnt+= 1
if 1<=x-1<=8 and 1<=y-2<=8:
    cnt+= 1
print(cnt)    



# +
#왕실의 나이트 _선녀 풀이
#입력
n = list(input())
cnt = 0
#print(n)

#행 이름 -> 행 번호로 변환


steps=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]


for step in steps:
    x = int(ord(n[0])-96)
    y = int(n[1])
    x = x + step[0]
    y = y + step[1]
    if 1<= x <= 8 and 1<= y <=8:
        cnt += 1
print(cnt)

# +
#게임 개발

#입력
n,m = map(int,input().split())
a,b,d = input().split()
for i in range(n):
    mapp = list(map(int,input().split()))
    
x = mapp[a]
y = mapp[b]

if d == 0:
    if y-1 == 0:
        y -= 1
        cnt +=1
    else:
        
elif d==1:
    x -= 1
elif d==2:
    y += 1
else:
    x += 1
    
    


