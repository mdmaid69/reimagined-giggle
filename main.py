import random
def generate_random_number(start, end):
        return random.randint(start, end)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"