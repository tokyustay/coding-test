import sys
input = sys.stdin.readline

s = input().strip() # 문자열은 리스트다

# list_s = list(s)

result = []

for i in range(1, len(s)) :
    check = len(s) - i
    if check == 0 : continue
    for j in range(0, check + 1, 1) :
        result.append(s[j:j+i])
result.append(s)

# result = set([tuple(x) for x in result])

result = set(result)
print(len(result))
