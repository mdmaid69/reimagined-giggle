n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)