def sort_numbers(numbers):
        return sorted(numbers)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a