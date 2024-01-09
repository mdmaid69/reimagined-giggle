def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])