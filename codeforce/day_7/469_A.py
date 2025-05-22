n = int(input())

s1 = set(map(int, input().split()[1:]))  # Skipping first number (count)
s2 = set(map(int, input().split()[1:]))

s = s1.union(s2)

flag = True
for i in range(1, n + 1):
    if i not in s:
        print("Oh, my keyboard!")
        flag = False
        break

if flag:
    print("I become the guy.")
