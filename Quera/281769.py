n, k = map(int, input().split())
max_groups = n - k + 1
groups = min(k, max_groups)
print(k - groups)


