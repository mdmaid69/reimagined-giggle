n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))