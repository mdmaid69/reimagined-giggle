def remove_duplicates(lst):
        return list(set(lst))
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a