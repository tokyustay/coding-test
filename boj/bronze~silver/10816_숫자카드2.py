import sys
from bisect import bisect_left, bisect_right
#bisect library

def length(a, x) :
    right = bisect_right(a,x)
    left = bisect_left(a,x)
    return right - left

input = sys.stdin.readline

result = []

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())

check = list(map(int, input().split()))

for i in check :
    num = length(arr, i)
    result.append(num)

print(*result)