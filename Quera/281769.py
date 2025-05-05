n = int(input())
s = [i for i in range(1, n + 1)]
sum_of_numbers = sum(s)
expression = " + ".join(str(i) for i in s)
print(f"{expression} = {sum_of_numbers}")
