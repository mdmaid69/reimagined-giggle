n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets