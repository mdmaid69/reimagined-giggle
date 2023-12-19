def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a