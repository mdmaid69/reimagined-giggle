import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a