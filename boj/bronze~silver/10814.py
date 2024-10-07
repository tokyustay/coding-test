import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n) :
    arr.append(list(input().split()))

arr.sort(key = lambda x:int(x[0]))

for i in arr :
    print(*i)