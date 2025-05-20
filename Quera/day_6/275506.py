# Hezardastan’s Annual Report
import math

n = int(input())
ans = 0
pages = list(map(int, input().split()))

for i in pages:
    ans += math.ceil(i / 2)

print(ans)

