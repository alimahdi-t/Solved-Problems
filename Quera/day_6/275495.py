import math

# n: number of car
# f: length of flower street
n, f = map(int, input().split())
t = math.inf
ans = -1
for i in range(1, n + 1):
    location, speed = map(float, input().split())
    distance = f - location
    time = distance / speed

    if time < t:
        t = time
        ans = i

print(ans)
