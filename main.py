  import math
  def calculate_square_root(n):
        return math.sqrt(n)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a