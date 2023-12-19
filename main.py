def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])