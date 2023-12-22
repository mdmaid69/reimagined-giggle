import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def get_string_from_array(array):
        return array.tobytes()