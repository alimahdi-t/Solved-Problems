n = int(input())
f = list(map(int, input().split()))

f = [0] + f
found = False
for i in range(1 , n + 1):
    a = f[i]
    b = f[a]
    c = f[b]

    if c == i and i != a and a != b and b != c:
        found = True
        break

print("YES" if found else "NO")
