import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def get_array_item_count(array, item):
        return array.count(item)