from collections import deque

def bfs(x, y, color) :
    q = deque()
    q.append([x,y])
    dx = [-1, 0, 1, 0]
    dy = [0,1,0,-1]
    blocks, rainbows = 1, 0
    block, rainbow = [[x,y]], []

    while q :
        x,y = q.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == color :
                visited[nx][ny] = 1
                q.append([nx,ny])
                blocks += 1
                block.append([nx,ny])

            elif 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 0 :
                visited[nx][ny] = 1
                q.append([nx,ny])
                blocks += 1
                rainbows += 1
                rainbow.append([nx,ny])

    for x, y in rainbow :
        visited[x][y] = 0

    return [blocks, rainbows, block + rainbow]

def remove(block) :
    for x, y in block :
        arr[x][y] = -2

def gravity(arr) :
    for i in range(n-2, -1, -1) :
        for j in range(n) :
            if arr[i][j] > -1 :
                r = i
                while 1 :
                    if 0 <= r + 1 < n and arr[r+1][j] == -2 :
                        arr[r+1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else :
                        break

def rotate90(arr) :
    rotated = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            rotated[n-1-j][i] = arr[i][j]

    return rotated

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
score = 0

while 1 :
    visited = [[0]*n for _ in range(n)]
    block = []
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] > 0 and not visited[i][j] :
                visited[i][j] = 1
                search = bfs(i,j,arr[i][j])
                if search[0] >= 2 :
                    block.append(search)
    block.sort(reverse=True)

    if not block :
        break
    remove(block[0][2])
    score += block[0][0]**2

    gravity(arr)

    arr = rotate90(arr)
    gravity(arr)

print(score)