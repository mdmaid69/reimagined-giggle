def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
x = 10
y = 20
print("Sum:", x + y)