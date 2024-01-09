def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import itertools
print(list(itertools.permutations([1, 2, 3])))