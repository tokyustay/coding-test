def sum(a,b) :
    return a + b

t = int(input())
result = []
for i in range(t) :
    a, b = map(int, input().split())
    result.append(sum(a,b))
for i in range(len(result)) :
    print(result[i])
