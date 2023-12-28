import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)