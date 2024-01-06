numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))