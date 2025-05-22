t = int(input())

for _ in range(t):
    n = int(input())
    digits = sorted(list(map(int, input().split())))[::-1]
    digits[-1] += 1
    ans = 1
    for i in digits:
        ans *= i
    print(ans)

