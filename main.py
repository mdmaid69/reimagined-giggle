import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def get_bytes_from_array(array):
        return array.tobytes()