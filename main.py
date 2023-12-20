import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time