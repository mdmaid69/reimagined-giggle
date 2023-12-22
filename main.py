def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)