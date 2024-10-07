import sys
input = sys.stdin.readline

input()

a = list(map(int, input().split()))
b = list(map(int, input().split()))
len_a = len(a)
len_b = len(b)
for i in b :
    append_a = a.append(i)
set_a = set(a)
intersection = len(a) - len(set_a)
print((len_a - intersection) + (len_b - intersection))