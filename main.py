import array
def iterate_over_array(array):
        for item in array:
        print(item)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a