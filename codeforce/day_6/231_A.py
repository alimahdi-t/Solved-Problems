n = int(input())
cnt = 0
for _ in range(n):
    m = list(map(int, input().split())).count(1)
    if m >= 2:
        cnt += 1
print(cnt)
