initial_money, n = map(int, input().split())
if initial_money == 0:
    print(0)
elif n == 0:
    print(initial_money)
else:
    prices = [int(input()) for _ in range(n)]
    coins = 0  # number of coins
    cash = initial_money  # amount of cash
    for i in range(n - 1):
        if prices[i] < prices[i + 1]:
            # buy coins today
            buy = cash // prices[i]
            cash -= buy * prices[i]
            coins += buy
            # sell the coins tomorrow
            cash += coins * prices[i + 1]
            coins = 0

    # Sell any remaining coins on the last day
    cash += coins * prices[-1]

    print(cash)


