numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))