import array
def get_array_as_memoryview(array):
        return memoryview(array)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))