from collections import deque
import copy

def make_wall(cnt) :
    if cnt == 3 : 
        bfs()
        return

    for i in range(r) :
        for j in range(c) :
            if lab[i][j] == 0 :
                lab[i][j] = 1
                make_wall(cnt + 1)
                lab[i][j] = 0

def bfs() :
    queue = deque()
    temp = copy.deepcopy(lab)

    for i in range(r) :
        for j in range(c) :
            if temp[i][j] == 2 :
                queue.append((i,j))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c :
                continue
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                queue.append((nx,ny))
    
    global ans
    check = 0
    for i in range(r) :
        check += temp[i].count(0)

    ans = max(ans, check)     

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
r, c = map(int, input().split())

lab = [[] for _ in range(r)]
for i in range(r) :
    lab[i] = list(map(int, input().split()))

make_wall(0)
print(ans)

# copy = deepcopy, shallowcopy는 주소값도 공유(b = a[])