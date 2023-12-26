import array
def extend_array(array, iterable):
        array.extend(iterable)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))