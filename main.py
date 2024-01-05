import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a