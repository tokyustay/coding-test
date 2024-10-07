import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = dict()
count = 0

for _ in range(n) :
    word = input()
    arr[word] = True

for _ in range(m) :
    check = input()
    if check in arr.keys() :  # if a in b = b에서 a찾기 
        # dict = (key : value)
        count += 1

print(count)