import array
def get_array_as_memoryview(array):
        return memoryview(array)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))