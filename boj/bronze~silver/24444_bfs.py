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


bfs(graph, v, visited)

for i in range(1, len(visited)) :
    print(visited[i])