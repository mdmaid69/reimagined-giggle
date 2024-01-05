  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a