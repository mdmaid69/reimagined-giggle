import array
def get_bytes_from_array(array):
        return array.tobytes()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a