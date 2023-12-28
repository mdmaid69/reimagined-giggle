def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
n = 10
print("Square numbers:", [x**2 for x in range(n)])