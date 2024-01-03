n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time