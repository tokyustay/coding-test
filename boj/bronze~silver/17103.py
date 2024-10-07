import sys

arr = [True for i in range(1000001)]

# 아리토스테네스의 체

m = int(len(arr)**0.5) # 어떤 수 N의 가장 큰 소수 팩터(소수 인수)는 N의 제곱근 이하라는 수학적 성질 

for i in range(2, m + 1) :
    if arr[i] :
        for j in range(2*i, 1000001, i) :
            arr[j] = False

T = int(input())

for i in range(T) :
    n = int(input())
    count = 0
    for j in range(2, n//2 + 1) : #1은 소수가 아니므로 2부터, n의 절반까지만 탐색-> 이후론 대칭이므로
        if arr[j] and arr[n - j] :
            count += 1
    print(count)

