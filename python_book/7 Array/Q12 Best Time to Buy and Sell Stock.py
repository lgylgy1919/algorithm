import sys
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
prices = [7, 1, 5, 3, 6, 4]

# 브루트 포스로 계산


def max_profit(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j]-price, max_price)

    return max_price

# 저점과 현재 값과의 차이 계산


def max_profit2(prices):
    max_profit = 0
    min_price = max(prices)
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(price - min_price, max_profit)

    return max_profit


max_profit2(prices)


def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)

    return profit


def maxProfit(prices)
