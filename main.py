import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)