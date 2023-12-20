import itertools
print(list(itertools.permutations([1, 2, 3])))
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)