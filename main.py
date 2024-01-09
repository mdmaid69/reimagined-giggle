import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import array
def get_array_as_frozenset(array):
        return frozenset(array)