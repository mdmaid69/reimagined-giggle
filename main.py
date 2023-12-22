def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))