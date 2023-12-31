def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))