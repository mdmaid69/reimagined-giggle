def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])