def find_union(list1, list2):
        return set(list1) | set(list2)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a