def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities