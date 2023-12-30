import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def find_union(list1, list2):
        return set(list1) | set(list2)