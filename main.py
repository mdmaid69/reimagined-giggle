import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a