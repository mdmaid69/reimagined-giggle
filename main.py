import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))