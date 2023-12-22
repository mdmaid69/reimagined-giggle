import itertools
print(list(itertools.permutations([1, 2, 3])))
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable