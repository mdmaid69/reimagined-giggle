import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import array
def convert_array_to_string(array):
        return array.tostring()