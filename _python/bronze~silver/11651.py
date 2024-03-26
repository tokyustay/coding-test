n = int(input())

arr = [[0]*2 for _ in range(n)]

for i in range(0,n) :
    x, y = map(int, input().split())
    arr[i][0], arr[i][1] = x, y

arr.sort(key = lambda x:(x[1], x[0]))
for i in range(n) :
    print(*arr[i])