import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n) :
    arr.append(input().strip())

arr = list(set(arr)) # 중복제거 (집합 만들기)
arr.sort()
arr.sort(key = len)
for i in arr :
    print(i)