import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))