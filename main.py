  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a