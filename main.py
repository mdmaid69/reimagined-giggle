import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal