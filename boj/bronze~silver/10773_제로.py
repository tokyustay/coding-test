n = int(input())
arr = []

for i in range(n) :
    m = int(input())
    if m == 0 :
        arr.pop()
    else :
        arr.append(m)

sum = 0

for i in arr :
    sum += i

print(sum)