import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))