n,m = map(int, input().split())

arr=[]

for i in range(1, n+1) :
    arr.append(i)

for i in range(m) :
    x,y = map(int, input().split())
    temp = arr[x-1:y]
    temp.reverse()
    arr[x-1:y] = temp
print(*arr)

# arr[x-1:y].reverse() = 슬라이싱된 리스트는 원본 리스트의 복사본을 생성하기 때문에, 이 복사본을 바로 .reverse()로 처리해도 원본 arr 리스트에는 아무런 영향을 주지 않습니다.