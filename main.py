import array
def set_array_item(array, i, item):
        array[i] = item
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))