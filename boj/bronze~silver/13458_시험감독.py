n = input()
a = []

if n == 1 :
    a[0] = int(input())
else :
    a = list(map(int, input().split()))

b, c = map(int, input().split())

total = 0

for i in range(len(a)) :
    a[i] -= b

total += len(a)

for i in range(len(a)) :
    if a[i] > 0 :
        if a[i] % c == 0 : total += (a[i] // c)
        else : total += (a[i] // c) + 1

print(total)