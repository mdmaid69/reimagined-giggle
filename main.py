def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))