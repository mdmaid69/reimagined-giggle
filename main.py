def calculate_average(lst):
        return sum(lst) / len(lst)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a