import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = dict()

for i in range(1, n + 1) :
    name = input().strip()
    arr[name] = str(i)

reversed_arr = dict(map(reversed, arr.items())) # value, key값 반전
print_array = []

for i in range(1,m + 1) :
    check = input().strip()
    if check.isdigit() : # isdigt = 문자열이 숫자로만 이루어져있는지 판별
        print_array.append(reversed_arr[check])
    else :
        print_array.append(arr[check])
        
    
for i in print_array :
    print(i)