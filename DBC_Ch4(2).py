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
#110pg
#상하좌우(내풀이)

n= int(input())
li =list(input().split())

def func(li):
    x,y = 1,1
    
    for i in li:
        if i == "L" and y>1:
            y -= 1
        elif i =="R" and y <n :
            y += 1
        elif i =="U" and x >1:
            x -= 1
        elif i=="D" and y<n:
            x += 1
        else:
            continue
    return print(x,y)

func(li)
        

# +
#110pg
#상하좌우(답안 예시)

#입력
n = int(input())
x,y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    #이동 수행
    x,y = nx, ny
    
print(x,y)
            

# +
#113pg
#시각(내풀이)

n = int(input())
cnt = 0

for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1
                
print(cnt)


# +
#115pg
#왕실의 나이트(내풀이)

n = list(input())
x = int(n[1]) 
y = ord(n[0])-ord('a')+1

cnt = 0

direct = [[2,1],[2,-1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]]

for i in range(len(direct)):
    nx = x + direct[i][0]
    ny = y + direct[i][1]
    if nx < 1 or nx > 8 or ny <1 or ny >8:
        continue
    else:
        cnt += 1

print(cnt)

# +
#118pg
#게임 개발(답안예시)

#N,M을 공백으로 구분하여 입력 받기
n,m = map(int,input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
#현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction  = map(int,input().split())
d[x][y] = 1 #현재 좌표 방문 처리 

#전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북, 동, 남, 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
#시뮬레이션 시작
count = 1
turn_time = 0

while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    #회전한 이후 가보지 않은 칸이 존재하는 경우 이동
    if array[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

#정답 출력
print(count)
        
# -


