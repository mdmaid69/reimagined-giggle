import array
def append_to_array(array, item):
        array.append(item)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))