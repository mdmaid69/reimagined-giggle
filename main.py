text = "Hello, world!"
print("Reversed:", text[::-1])
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))