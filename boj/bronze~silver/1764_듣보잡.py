import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hear = dict()
see = dict()
result = []

for i in range(n) :
    hear[input().strip()] = i

for i in range(m) :
    see[input().strip()] = i

len_hear = len(hear.keys())
len_see = len(see.keys())

for i in hear.keys() :
    if i in see.keys() :
        result.append(i)

print(len(result))

result.sort()

for i in result :
    print(i)