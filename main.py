import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import array
def get_string_from_array(array):
        return array.tobytes()