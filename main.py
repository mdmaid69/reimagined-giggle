import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def get_array_buffer_info(array):
        return array.buffer_info()