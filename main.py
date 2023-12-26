def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets