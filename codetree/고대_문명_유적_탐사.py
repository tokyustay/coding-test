from collections import deque
from copy import deepcopy

def rotate(grid, sy, sx, cnt) :
    copied = deepcopy(grid)
    subgrid = deepcopy([row[sx:sx+3] for row in grid[sy:sy+3]])
    for _ in range(cnt) :
        subgrid = [list(row) for row in zip(*subgrid[::-1])]
    for i in range(3) :
        for j in range(3) :
            copied[sy+i][sx+j] = subgrid[i][j]
    return copied

def cal_score(grid) :
    score = 0
    visit = [[False] * 5 for _ in range(5)]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    for i in range(5) :
        for j in range(5) :
            if not visit[i][j] :
                visit[i][j] =True
                dq, trace = deque([(i,j)]), deque([(i,j)])
                while dq :
                    cur = dq.popleft()
                    for k in range(4) :
                        ny, nx = cur[0]+dy[k], cur[1]+dx[k]
                        if 0<=nx<5 and 0<=ny<5 and visit[ny][nx] == False and grid[cur[0]][cur[1]] == grid[ny][nx] :
                            trace.append([ny,nx])
                            dq.append((ny,nx))
                            visit[ny][nx] = True
            
            if len(trace) >= 3 :
                score += len(trace)
                while trace :
                    t = trace.popleft()
                    grid[t[0]][t[1]] = 0

    return score

def fill(grid, wait) :
    for j in range(5) :
        for i in range(4, -1, -1) :
            if grid[i][j] == 0 :
                p = wait.popleft()
                grid[i][j] = p

    return grid

K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
M_list = list(map(int, input().split()))
M_list = deque(M_list)

for _ in range(K):
    maxScore = 0
    ismax = False
    maxScoreGrid = None
    
    for cnt in range(1,4) :
        for j in range(3) :
            for i in range(3) :
                rotated = rotate(grid, i, j, cnt)
                score = cal_score(rotated)
                if maxScore < score :
                    maxScore = score
                    ismax = True
                    maxScoreGrid = rotated

    if ismax == False :
        break
    
    grid = maxScoreGrid
    while True:
        gird = fill(grid, M_list)
        newScore = cal_score(grid)
        if newScore == 0 :
            break
        maxScore += newScore

    print(maxScore, end = " ")

