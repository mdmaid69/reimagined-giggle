import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import array
def insert_into_array(array, i, item):
        array.insert(i, item)