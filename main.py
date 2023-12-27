import array
def get_array_index(array, item):
        return array.index(item)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))