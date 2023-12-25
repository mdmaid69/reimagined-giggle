import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a