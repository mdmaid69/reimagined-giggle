def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)