d = [0]*6
max = 0
check = 0

a = list(map(int, input().split()))

for i in a :
    d[i - 1] += 1

for j in range(0, len(d)) :
    if d[j] == 3 :
        print(10000 + (j+1)*1000)
        check += 1
    elif d[j] == 2 :
        print(1000 + (j+1)*100)
        check += 1
    elif d[j] == 1 :
        max = j + 1

if check == 0 :
    print(max*100)