def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)