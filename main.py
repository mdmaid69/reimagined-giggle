n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time