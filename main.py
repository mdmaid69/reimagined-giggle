n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time