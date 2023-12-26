n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time