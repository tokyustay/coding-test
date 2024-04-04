import sys
input = sys.stdin.readline

s = input().strip()

bomb = input().strip()
bomb = list(bomb)
arr = []

for i in list(s) :
    arr.append(i)
    if len(arr) < len(bomb) : continue
    if arr[len(arr) - len(bomb):len(arr) + 1] == bomb :
        for _ in range(len(bomb)):
            arr.pop()

    
if len(arr) == 0 : print('FRULA') 
else : print(*arr, sep="")

# replace 함수는 시간복잡도가 크다