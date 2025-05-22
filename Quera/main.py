n = int(input())

arr = []

for i in range(n):
    x = input()
    if len(x) < 100 and int(x) >= 0:
        arr.append(int(x))


m = max(arr)
for i in range(0, m):
    if i not in arr:
        print(i)
        break
