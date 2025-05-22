from collections import Counter

n = int(input())
groups = list(map(int, input().split()))
d = Counter(groups)
cnt = 0

if d.get(4):
    cnt += d.get(4)
    d[4] = 0

if d.get(3):
    m = min(d[3], d[1])
    cnt += m
    d[3] = d[3] - m
    d[1] = d[1] - m
    cnt += d[3]
    d[3] = 0
if d.get(2):
    m = d.get(2)
    cnt += m // 2
    d[2] = m % 2

    # 2 and 1
    if d.get(2) and d.get(1):
        m = d[1]
        d[2] = 0
        if m >= 2:
            d[1] -= 2
            cnt += 1
        elif m >= 1:
            d[1] -= 1
            cnt += 1
    elif d.get(2):
        cnt += d[2]
        d[2] = 0
if d.get(1):
    m = d[1]
    cnt += m // 4
    if m % 4 != 0:
        cnt += 1

print(cnt)













# while groups:
#     if len(groups) <= 1:
#         cnt += 1
#     else:
#         if groups[0] == 4:
#             cnt += 1
#             groups = groups[1:]
#             continue
#         elif groups[0] == 403:
#             if groups[-1] == 1:
#                 groups = groups[1:-1]
#                 cnt += 1
#             else:
#                 groups = groups[1:]
#                 cnt += 1
#         elif groups[0] == 2:
#             if groups[1] == 2:
#                 groups = groups[2:]
#                 cnt += 1
#             elif groups[-1] == 1:
#                 groups = groups[1:-1]
#         else: groups[0] == 1

