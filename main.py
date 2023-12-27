  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable