n = int(input())
d = []

for i in range(n) :
    d.append(int(input()))
    
for j in range(n) :
    temp = j
    for k in range(j, n) :
        if d[temp] > d[k] :
            temp = k
    d[j], d[temp] = d[temp], d[j]

print(*d, sep=('\n'))

# *array = 배열 열기, sep = 나누기