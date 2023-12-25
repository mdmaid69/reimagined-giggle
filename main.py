import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))