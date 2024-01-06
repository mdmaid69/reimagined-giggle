import itertools
print(list(itertools.permutations([1, 2, 3])))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time