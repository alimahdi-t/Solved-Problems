# Problem B : Chaarshanbegaan at Cafebazaar
import math

n = int(input())

score = 0
for i in range(n):
    x, y = map(int, input().split())
    distance = math.sqrt(x ** 2 + y ** 2)

    if distance <= 10:
        score += 10
    elif 10 < distance <= 30:
        score += 9
    elif 30 < distance <= 50:
        score += 8
    elif 50 < distance <= 70:
        score += 7
    elif 70 < distance <= 90:
        score += 6
    elif 90 < distance <= 110:
        score += 5
    elif 110 < distance <= 130:
        score += 4
    elif 130 < distance <= 150:
        score += 3
    elif 150 < distance <= 170:
        score += 2
    elif 170 < distance <= 190:
        score += 1

print(score)