n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)