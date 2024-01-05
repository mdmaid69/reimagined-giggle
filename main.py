import itertools
print(list(itertools.permutations([1, 2, 3])))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))