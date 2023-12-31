import array
def get_array_item(array, i):
        return array[i]
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))