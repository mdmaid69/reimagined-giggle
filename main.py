n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time