import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def find_common_elements(list1, list2):
        return set(list1) & set(list2)