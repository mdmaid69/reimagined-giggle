import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)