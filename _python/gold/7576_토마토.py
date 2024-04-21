from collections import deque

m, n = map(int, input().split())
maped = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
dx, dy = [-1,1,0,0],[0,0,-1,1]
result = 0

for i in range(n) :
    for j in range(m) :
        if maped[i][j] == 1 :
            queue.append([i,j])

def bfs() :
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and maped[nx][ny] == 0:
                maped[nx][ny] = maped[x][y] + 1
                queue.append([nx,ny])

bfs()
for i in maped :
    for j in i :
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)        