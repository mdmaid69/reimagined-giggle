n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))