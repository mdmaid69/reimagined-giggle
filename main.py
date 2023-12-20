import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array