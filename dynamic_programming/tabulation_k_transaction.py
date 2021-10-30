def max_profit_with_k_transactions(prices, k):
    if not prices:
        return 0
    all_price = [[0 for _ in prices] for _ in range(k + 1)]
    for transaction_num in range(1, k + 1):
        maximum_in_row = float("-inf")
        for day in range(1, len(prices)):
            maximum_in_row = max(maximum_in_row, all_price[transaction_num-1][day-1] - prices[day-1])
            all_price[transaction_num][day] = max(all_price[transaction_num][day-1], maximum_in_row + prices[day])
    return all_price[-1][-1]


if __name__ == "__main__":
    max_profit_with_k_transactions(prices=[5, 11, 3, 50, 60, 90], k=2)

#     5  11   3  50  60  90
# 0   0   0   0   0   0   0
# 1   0   6   6  47  57  87
# 2   0   6   6  53  63  93