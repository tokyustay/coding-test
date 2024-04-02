import sys

input = sys.stdin.readline

n = int(input())
arr = dict()

for _ in range(n) :
    name, status = input().strip().split()
    arr[name] = status

for i in arr.keys() :
    if arr[i] == "enter" :
        arr[i] = True
    else :
        arr[i] = False

sorted_arr = dict(sorted(arr.items(), key = lambda x: x[0], reverse = True))
# dictionary를 정렬하는방법 = sorted ( dictionary.items(), key = lambda x : x)

for i in sorted_arr.keys():
    if arr[i] == True :
        print(i)
    else :
        continue
