def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)