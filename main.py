def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a