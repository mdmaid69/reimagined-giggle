def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))