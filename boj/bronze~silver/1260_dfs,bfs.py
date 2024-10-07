import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(150000)

def bfs (graph, start, visited):
    global cnt
    visited[start] = cnt
    cnt += 1
    queue = deque([start])
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if visited[i] == 0 :
                queue.append(i)
                visited[i] = cnt
                cnt += 1

def dfs(graph, start, visited) :
    global cnt
    visited[start] = cnt
    graph[start].sort()
    for i in graph[start] :
        if visited[i] == 0 :
            cnt += 1
            dfs(graph, i, visited)

n, m, v = map(int, input().split())

visited = [0]*(n+1)
graph = [[] for _ in range(n + 1)]
cnt = 1

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(visited)) :
    graph[i].sort()

dfs(graph, v, visited)

print(*visited[1:])

visited = [0]*(n+1)
cnt = 1

bfs(graph, v, visited)

print(*visited[1:])