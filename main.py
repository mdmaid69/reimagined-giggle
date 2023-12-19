import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))