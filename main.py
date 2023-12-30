  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a