def sort_numbers(numbers):
        return sorted(numbers)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a