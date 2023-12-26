import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable