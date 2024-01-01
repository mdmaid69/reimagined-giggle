def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)