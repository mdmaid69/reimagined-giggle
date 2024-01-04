import array
def iterate_over_array(array):
        for item in array:
        print(item)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a