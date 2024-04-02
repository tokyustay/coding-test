import sys

def binary_search(arr, x, start, end) :
    mid = (start + end) // 2
    if arr[mid] == x :
        d.append(1)
        return
    if start > end :
        d.append(0)
        return                   # return 1, return 0은 1과 0을 반환하지않음
    if arr[mid] > x :
        end = mid - 1
    elif arr[mid] < x :
        start = mid + 1
    binary_search(arr, x, start, end)

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

m = int(input())

check = list(map(int, input().split()))

arr.sort()

d = []

for i in check :
    binary_search(arr, i, 0, len(arr) - 1)

print(*d)