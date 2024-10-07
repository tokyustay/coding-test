import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for _ in range(n) :
    array[int(sys.stdin.readline())] += 1

for i in range(len(array)) :
    for j in range(array[i]) :
        print(i)

# 계수정렬