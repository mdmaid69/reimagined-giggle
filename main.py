import array
def get_array_buffer_info(array):
        return array.buffer_info()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a