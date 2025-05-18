import sys
sys.setrecursionlimit(100010)

n, m = map(int, input().split())
s, t = map(int, input().split())  # start vertex (s) and goal vertex (t)

s -= 1
t -= 1

adj = [[] for _ in range(n)]
mark = [False] * n  # create


for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)


def DFS(v):
    mark[v] = True
    for u in adj[v]:
        if not mark[u]:
            DFS(u)

DFS(s)

if mark[t]:
    print('YES')
else:
    print('NO')
