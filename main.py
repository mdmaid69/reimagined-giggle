def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])