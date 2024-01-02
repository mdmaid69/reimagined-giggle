numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))