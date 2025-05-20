n = int(input())

arr = [100, 20, 10, 5, 1]
cnt = 0
for num in arr:
    cnt += n // num
    n = n % num


print(cnt)
