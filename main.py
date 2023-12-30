def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)