import sys

n = int(sys.stdin.readline())
d = []

for i in range(n) :
    d.append(int(sys.stdin.readline()))
    
d.sort()

for j in range(len(d)) :
    print(d[j])

# sys