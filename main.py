def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)