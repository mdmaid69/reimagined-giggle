import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)