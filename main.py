  def multiply_numbers(x, y):
        return x * y
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a