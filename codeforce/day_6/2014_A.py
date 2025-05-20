t = int(input())

for t in range(t):
    n, k = map(int, input().split())
    # if gold of any person was greater or equal to k, robin will take its gold
    arr = list(map(int, input().split()))
    robin_gold = 0
    cnt = 0

    for i in arr:
        if i == 0 and robin_gold:
            cnt += 1
            robin_gold -= 1
        elif i != 0 and i >= k:

            robin_gold += i
            i = 0
    print(cnt)
