import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)