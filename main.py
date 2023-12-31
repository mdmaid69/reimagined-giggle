def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a