def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets