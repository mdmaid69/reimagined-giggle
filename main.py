def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import itertools
print(list(itertools.permutations([1, 2, 3])))