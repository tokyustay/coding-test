n, m = map(int, input().split())

basket = [0]*n

for x in range(0,m) :
    i, j, k = map(int, input().split())
    for y in range(i-1, j, 1) :
        basket[y] = k

print(*basket)