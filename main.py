import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import array
def get_array_buffer_info(array):
        return array.buffer_info()