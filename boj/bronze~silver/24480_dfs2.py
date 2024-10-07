import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(graph, start, visited) :
    global cnt
    visited[start] = cnt
    graph[start].sort(reverse = True)
    for i in graph[start] :
        if visited[i] == 0 :
            cnt += 1
            dfs(graph, i, visited)

n, m, v = map(int, input().split())
cnt = 1
visited = [0]*(n+1)

graph = [[] for _ in range(n + 1)]

for i in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, v, visited)

for i in visited[1:] :
    print(i)