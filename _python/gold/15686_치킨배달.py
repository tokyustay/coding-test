n, m = map(int, input().split())

min_ans = 9999999
house = []
chicken = []

for i in range(n) :
    arr = list(map(int, input().split()))

    for j in range(n) :
        if arr[j] == 1 :
            house.append((i,j))
        elif arr[j] == 2 :
            chicken.append((i,j))

visited = [False] * len(chicken)

def dfs(index,cnt) :

    global min_ans

    if cnt == m :
        ans = 0
        for i in house :
            distance = 9999999
            for j in range(len(visited)) :
                if visited[j] :
                    check = abs(i[0] - chicken[j][0]) + abs(i[1] - chicken[j][1])
                    distance = min(distance, check)
            ans += distance
        min_ans = min(ans,min_ans)
        
        return
    

    for i in range(index, len(chicken)) :
        if not visited[i] :
            visited[i] =True
            dfs(i + 1, cnt + 1)
            visited[i] = False

dfs(0,0)

print(min_ans)