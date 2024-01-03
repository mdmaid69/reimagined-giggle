import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import array
def remove_from_array(array, item):
        array.remove(item)