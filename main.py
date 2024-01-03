def find_difference(list1, list2):
        return set(list1) - set(list2)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a