teams = int(input())
games = teams * (teams - 1)
arr = []
for _ in range(teams):
    arr.append(tuple(map(int, input().split())))
ans = 0
for i in range(teams):
    h_1, h_2 = arr[i]
    for j in range(teams):
        if i == j:
            continue
        g_1, g_2 = arr[j]
        if h_1 == g_2:
            ans += 1
print(ans)