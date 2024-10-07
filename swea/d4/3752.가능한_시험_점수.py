# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 2 3 5 => 0, 2, 3, 5, 7, 8, 10
    n = int(input())
    arr = list(map(int, input().split()))
    lst = [1] + [0]*sum(arr)
    tot = [0]
    
    for i in arr :
        for j in range(len(tot)) :
            if not lst[i + tot[j]] :
                tot.append(i + tot[j])
                lst[i + tot[j]] = 1

    print(f"#{test_case} {len(tot)}")
    # ///////////////////////////////////////////////////////////////////////////////////
