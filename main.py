n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))