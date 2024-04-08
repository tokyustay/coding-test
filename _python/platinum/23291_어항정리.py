from collections import deque

def get_diff(arr) :
    q = arr[0]
    return max(q) - min(q)

def rotate(arr) :
    while 1 :
        if len(arr) > len(arr[0]) - len(arr[-1]) : break
        map = []
        r = len(arr)
        c = len(arr[-1])

        for i in range(r) :
            temp = deque()
            for _ in range(c) :
                temp.append(arr[i].popleft())
            map.append(temp)
        
        arr = [arr[0]]
        rotated = rotate_90(map)
        for row in rotated :
            arr.append(deque(row))

    return arr

def rotate_90 (map) :
    temp = [[0]*len(map) for _ in range(len(map[0]))]
    for i in range(len(map[0])) :
        for j in range(len(map)) :
            temp[i][j] = map[j][len(map[0]) -1-i]
    return temp

def fix_fish(arr) :
    dp = [[0]*len(arr[x]) for x in range(len(arr))]
    for x in range(len(arr)) :
        for y in range(len(arr[x])) :
            for dir in directions :
                nx = x + dir[0]
                ny = y + dir[1]

                if 0 <= nx < len(arr) and 0<= ny < len(arr[nx]) :
                    if arr[x][y] > arr[nx][ny] :
                        diff = (arr[x][y] - arr[nx][ny]) // 5
                        if diff >= 1 :
                            dp[x][y] -= diff
                    else :
                        diff = (arr[nx][ny] - arr[x][y]) // 5
                        if diff >= 1 :
                            dp[x][y] += diff
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            arr[i][j] += dp[i][j]

def linear(arr) :
    temp = deque()
    for i in range(len(arr[-1])) :
        for j in range(len(arr)) :
            temp.append(arr[j][i])

    for i in range(len(arr[-1]), len(arr[0])) :
        temp.append(arr[0][i])

    return [temp]

def half(arr) :
    temp = deque()
    for i in range(n // 2) :
        temp.append(arr[0].popleft())
    rotated = rotate_180([temp])
    arr += rotated

    left = []
    for i in range(2) :
        data = deque()
        for j in range(n//4) :
            data.append(arr[i].popleft())
        left.append(data)
    rotated = rotate_180(left)
    arr += rotated

def rotate_180(arr) :
    temp = []
    for i in reversed(range(len(arr))) :
        arr[i].reverse()
        temp.append(arr[i])

    return temp
            
        

 

n, k = map(int, input().split())
fishbowl = [deque(map(int, input().split()))]
directions = [(-1,0), (1,0), (0,-1), (0,1)]
total = 0


while 1 :
    diff = get_diff(fishbowl)
    if diff <= k :
        print(total)
        break

    minimum = min(fishbowl[0])
    for i in range(len(fishbowl[0])) :
        if fishbowl[0][i] == minimum :
            fishbowl[0][i] += 1
    
    value = fishbowl[0].popleft()
    fishbowl.append(deque([value]))

    fishbowl = rotate(fishbowl)
    fix_fish(fishbowl)
    fishbowl = linear(fishbowl)
    half(fishbowl)
    fix_fish(fishbowl)
    fishbowl = linear(fishbowl)

    total += 1

    
